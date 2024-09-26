from channel import Channel
from video import Video
from shortvedio import ShortVideo
from comment import Comment


class User:
    def __init__(self, name, email, comment=None):
        self.name = name
        self.email = email
        self.channels = []
        self.subscribed_channels

    def create_channel(self, channel_name):
        channel = Channel(channel_name, self)
        self.channels.append(channel)
        return channel

    def subscribe_channel(self, channel):
        if channel not in self.subscribed_channels:
            self.subscribed_channels.append(channel)
            channel.subscribers.append(self)
            print("Subscription added successfully")
        else:
            return "Already subscribed"

    def like_video(self, video):
        video.likes += 1
        return "Like added"

    def comment_on_video(self, video, text):
        comment = Comment(text, self)
        video.add_comment(comment)
        return comment
