import requests

url = "http://localhost:3476/v1/tenants/{tenant_id}/schemas/write"
headers = {"Content-Type": "application/json"}
data = {
    "schema": "entity user {}\n\n    entity organization {\n\n        relation admin @user\n        relation member @user\n\n        action create_repository = (admin or member)\n        action delete = admin\n    }\n\n    entity repository {\n\n        relation owner @user\n        relation parent @organization\n\n        action push = owner\n        action read = (owner and (parent.admin and parent.member))\n        action delete = (parent.member and (parent.admin or owner))\n }"
}

response = requests.post(url, headers=headers, json=data)
print(response.text)