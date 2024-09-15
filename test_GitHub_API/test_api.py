import os
from dotenv import load_dotenv
import requests

load_dotenv()

GITHUB_USERNAME = os.getenv("GITHUB_USERNAME")
GITHUB_TOKEN = os.getenv("GITHUB_TOKEN")
REPO_NAME = os.getenv("REPO_NAME")


def create_new_repo():
    requests.post(
        "https://api.github.com/user/repos",
        headers={"Authorization": f"token {GITHUB_TOKEN}", },
        json={"name": REPO_NAME, }
    )
    print(f"Репозиторий '{REPO_NAME}' успешно создан.")

    list_repos = requests.get(
        f"https://api.github.com/users/{GITHUB_USERNAME}/repos",
        headers={
            "Authorization": f"token {GITHUB_TOKEN}"
        }
    )
    assert any(repo["name"] == REPO_NAME for repo in list_repos.json())
    print(f"Репозиторий '{REPO_NAME}' найден.")

    requests.delete(
        f"https://api.github.com/repos/{GITHUB_USERNAME}/{REPO_NAME}",
        headers={"Authorization": f"token {GITHUB_TOKEN}"}
    )
    print(f"Репозиторий '{REPO_NAME}' успешно удален.")


if __name__ == "__main__":
    create_new_repo()
