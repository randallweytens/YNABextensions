from dotenv.main import dotenv_values
import requests
import os
import json
from dotenv import load_dotenv

#ynab api endpoints
#https://api.youneedabudget.com/v1

#imports variables from .env into the environment
#load_dotenv(dotenv_path="conf/.env",verbose=True)

#print(os.environ)

#token = os.environ.get("YNAB_TOKEN")

#load the .env file into a config dict
config = dotenv_values(dotenv_path="conf/.env",verbose=True)

token = config["YNAB_TOKEN"]

#print(config["YNAB_TOKEN"])

#print(token)

#build the request header
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
