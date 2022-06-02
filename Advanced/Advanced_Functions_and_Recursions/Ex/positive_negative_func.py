def find_positive_and_negative_sums(*args):
    positive_sum = 0
    negative_sum = 0

    for n in args:
        if n > 0:
            positive_sum += n
        else:
            negative_sum += n

    if abs(positive_sum) > abs(negative_sum):
        return positive_sum, negative_sum, 'The positives are stronger than the negatives'
    else:
        return positive_sum, negative_sum, 'The negatives are stronger than the positives'


nums = [int(x) for x in input().split()]

positive_sum, negative_sum, statement = find_positive_and_negative_sums(*nums)

print(negative_sum, positive_sum, statement, sep='\n')
