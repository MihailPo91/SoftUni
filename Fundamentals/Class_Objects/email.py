class Email:

    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        string = f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"
        return string


emails = []

while True:
    line = input()

    if line == "Stop":
        break

    else:
        explode = line.split(" ")
        sender = explode[0]
        receiver = explode[1]
        content = explode[2]
        email = Email(sender, receiver, content)
        emails.append(email)

send_emails = [emails[int(x)].send() for x in input().split(", ")]

for email in emails:
    print(email.get_info())
