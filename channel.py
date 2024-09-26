from video import Video, ShortVideo


class Channel:
    def __init__(self, name, owner):
        self.name = name
        self.owner = owner  # Owner has a "has-a" relationship with User
        self.subscribers = []
        self.videos = []  # Channel has a list of videos

    def upload_video(self, title, description, comments=[]):
        video = Video(
            title, description, comments
        )  # Pass comments to Video
        self.videos.append(video)
        return video

    def upload_short(self, title, description):
        short_video = ShortVideo(title, description)
        self.videos.append(
            short_video
        )  # Store shorts in the same list of videos
        return short_video

    def get_subscriber_count(self):
        return len(self.subscribers)
