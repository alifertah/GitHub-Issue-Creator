import requests
from requests.auth import HTTPBasicAuth
import sys

def create_github_issue(repo_owner, repo_name, title, body, token, assignees=[], labels=[]):
    url = f'https://api.github.com/repos/{repo_owner}/{repo_name}/issues'
    headers = {"Authorization": token,}

    data = {
        'title': title,
        'body': body,
        'assignees': assignees,
        'labels': labels
    }

    response = requests.post(url, 
        auth=HTTPBasicAuth(repo_owner, token)
        ,json=data, headers=headers)

    if response.status_code == 201:
        print(f"Issue created successfully. Issue URL: {response.json()['html_url']}")
    else:
        print(f"Failed to create issue. Status Code: {response.status_code}\nResponse: {response.text}")
        print(url)

repo_owner = sys.argv[1]
repo_name = sys.argv[2]
title = sys.argv[3]
body = sys.argv[4]
token = sys.argv[5]
assignees = ["alifertah"]
labels = ["fix", "hot"]

create_github_issue(repo_owner, repo_name, title, body, token, assignees, labels)