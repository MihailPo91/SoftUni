def greet(first_name, last_name):
    return f"""
    Hello, {first_name} {last_name}!
    This is a test email, made with the sole purpose of training.
    Kind regards, Blabla!
"""


email = greet("Mihail", "Polimenov")

print(email)

