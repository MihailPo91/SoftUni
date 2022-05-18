from collections import deque

q = deque()

customer = input()

while customer != "End":

    if customer == "Paid":
        while q:
            print(q.popleft())

    else:
        q.append(customer)

    customer = input()

print(f"{len(q)} people remaining.")
