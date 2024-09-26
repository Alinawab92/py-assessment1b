from video import Video
from shortvedio import ShortVideo


class Channel:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner
        self.vedio = []

    def upload_video(self, title, description):
        video = Video(title, description)  # Create a Video object
        self.vedio.append(video)
        return video

    def upload_short(self, title, description):
        short_video = ShortVideo(title, description)  # Create a ShortVideo object
        self.vedio.append(short_video)
        return short_video

    def get_subscriber_count(self):
        return len(self.subscribers)
