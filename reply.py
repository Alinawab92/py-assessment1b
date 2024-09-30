class Reply:
    def __init__(self, comment_reply):
        self.text = comment_reply

    def display_reply(self):
        return f"Replies {self.comment_reply}"
