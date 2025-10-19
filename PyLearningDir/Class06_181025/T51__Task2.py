# An API sometimes fails due to network delays.
#
# Write a program to retry the API call 3 times until the response code becomes 200.
#
# If it still fails after 3 tries, print a failure message.
#
# Hint: Use a while loop with a counter.
#
# Expected Output Example:
# Attempt 1: Response 500
# Attempt 2: Response 200
# ✅ Test Passed


call = 0
while call < 3:
    number = int(input("Enter a number: "))
    if number == 200:
        print("200 Ok")
        break
    elif number != 200:
        print("Invalid call")
    call += 1
if call==3:
    print("Too many time calls")



