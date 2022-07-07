# 1_Implement class iterator for Fibonacci numbers. Iterator get numbers of first Fibonacci numbers
# 1, 1, 2, 3, 5, 8, 13, 21, 34, 55, 89, 144

class Fibonacci:
    def __init__(self, how_number):
        self.how_number = how_number
        self.cur_num = 0
        self.next_num = 1

    def __iter__(self):
        return self

    def __next__(self):
        if self.how_number == 0:
            raise StopIteration
        self.how_number -= 1

        next_num = self.cur_num + self.next_num
        self.cur_num = self.next_num
        self.next_num = next_num

        return self.cur_num


num_12 = Fibonacci(12)

for num in num_12:
    print(num)


# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21
# 34
# 55
# 89
# 144

# 2_Implement generator for Fibonacci numbers

def fib(num_1):
    a = 1
    b = 1
    for c in range(num_1):
        yield a
        a, b = b, a + b


for x in fib(8):
    print(x)


# 1
# 1
# 2
# 3
# 5
# 8
# 13
# 21

#  3_Write generator expression that returns square numbers of integers from 0 to 10

def square(lenght):
    for a in range(lenght):
        yield a ** 2


for x in square(11):
    print(x)


# 0
# 1
# 4
# 9
# 16
# 25
# 36
# 49
# 64
# 81
# 100

# 4_Implement coroutine for accumulation arithmetic mean

def accumulation_mean():
    total = 0
    quantity = 0
    while True:
        a = yield
        quantity += 1
        total += a
        print(total / quantity)


ac_mean_1 = accumulation_mean()
ac_mean_1.__next__()
ac_mean_1.send(18)  # 18.0
ac_mean_1.send(12)  # 15.0
ac_mean_1.send(100)  # 43.333333333333336
