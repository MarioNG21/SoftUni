class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        return f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}"


emails = []
data = input()
while data != "Stop":
    sender, receiver, content = data.split()
    email = Email(sender, receiver, content)
    emails.append(email)
    data = input()


index = [int(el) for el in input().split(", ")]

for indexes in index:
    emails[indexes].send()

for email in emails:
    print(email.get_info())