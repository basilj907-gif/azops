import os
import requests
from azure.identity import DefaultAzureCredential
 
SUBSCRIPTION_ID = "####################"
API_VERSION = "2023-03-01"
 
def get_access_token():
    credential = DefaultAzureCredential()
    token = credential.get_token("https://management.azure.com/.default")
    return token.token
 
def fetch_vm_cost():
    url = (
        f"https://management.azure.com/subscriptions/{SUBSCRIPTION_ID}"
        f"/providers/Microsoft.CostManagement/query?api-version={API_VERSION}"
    )
 
    payload = {
        "type": "ActualCost",
        "timeframe": "MonthToDate",
        "dataset": {
            "granularity": "Daily",
            "aggregation": {
                "totalCost": {
                    "name": "PreTaxCost",
                    "function": "Sum"
                }
            },
            "grouping": [
                {"type": "Dimension", "name": "ResourceName"},
                {"type": "Dimension", "name": "ResourceType"}
            ],
            "filter": {
                "dimensions": {
                    "name": "ResourceType",
                    "operator": "In",
                    "values": ["Microsoft.Compute/virtualMachines"]
                }
            }
        }
    }
 
    headers = {
        "Authorization": f"Bearer {get_access_token()}",
        "Content-Type": "application/json"
    }
 
    response = requests.post(url, headers=headers, json=payload, timeout=30)
    response.raise_for_status()
 
    data = response.json()
 
    # 🔹 PRINT RAW RESPONSE
    print("\n===== RAW COST API RESPONSE =====")
    print(data)
 
    return data