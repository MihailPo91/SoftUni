num_1 = input().split(" ")
num_2 = input().split(" ")
num_3 = input().split(" ")
one_is_winning = False
two_is_winning = False
is_draw = False

map(int, num_1, num_2, num_3)

a, b, c = list(num_1), list(num_2), list(num_3)

if a[0] == "1" and a[1] == "1" and a[2] == "1":
    one_is_winning = True
elif a[0] == "1" and b[1] == "1" and c[2] == "1":
    one_is_winning = True
elif a[0] == "1" and b[0] == "1" and c[0] == "1":
    one_is_winning = True
elif b[0] == "1" and b[1] == "1" and b[2] == "1":
    one_is_winning = True
elif a[1] == "1" and b[1] == "1" and c[1] == "1":
    one_is_winning = True
elif c[0] == "1" and c[1] == "1" and c[2] == "1":
    one_is_winning = True
elif a[2] == "1" and b[2] == "1" and c[2] == "1":
    one_is_winning = True
elif c[0] == "1" and b[1] == "1" and a[2] == "1":
    one_is_winning = True
elif a[0] == "2" and a[1] == "2" and a[2] == "2":
    two_is_winning = True
elif a[0] == "2" and b[1] == "2" and c[2] == "2":
    two_is_winning = True
elif a[0] == "2" and b[0] == "2" and c[0] == "2":
    two_is_winning = True
elif b[0] == "2" and b[1] == "2" and b[2] == "2":
    two_is_winning = True
elif a[1] == "2" and b[1] == "2" and c[1] == "2":
    two_is_winning = True
elif c[0] == "2" and c[1] == "2" and c[2] == "2":
    two_is_winning = True
elif a[2] == "2" and b[2] == "2" and c[2] == "2":
    two_is_winning = True
elif c[0] == "2" and b[1] == "2" and a[2] == "2":
    two_is_winning = True
else:
    is_draw = True

if one_is_winning:
    print("First player won")
if two_is_winning:
    print("Second player won")
if is_draw:
    print("Draw!")










