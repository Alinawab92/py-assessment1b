from video import Video


class ShortVideo(Video):
    def __init__(self, title, description):
        super().__init__(title, description)
        self.max_length = 60  # Max length in seconds

    def short_format(self):
        return f"{self.title} (Short video, Max length: {self.max_length} seconds)"
