# test-jira-ansible-remediation-bot
Personal testing ground for automating specific tasks in Jira SM using Ansible


What's the purpose?


For when you run certain routine tasks (server patching, users leaving), this will detect the ticket status so it triggers and performs the actions, creates an auditing trail (comments) and changes the status of the tickets if it succeeds or fails. 

Pulls ticket data without requiring open inbound firewall ports using the JIRA API.
Automates the "Done/Failed" transition logic based on system thresholds (currently set to Fail on purpose for changing status tests).


The Stack I used for this so far


Language: Python 3.12+ (Virtual Env)

Automation: Ansible-Core

API: Jira Service Management (REST API v3 / ServiceDesk API)

Scheduler: System Cron



Logic Flow used


Fetch: Queries /rest/servicedeskapi/request for tickets where status == "Work in progress".

Inspect: Runs ps aux and docker ps via Ansible shell modules.

Analyze: Parses CPU output.

Respond: * If CPU meets the criteria: Posts logs and transitions ticket to Done.

When CPU fails criteria (again, on purpose): Posts failure reason and transitions ticket to Failed.


Standard JQL search (/rest/api/3/search) was returning 410 Gone for Service Management fields, so I had to use the logic to use the Service Desk-specific endpoint which handles "Request Type" IDs more reliably.
