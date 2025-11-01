# Write a Function to Check Test Case Status
from unittest import case

# Problem:
# Write a function check_status(status_code) that returns:
# "PASS" if status_code = 200
# "FAIL" if status_code = 400 or 500
# "UNKNOWN" otherwise
# Example Input & Output:
# print(check_status(200))   # PASS
# print(check_status(500))   # FAIL
# print(check_status(302))   # UNKNOWN

status_code = int(input("Enter Status code: ").strip())

def check_status(code):
    if status_code<=0 or status_code >1000:
        print("please check your code")
        return None
    else:
        match status_code:
            case 200:
                return  "Pass"
            case 300 | 400 | 500:
                return "Fail"
            case _:
                return "Unknown"


print(check_status(status_code))

