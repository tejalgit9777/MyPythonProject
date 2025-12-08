# Real API Testing Example
import  requests

try:
    url = str(input("Enter URL: "))
    response = requests.get(url, timeout=3)
    print(response.status_code)
    print(response.text)
    print(response.status_code)
except requests.exceptions.Timeout:
    print("Timeout error, not able to load the URL.")
except requests.exceptions.RequestException:
    print("Error due to the wrong URL or connection failed!")
except Exception as e: # alias e
    print(e)

