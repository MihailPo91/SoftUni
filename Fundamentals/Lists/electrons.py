num_el = int(input())
new_list = []
i = 0

while 0 < num_el:

    i += 1
    shell = 2 * i ** 2

    if num_el >= shell:
        new_list.append(shell)
        num_el -= shell
    else:
        new_list.append(num_el)
        num_el = 0

print(new_list)

















