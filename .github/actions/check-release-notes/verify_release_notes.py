#!/usr/bin/env python3

from github import Github
import sys

def print_usage():
    print('Verify that a GitHub pull request modifies RELEASE_NOTES')
    print()
    print('Usage:')
    print('  verify_release_notes.py <github token> <pull number> <bypass label name> <release notes file>')

# The first argument is the path to this script.
if len(sys.argv) < 5:
    print_usage()
    sys.exit(1)

authentication_token = sys.argv[1]
pull_number = sys.argv[2]
bypass_label_name = sys.argv[3]
release_notes_file = sys.argv[4]

g = Github(authentication_token)

REPO_NAME = "bejado/verify-release-notes"
repo = g.get_repo(REPO_NAME)

pull_request = repo.get_pull(int(pull_number))

# First check if the PR has the "bypass" label. This label is used for PRs that don't need to update
# RELEASE_NOTES. If so, we can exit immediately.
labels = [l.name for l in pull_request.labels]
if bypass_label_name in labels:
    print(f"PR number {pull_number} in repo {REPO_NAME} contains the '{bypass_label_name}' label. Exiting with success.")
    sys.exit(0)

# Next, check if the release notes file (RELEASE_NOTES.md or similar) has been modified.
files = pull_request.get_files()
for file in files:
    if file.filename == release_notes_file:
        print(f"PR number {pull_number} in repo {REPO_NAME} modifies '{release_notes_file}'. Exiting with success.")
        sys.exit(0)

# At this point, we issue a warning to the PR author to remember to modify the release notes, and
# exit with failure.
pull_request.create_issue_comment(f"Please remember to add a release note line to {release_notes_file}. If this PR does not warrant a release note, add the {bypass_label_name} label.")
sys.exit(1)

print('Done!')
