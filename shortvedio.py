from video import Video


class ShortVideo(Video):
    def __init__(self, title, description):
        super().__init__(title, description)
        self.duration = 60  # Max duration for short video

    def short_formate(self):  # Ensure this is spelled 'short_formate'
        return f"{self.title} is in short format with {self.duration} seconds duration."
