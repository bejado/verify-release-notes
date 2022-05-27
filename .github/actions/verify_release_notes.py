from github import Github

authentication_token = os.environ.get('GITHUB_API_KEY')
if not authentication_token:
    sys.stderr.write('Error: the GITHUB_API_KEY is not set.\n')
    sys.exit(1)

g = Github(authentication_token)

FILAMENT_REPO = "bejado/filament"
filament = g.get_repo(FILAMENT_REPO)

pull_request = filament.get_pull(4)
pull_request.create_issue_comment('Hi, I\'m Filament bot!')

print('Done!')
