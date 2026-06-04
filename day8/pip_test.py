import requests

# Fetch a public API — random useless fact
url = "https://api.api-ninjas.com/v1/quotes"
print("Fetching from a public test endpoint...")

# Use a simpler public API that needs no key
response = requests.get("https://api.github.com")

print(f"Status code: {response.status_code}")        # 200 means success
print(f"Headers content-type: {response.headers['content-type']}")
print(f"Response (first 200 chars): {response.text[:200]}")