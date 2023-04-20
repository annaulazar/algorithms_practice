import random

def slow_f(lst):
    pass

def fast_f(lst):
    pass


while True:
    rand_list = [random.randint(1, 120) for _ in range(5)]
    right_res = slow_f(rand_list)
    wrong_res = fast_f(rand_list)
    if right_res != wrong_res:
        print(rand_list)
        print(right_res, wrong_res)
        break
