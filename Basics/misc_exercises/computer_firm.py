number_of_models = int(input())
sales_made = 0
rating_total = 0

for model in range(1, number_of_models + 1):
    rating_per_model = int(input())

    rating = rating_per_model % 10
    rating_total += rating
    rating_text = str(rating_per_model)
    possible_sales_text = (rating_text[0] + rating_text[1])
    possible_sales = int(possible_sales_text)

    if rating == 2:
        sales_made += 0

    elif rating == 3:
        sales_made += possible_sales / 2

    elif rating == 4:
        sales_made += possible_sales * 0.70

    elif rating == 5:
        sales_made += possible_sales * 0.85

    elif rating == 6:
        sales_made += possible_sales


print(f"{sales_made:.2f}")
print(f"{rating_total / number_of_models:.2f}")