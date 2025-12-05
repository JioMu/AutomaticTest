import math
import random


class WayFloor:
    @staticmethod
    def ways(n):
        if n < 0:
            print("楼层要大于0")
        if n == 1 or n == 2 or n == 3:
            return n
        else:
            a, b, c = 1, 2, 3
            for _ in range(4, n + 1):
                a, b, c = b, c, b + c
            return c


if __name__ == '__main__':
    # n = math.ceil(random.random()*100)
    n = int(12)
    WayFloor = WayFloor()
    print(f"到{n}楼层的方法有：", WayFloor.ways(n), "种")
