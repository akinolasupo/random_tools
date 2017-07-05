#!/usr/bin/env python
from travispy import TravisPy
import sys, os

if len (sys.argv) != 2 :
    print("Usage: python travis_sync.py <repositoryname>")
    sys.exit (1)

travis = TravisPy.github_auth(os.environ['GITHUB_TOKEN'])
repo = travis.repo(sys.argv[1])

if not repo.active:
   enabled = repo.enable() # Switch is now on
   if enabled:
      print("Repository enabled")
else:
   print("Repository already enabled")


