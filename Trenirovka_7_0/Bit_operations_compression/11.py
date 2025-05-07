import time


a = '1' + '0' * 450 + '1' * 5 + '0' * 549
b = '1' * 10 + '0' * 200 + '1' * 50 + '0' * 740
a1 = int(a, 2)
b1 = int(b, 2)

c = [0] * 1000

start = time.time()
for _ in range(10000):
    d = a1 & b1
print(time.time() - start)

start = time.time()
for _ in range(10000):
    for i in range(1000):
        if c[i] == 1:
            break

print(time.time() - start)
