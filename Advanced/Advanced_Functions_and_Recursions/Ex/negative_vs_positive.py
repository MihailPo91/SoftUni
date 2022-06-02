nums = [int(x) for x in input().split()]

positives = [0,]
negatives = [0,]

for n in nums:
    if n > 0:
        positives.append(n)
    else:
        negatives.append(n)

print(sum(negatives))
print(sum(positives))

if abs(sum(positives)) > abs(sum(negatives)):
    print('The positives are stronger than the negatives')
else:
    print('The negatives are stronger than the positives')

