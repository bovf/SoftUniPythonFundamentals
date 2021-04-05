class Email:
    def __init__(self, sender, receiver, content):
        self.sender = sender
        self.receiver = receiver
        self.content = content
        self.is_sent = False

    def send(self):
        self.is_sent = True

    def get_info(self):
        print(f"{self.sender} says to {self.receiver}: {self.content}. Sent: {self.is_sent}")


emails = []

while True:
    command = input()

    if command == "Stop":
        break

    email_info = command.split(" ")
    email_sender = email_info[0]
    email_receiver = email_info[1]
    email_content = email_info[2]

    email = Email(email_sender, email_receiver, email_content)
    emails.append(email)

send_index = [int(num) for num in (input().split(", "))]

for index in send_index:
    emails[index].send()

for email in emails:
    email.get_info()
