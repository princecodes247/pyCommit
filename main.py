import base64
from github import Github
from pprint import pprint

# Github username and password
username = "username"
password = "password"

# authenticate to github
g = Github(username, password)
# get the authenticated user
user = g.get_user()
for repo in user.get_repos():
    print_repo(repo)