from video import Video
from shortvideo import ShortVideo


class Channel:
    def __init__(self, name, user):
        self.name = name
        self.owner = user
        self.videos = []
        self.subscribers = []

    def upload_video(self, title, description):
        video = Video(title, description)
        self.videos.append(video)
        return video

    def upload_short(self, title, description):
        short_video = ShortVideo(title, description)
        self.videos.append(short_video)
        return short_video

    def get_subscriber_count(self):
        return len(self.subscribers)

    def display_channel_info(self):
        return f"Channel: {self.name}, Owner: {self.owner.name}, Videos: {len(self.videos)}, Subscribers: {len(self.subscribers)}"
