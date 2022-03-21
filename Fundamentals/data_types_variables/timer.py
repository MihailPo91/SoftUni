import time
import winsound

user_start = int(input())
counter = user_start
tic = time.perf_counter()

while True:
    toc = time.perf_counter()
    if toc - tic > 1:
        counter -= 1
        print(counter)
        if counter <= 0:
            print("Bang!")
            winsound.Beep(500, 2000)
            break
        tic = toc
