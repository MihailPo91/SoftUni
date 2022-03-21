def loading_bar(num):

    if num == 100:
        print("100% Complete!")
        print("[%%%%%%%%%%]")
    else:
        loading_status = f"[{((num//10) * '%')}{((10 - (num//10)) * '.')}]"
        print(f"{num}% {loading_status}")
        print("Still loading...")


num = int(input())
loading_bar(num)