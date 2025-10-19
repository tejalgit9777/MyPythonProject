# Simulate a page loading check using a while loop.
# If page_loaded becomes True within 5 seconds, print success; else timeout.
#
# Hint: Use a counter (like wait_time) and break condition.

page_load = False
wait_time=0
while wait_time < 5:
    time = int(input("Response Code: "))
    if time <= 5:
        page_load = True
        print("Success")
        break
    else:
        print("Time Out")
    wait_time += 1

if page_load == True:
    print("Page Loaded")
else:
    print("Time Out")