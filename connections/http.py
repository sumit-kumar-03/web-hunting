import requests
import sys


def send_http_get(domain):
    url = f"http://{domain}"
    headers = {
        "User-Agent": "Mozilla/5.0 (Linux; Web-Hunting Script)",
        "Accept": "*/*",
        "Connection": "close",
    }
    try:
        response = requests.get(
            url,
            headers=headers,
            timeout=5,
        )
        print(f"Request URL: {response.url}")
        print(f"Status Code: {response.status_code}")
        print("Response Headers:")
        for k, v in response.headers.items():
            print(f"  {k}: {v}")
        print("\nResponse Body:")
        print(response.text)
    except Exception as e:
        print(f"Error sending HTTP GET request: {e}")
