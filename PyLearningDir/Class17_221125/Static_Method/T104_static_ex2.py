
class Counter:

    count = 0

    def __init__(self):
        Counter.count += 1

t1= Counter()
t2 = Counter()
t3 = Counter()
print("Counter: ",Counter.count)


