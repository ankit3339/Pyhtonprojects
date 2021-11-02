import time

while True:
    secs = input("Enter the time\t")
    stop = abs(int(secs))
    while stop > 0:
        m, s = divmod(stop, 60)
        h, m = divmod(m, 60)
        left = str(h).zfill(2) + ":" + str(m).zfill(2) + ":" + str(s).zfill(2)
        print(left + "\n", end="")
        time.sleep(1)
        stop -= 1


# def countTime(t):
#     while t > 0:
#         print(t)
#         t = t - 1
#         time.sleep(1)
#     print("times up")
#
#
# secs = int(input("Enter the seconds you want to add"))
# countTime(secs)
