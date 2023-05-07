import requests
import os
from datetime import datetime
from dateutil.relativedelta import relativedelta
import openai


def get_headers(key):
    headers = {'Authorization': f'Bearer {key}'}
    return headers

def get_subscription(key):
    queryUrl = 'https://api.openai.com/dashboard/billing/subscription'
    headers = get_headers(key)
    r = requests.get(queryUrl, headers=headers)
    results = r.json()
    if check_key_availability():
        has_payment_method = results["has_payment_method"]
        # hard_limit = results["hard_limit"]
        hard_limit_usd = results["hard_limit_usd"]
        plan = results["plan"]["title"]
        account_name = results["account_name"]
        return {"account_name": account_name,
                "has_payment_method": has_payment_method,
                "hard_limit_usd": hard_limit_usd,
                "plan": plan}
    else:
        return {"account_name": "",
                "has_payment_method": False,
                "hard_limit_usd": "",
                "plan": ""}

def get_usage(key):
    if check_key_availability():
        start_date = datetime.now().strftime('%Y-%m-01')
        end_date = (datetime.now() + relativedelta(months=1)).strftime('%Y-%m-01')
        queryUrl = f'https://api.openai.com/dashboard/billing/usage?start_date={start_date}&end_date={end_date}'
        headers = get_headers(key)
        r = requests.get(queryUrl, headers=headers)
        return r.json()['total_usage']/100.0
    else:
        return ""

def check_gpt4_availability():
    if check_key_availability():
        available_models = [model["root"] for model in openai.Model.list()["data"]]
        if 'gpt-4' in available_models:
            return True
        else:
            return False
    else:
        return False

def check_key_availability():
    try:
        openai.Model.list()
        return True
    except:
        return False

if __name__ == "__main__":
    key = os.getenv("OPENAI_API_KEY")
    results = get_usage(key)
    print(results)

    results = get_subscription(key)
    for k, v in results.items():
        print(f"{k}: {v}")