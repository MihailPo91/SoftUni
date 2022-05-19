from collections import deque

bullet_price = int(input())
barrel_size = int(input())

bullets = deque([int(x) for x in input().split()])
locks = deque([int(x) for x in input().split()])

intelligence = int(input())
bullets_used = 0

while bullets:

    if locks:

        current_bullet = bullets.pop()
        bullets_used += 1

        current_lock = locks[0]
        if current_bullet <= current_lock:
            locks.popleft()
            print('Bang!')
        else:
            print('Ping!')

    else:
        break

    if bullets_used % barrel_size == 0 and bullets_used > 0 and bullets:
        print('Reloading!')

if bullets:
    print(f'{len(bullets)} bullets left. Earned ${intelligence - bullets_used * bullet_price}')
else:
    if not locks:
        print(f'0 bullets left. Earned ${intelligence - bullets_used * bullet_price}')
    else:
        print(f"Couldn't get through. Locks left: {len(locks)}")
