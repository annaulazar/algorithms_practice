from time import time


d = {'key': 1}
start = time()
for i in range(20000000):
    a = d['key']
print(time() - start)

start1 = time()
for i in range(20000000):
    a = d.get('key')
print(time() - start1)
