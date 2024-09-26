from video import Video


class ShortVideo(Video):
    max_duration = 60  # seconds
    dimensions = "portrait"

    def __init__(self, title, description):
        super().__init__(title, description)

    def short_formate(self):
        return "max_duration=60 second /n Dimention=Portrate"
