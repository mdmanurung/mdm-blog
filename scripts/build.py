"""Clean offline content build; no publishing or provider synchronization."""
import argparse
import os
from pathlib import Path
import shutil
import subprocess
import sys
from content import ROOT, read_yaml
p=argparse.ArgumentParser(); p.add_argument('--production',action='store_true'); args=p.parse_args()
quarto=os.getenv('QUARTO_BIN') or shutil.which('quarto')
if not quarto: raise SystemExit('Quarto 1.8.27 required; set QUARTO_BIN or add it to PATH')
config=read_yaml(ROOT/('_quarto.yml' if args.production else '_quarto-staging.yml'))
env=dict(os.environ,MDM_SITE_URL=config['website']['site-url'],MDM_STAGING='0' if args.production else '1')
subprocess.run([sys.executable,'scripts/validate_content.py'],cwd=ROOT,check=True)
shutil.rmtree(ROOT/'_preview',ignore_errors=True)
subprocess.run([sys.executable,'scripts/render_content.py'],cwd=ROOT,check=True)
command=[quarto,'render']+([] if args.production else ['--profile','staging'])
subprocess.run(command,cwd=ROOT,env=env,check=True)
subprocess.run([sys.executable,'scripts/check_site.py'],cwd=ROOT,check=True)
