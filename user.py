from channel import Channel
from comment import Comment


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.comments = []
        self.channels = []

    def create_channel(self, channel_name):
        channel = Channel(channel_name, self)
        self.channels.append(channel)
        return channel

    def subscribe_channel(self, channel):
        if channel not in self.channels:
            channel.subscribers.append(self)
            return f"{self.name} subscribed to {channel.name}"
        else:
            return "Already subscribed"

    def like_video(self, video):
        video.add_like()
        return "Like added!"

    def comment_on_video(self, video, text):
        comment = Comment(text, self)
        video.add_comment(comment)
        return comment
