import requests
from requests.auth import HTTPBasicAuth


def create_jira_ticket(summary, description):
    #Define Jira SM tenant and info
    DOMAIN = "DOMAIN_URL"
    EMAIL: "username@domain.com"
    API_TOKEN: "API_TOKEN"
    SERVICE_DESK_ID = "1"
    REQUEST_TYPE_ID = "1"

    url = f"https://{DOMAIN}/rest/servicedeskapi/request"
    auth = HTTPBasicAuth(EMAIL, API_TOKEN)
    headers = {"Accept": "application/json", "Content-Type": "application/json"}

    payload = {
        "serviceDeskId": SERVICE_DESK_ID,
        "requestTypeId": REQUEST_TYPE_ID,
        "requestFieldValues": {
            "summary": summary,
            "description": description
        }
    }

    response = requests.post(url, json=payload, auth=auth, headers=headers)
    
    if response.status_code == 201:
        print(f"✅ Success! Ticket created: {response.json()['issueKey']}")
    else:
        print(f"❌ Failed: {response.status_code} - {response.text}")

# Example trigger
create_jira_ticket("ALERT: Web Server Down", "The Ansible-managed web server is not responding to pings.")


