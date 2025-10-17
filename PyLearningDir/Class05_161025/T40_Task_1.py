#You receive an API response code from your test script.
#Write an if-else block to check whether the response is successful (status code 200) or not.

status = int(input("Enter status: ").strip())

if status != 200 and status != 400 and status != 500:
    print("Invalid status!")
elif status == 200:
    print("✅ Passed API Request")
elif status == 400:
    print("❌ Failed API Request")
elif status == 500:
    print("❌ Internal Server Error")

    






