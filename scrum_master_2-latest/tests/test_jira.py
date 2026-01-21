import os
from jira import JIRA

def test_jira_authentication():
    JIRA_URL = os.getenv("JIRA_BASE_URL")
    JIRA_EMAIL = os.getenv("JIRA_EMAIL")
    JIRA_API_TOKEN = os.getenv("JIRA_API_TOKEN")

    assert JIRA_URL, "JIRA_BASE_URL is missing"
    assert JIRA_EMAIL, "JIRA_EMAIL is missing"
    assert JIRA_API_TOKEN, "JIRA_API_TOKEN is missing"

    jira = JIRA(
        server=JIRA_URL,
        basic_auth=(JIRA_EMAIL, JIRA_API_TOKEN)
    )

    user = jira.current_user()
    projects = jira.projects()

    print("✅ Jira authentication SUCCESS")
    print("User:", user)
    print("Projects found:", len(projects))

    assert user is not None
    assert len(projects) >= 0

