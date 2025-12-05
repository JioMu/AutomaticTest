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
            return WayFloor.ways(n - 1) + WayFloor.ways(n - 2)


if __name__ == '__main__':
    # n = math.ceil(random.random()*100)
    n = int(10000)
    WayFloor = WayFloor()
    print("到n楼层的方法有：", WayFloor.ways(n), "种")
