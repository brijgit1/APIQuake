import requests

def run_api_test(api):
    method = api.get("method", "GET").upper()
    url = api["url"]
    headers = api.get("headers", {})
    params = api.get("params", {})
    payload = api.get("payload", {})
    expected_status = api.get("expected_status")
    expected_keys = api.get("expected_keys", [])

    try:
        if method == "GET":
            response = requests.get(url, headers=headers, params=params)
        elif method == "POST":
            response = requests.post(url, headers=headers, json=payload)
        else:
            return {"name": api["name"], "status": "Unsupported method", "code": 405}

        resp_content = response.json() if "application/json" in response.headers.get("Content-Type", "") else {}

        # Validate status code
        status_pass = response.status_code == expected_status

        # Validate response keys if it's a dict or a list of dicts
        key_pass = False
        if isinstance(resp_content, dict):
            key_pass = all(key in resp_content for key in expected_keys)
        elif isinstance(resp_content, list) and resp_content:
            key_pass = all(key in resp_content[0] for key in expected_keys)

        return {
            "name": api["name"],
            "url": url,
            "status_code": response.status_code,
            "response": resp_content,
            "status_check": status_pass,
            "key_check": key_pass,
            "test_passed": status_pass and key_pass
        }

    except Exception as e:
        return {
            "name": api["name"],
            "url": url,
            "status_code": "Error",
            "response": str(e),
            "status_check": False,
            "key_check": False,
            "test_passed": False
        }
