
#   
# GitHub Issue Creator

This Python script allows you to create GitHub issues programmatically using the GitHub API. It utilizes the `requests` library to send HTTP requests to the GitHub API.

## Prerequisites

Before using this script, make sure you have the following installed:

-   Python (version 3.x)
-   `requests` library

Install the `requests` library using the following command:

`pip install requests` 

## Usage

Run the script with the following command:

`python create_github_issue.py [repo_owner] [repo_name] [title] [body] [token]` 

Replace the placeholders with the appropriate values:

-   `repo_owner`: The owner of the GitHub repository.
-   `repo_name`: The name of the GitHub repository.
-   `title`: The title of the GitHub issue.
-   `body`: The description or body of the GitHub issue.
-   `token`: Your personal access token with the necessary permissions to create issues in the repository.

Optional parameters:

-   `assignees`: A list of GitHub usernames to assign to the issue.
-   `labels`: A list of labels to add to the issue.

Example:

`python create_github_issue.py alifertah yougym "Test Issue" "This is a test issue created using the script." <your_personal_access_token>` 

## Note

Ensure that your personal access token has the required permissions to create issues in the specified repository. You can generate a personal access token in your GitHub account settings.

**Disclaimer:** Be cautious while handling personal access tokens, and avoid sharing them publicly.

Feel free to customize the script according to your needs or integrate it into your workflow.