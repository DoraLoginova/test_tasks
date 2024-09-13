import os
from dotenv import load_dotenv
import requests

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")


def test_github_api():
    # Создание нового репозитория
    create_repo_response = requests.post(
        f"https://api.github.com/user/repos",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}",
            "Content-Type": "application/json"
        },
        json={
            "name": REPO_NAME,
            "private": False
        }
    )

if __name__ == "__main__":
    test_github_api()
