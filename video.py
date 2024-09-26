class Video:
    def __init__(
        self, title, description, comments=None
    ):  # Accept comments as an argument
        self.title = title
        self.description = description
        self.likes = 0
        self.comments = (
            comments if comments is not None else []
        )  # Initialize with passed comments

    def view_video(self):
        print(
            f"Watching: {self.title}\nDescription: {self.description}"
        )

    def add_comment(self, comment):
        self.comments.append(comment)

    def get_video_info(self):
        return f"Title: {self.title}, Description: {self.description}, Likes: {self.likes}, Comments: {len(self.comments)}"


class ShortVideo(Video):
    max_duration = 60  # seconds
    dimensions = "portrait"

    def __init__(self, title, description):
        super().__init__(title, description)
