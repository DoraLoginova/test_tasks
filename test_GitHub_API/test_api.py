import os
from dotenv import load_dotenv
import requests

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")


def new_repo():
    requests.post(
        "https://api.github.com/user/repos",
        headers={"Authorization": f"token {GITHUB_TOKEN}", },
        json={"name": REPO_NAME, }
    )
    print(f"Репозиторий '{REPO_NAME}' создан.")

    list_repos = requests.get(
        f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}"
        }
    )
    for repo in list_repos.json():
        if repo["name"] == REPO_NAME:
            print(f"Репозиторий '{REPO_NAME}' найден.")
        else:
            print(f"Репозитория '{REPO_NAME}' не существует.")

    requests.delete(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"}
    )
    print(f"Репозиторий '{REPO_NAME}' удален.")


if __name__ == "__main__":
    new_repo()
