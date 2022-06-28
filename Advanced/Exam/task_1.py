from collections import deque

eggs = deque([int(x) for x in input().split(', ')])
papers = deque([int(x) for x in input().split(', ')])

boxes = 0

while eggs and papers:
    egg = eggs.popleft()
    paper = papers.pop()

    if egg <= 0:
        papers.append(paper)
        continue

    if egg == 13:
        switch_paper = papers.popleft()
        papers.appendleft(paper)
        papers.append(switch_paper)
        continue

    current_sum = egg + paper
    if current_sum <= 50:
        boxes += 1


if boxes > 0:
    print(f"Great! You filled {boxes} boxes.")
else:
    print("Sorry! You couldn't fill any boxes!")

if eggs:
    print(f'Eggs left: {", ".join([str(x) for x in eggs])}')
if papers:
    print(f'Pieces of paper left: {", ".join([str(x) for x in papers])}')
