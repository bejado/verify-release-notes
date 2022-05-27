#!/usr/bin/env python3

from github import Github
import sys

authentication_token = sys.argv[1]
if not authentication_token:
    sys.stderr.write('Error: a GitHub token must be the first argument to this script.\n')
    sys.exit(1)

g = Github(authentication_token)

REPO_NAME = "bejado/verify-release-notes"
repo = g.get_repo(REPO_NAME)

pull_request = repo.get_pull(1)
pull_request.create_issue_comment('Hi, I\'m Filament bot!')

print('Done!')
