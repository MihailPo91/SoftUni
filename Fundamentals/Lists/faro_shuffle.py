card_string = input().split(" ")
shuffles = int(input())


for n in range(shuffles):
    a = card_string[:len(card_string) // 2]
    b = card_string[len(card_string) // 2:]
