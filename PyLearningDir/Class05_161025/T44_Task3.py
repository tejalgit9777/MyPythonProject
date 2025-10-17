# Performance testing speed check


res_time = float(input("Response Time: ").strip())

if res_time >= 0 and res_time < 3:
    print("Performance speed is faster!")
else:
    print("⚠️ Page load too slow!")
