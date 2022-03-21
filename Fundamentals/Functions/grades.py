def grade_evaluate(grade):

    if grade < 3:
        return "Fail"
    elif 3 <= grade < 3.5:
        return "Poor"
    elif 3.5 <= grade < 4.5:
        return "Good"
    elif 4.5 <= grade < 5.5:
        return "Very Good"
    else:
        return "Excellent"


print(grade_evaluate(float(input())))


