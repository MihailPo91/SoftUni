class Comment:
    def __init__(self, username, content, likes=0):
        self.username = username
        self.content = content
        self.likes = likes

    def hello_there(self, favourite_book):
        return f"Hello there, {self.username}, you have {self.likes} likes. Your favourite book is {favourite_book}"


comment = Comment("user1", "I like this book", 50)
print(comment.username)
print(comment.content)
print(comment.likes)

print(comment.hello_there("Harry Potter."))
