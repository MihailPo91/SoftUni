user_input = input().split('\\')

for word in user_input:
    if "." in word:
        word = word.split(".")
        file, extension = word[0], word[1]

        print(f"File name: {file}")
        print(f"File extension: {extension}")