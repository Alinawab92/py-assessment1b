class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []

    def add_reply(self, reply_text, user):
        if len(self.replies) == 0:  # Only allow one reply
            reply = Comment(reply_text, user)
            self.replies.append(reply)
        else:
            print("A comment cannot have more than one reply.")
