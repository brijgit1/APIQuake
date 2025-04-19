import json
from api_tester import run_api_test

def load_apis():
    with open("api_config.json", "r") as f:
        config = json.load(f)
    return config["apis"]

def run_all_tests():
    apis = load_apis()
    results = [run_api_test(api) for api in apis]
    return results
