import requests
import os
import json
from decouple import config

#ynab api endpoints
#https://api.youneedabudget.com/v1

#print(os.environ)

#token = os.environ['ynab_token']

#os.environ

token = config('ynab_token')

print(token)

headers = {'Authorization': 'Bearer ' + token}

my_response = requests.get('https://api.youneedabudget.com/v1/budgets',headers=headers)

budgets = my_response.json()

#print(my_response.json())

#print(json.dumps(my_response.json(),indent=4, sort_keys=True, separators=(',', ':')))
#print(json.dumps(my_response.json(),indent=4))


print("\nPrint each budget key-value pair from JSON response\n")
for key, value in budgets.items():
    print(key, ":", value)

print("\nLoop through budgets\n")

for budget in budgets["data"]["budgets"]:
    print(budget["id"])
    budget_id = budget["id"]

#print(budgets["data"]["budgets"]{"id"})

my_response = requests.get(f"https://api.youneedabudget.com/v1/budgets/{budget_id}/accounts",headers=headers)

accounts = my_response.json()

print("\nPrint each account key-value pair from JSON response\n")
for key, value in accounts.items():
    print(key, ":", value)

for account in accounts["data"]["accounts"]:
    print(account["id"] + " " + account["name"])
