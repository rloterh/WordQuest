"""Run a read-only Codex review and retain local evidence; never publish or merge."""
import argparse
from datetime import datetime
import json
from pathlib import Path
import shutil
import subprocess
import sys


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument('--base', default='origin/dev', help='Actual PR base; fetch it first')
    args = parser.parse_args()
    repository = Path(__file__).resolve().parents[2]
    codex = shutil.which('codex')
    if not codex:
        parser.error('Codex CLI is not on PATH; install/sign in before review.')

    def git(*arguments):
        return subprocess.check_output(['git', *arguments], cwd=repository,
                                       text=True).strip()

    base = git('rev-parse', '--verify', args.base + '^{commit}')
    head = git('rev-parse', 'HEAD')
    status = git('status', '--porcelain')
    directory = repository / 'Artifacts/Reviews' / datetime.now().strftime('%Y%m%d-%H%M%S')
    directory.mkdir(parents=True)
    command = [codex, 'review', '--base', base,
               '-c', 'sandbox_mode="read-only"', '-c', 'approval_policy="never"']
    print(f'Reviewing {head} against {args.base} ({base}). Reports: {directory}', flush=True)
    # Direct files avoid inherited connector pipes holding the console stream open.
    with (directory / 'review.txt').open('w', encoding='utf-8') as output, \
            (directory / 'diagnostics.txt').open('w', encoding='utf-8') as diagnostics:
        result = subprocess.run(command, cwd=repository, stdout=output, stderr=diagnostics)
    evidence = {'base_ref': args.base, 'base_sha': base, 'head_sha': head,
                'worktree_status_at_start': status, 'exit_code': result.returncode,
                'head_unchanged': git('rev-parse', 'HEAD') == head,
                'worktree_status_unchanged': git('status', '--porcelain') == status}
    (directory / 'run.json').write_text(json.dumps(evidence, indent=2) + '\n', encoding='utf-8')
    print((directory / 'review.txt').read_text(encoding='utf-8', errors='replace'))
    print(f'Review process exit: {result.returncode}. Read findings; this is not merge approval.')
    return result.returncode


if __name__ == '__main__':
    sys.exit(main())
