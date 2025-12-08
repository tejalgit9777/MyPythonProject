try:
    data = open("t.txt").read()
except FileNotFoundError as fnf:
    print(fnf)