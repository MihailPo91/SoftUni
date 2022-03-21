tickets = input().split(", ")

for ticket in tickets:
    ticket_list = list(ticket)
    is_valid = False
    is_winning = False
    jackpot = False
    if len(ticket) == 20:
        is_valid = True
    if is_valid:
        first_half = ticket[:10]
        second_half = ticket[10:]
        if "@@@@@@" in first_half and "@@@@@@" in second_half or "######" in first_half and "######" in second_half \
                or "$$$$$$" in first_half and "$$$$$$" in second_half \
                or "^^^^^^" in first_half and "^^^^^^" in second_half:
            is_winning = True
        if "$$$$$$$$$$$$$$$$$$$$" == ticket or "####################" == ticket or "@@@@@@@@@@@@@@@@@@@@" == ticket\
                or "^^^^^^^^^^^^^^^^^^^^" == ticket:
            jackpot = True

        if jackpot:
            print(f'ticket "{ticket}" - 10$ Jackpot!')
        elif not jackpot and is_winning:
            print(f'ticket "{ticket}" - 6$')
        else:
            print(f'ticket "{ticket}" - no match')
    else:
        print("invalid ticket")

