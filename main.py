from multiprocessing import Pool
import random

# 初始化全局变量
sample_count = 100000
day_limit = 36500
stats = [0, 0]  # 死,活
process = 40


def simulate():
    day = 1
    alien_count = 1

    while day <= day_limit:
        r = random.randint(0, 3)
        if r == 1:
            alien_count += 1
        elif r == 2:
            alien_count += 2
        elif r == 3:
            alien_count -= 1
        if alien_count == 0:
            break
        day += 1

    if alien_count == 0:
        return True
    else:
        return False


def main():
    with Pool(processes=process) as pool:
        for _ in range(sample_count):
            res = pool.apply_async(simulate)
            print('Result from worker: ', res.get())
            if res.get():
                stats[0] += 1
            else:
                stats[1] += 1


if __name__ == "__main__":
    main()
    print("process count:", process)
    print("sample count:", sample_count)
    print("Result:", stats[0], "samples alive, ", stats[1], "samples dead, probability: ", stats[0] / sample_count)
