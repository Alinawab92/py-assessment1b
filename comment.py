from reply import Reply


class Comment:
    def __init__(self, text, author):
        self.text = text
        self.author = author
        self.replies = []  # A comment has many replies

    def add_reply(self, reply_text, user):
        reply = Reply(reply_text, user)
        self.replies.append(reply)

    def display_comment(self):
        return f"{self.author.name}: {self.text}"

    def display_replies(self):
        for reply in self.replies:
            print(reply.display_reply())
