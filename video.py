class Video:
    def __init__(self, title, description):
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = []  # A video has many comments

    def view_video(self):
        print(f"Watching: {self.title}\nDescription: {self.description}")

    def add_comment(self, comment):
        self.comments.append(comment)

    def add_like(self):
        self.likes += 1

    def get_video_info(self):
        return f"Title: {self.title}, Description: {self.description}, Likes: {self.likes}, Comments: {len(self.comments)}"
