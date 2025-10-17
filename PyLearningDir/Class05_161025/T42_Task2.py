# In automation, you often compare expected and actual outputs.
# Write code to check if a test case passed or failed.

match = "Dashboard"
test_result = str(input("Enter test case result: ").strip())
if test_result == match:
    print("Passed")
elif test_result == match.lower() or test_result == match.upper():
    print("Passed")
# elif test_result == match.upper():
#     print("Passed")
else:
    print("Failed")