cards = input().split()
shuffle = int(input())

length = len(cards)
mid = int(length / 2)

for i in range(0, shuffle):
    list_cards = []
    for p in range(0, mid):
        list_cards.append(cards[p])
        list_cards.append(cards[mid])
        mid += 1
    cards = list_cards
    mid = int(length / 2)

print(list_cards)
