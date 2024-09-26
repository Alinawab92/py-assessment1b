class Video:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.likes = 0
        self.comment = []

    def view_video(self):
        print(f"Watching: {self.title}\nDescription: {self.description}")

    def add_comment(self, comment):
        self.comment.append(comment)

    def get_video_info(self):
        return f"Title: {self.title}, Description: {self.description}, Likes: {self.likes}, Comments: {len(self.comment)}"
