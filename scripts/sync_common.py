"""Bounded network reads and atomic candidate writes; curated files are never targets."""
from datetime import datetime, timezone
import json
import os
from pathlib import Path
import tempfile
import time
from urllib.error import HTTPError
from urllib.request import Request, urlopen
import yaml
from content import ROOT, url

def now(): return datetime.now(timezone.utc).isoformat(timespec='seconds')

def fetch(address, *, token=None):
    if not url(address): raise ValueError('Fetch URL must use HTTPS')
    headers = {'User-Agent':'mdm-portfolio-metadata/1.0','Accept':'application/json'}
    if token: headers['Authorization']='Bearer '+token
    for attempt in range(3):
        try:
            with urlopen(Request(address,headers=headers),timeout=20) as response:
                body=response.read(8_000_001)
                if len(body)>8_000_000: raise ValueError('Response exceeds 8 MB limit')
                return body
        except HTTPError as exc:
            if exc.code not in {429,500,502,503,504} or attempt==2: raise
            time.sleep(min(2**attempt,4))
    raise RuntimeError('Fetch failed')

def json_fetch(address,**kwargs): return json.loads(fetch(address,**kwargs))

def write_cache(name,data,root=ROOT):
    target=root/'cache'/name
    target.parent.mkdir(exist_ok=True)
    # Atomic replacement only after the entire provider response validates.
    fd,temp=tempfile.mkstemp(dir=target.parent,prefix='.pending-')
    try:
        with os.fdopen(fd,'w') as stream: yaml.safe_dump(data,stream,sort_keys=False,allow_unicode=True)
        os.replace(temp,target)
    finally:
        if Path(temp).exists(): Path(temp).unlink()
