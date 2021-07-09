from github import Github
from datetime import datetime
from time import sleep
import os

# Github access token
access_token = os.getenv('GITHUB_TOKEN')

# authenticate to github
g = Github(access_token)
# get the authenticated user
user = g.get_user()

def commit_it(target): 
    repo = g.get_repo(target)
    branch = repo.get_branch("main")
    ref = branch.commit.sha
    # Current date time in local system
    commit = datetime.now()
    contents = repo.get_contents("commit.txt", ref=ref)
    repo.update_file(contents.path, f"{commit}", f"{commit}", contents.sha, branch="main")
    print("Made Commit")
while True:
    commit_it("princecodes247/pyCommited")
    sleep(10)
