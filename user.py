from channel import Channel
from comment import Comment


class User:
    def __init__(self, name, email):
        self.name = name
        self.email = email
        self.comment = []  # Composition: User owns comments
        self.channel = []  # Composition: User owns Channels

    def create_channel(self, channel_name):
        channel = Channel(
            channel_name, self
        )  # Create a Channel with this User as owner
        self.channel.append(channel)
        return channel

    def subscribe_channel(self, channel):
        if channel not in self.subscribed_channels:
            self.subscribed_channels.append(channel)
            channel.subscribers.append(self)
            print("Subscription added successfully")
        else:
            print("Already subscribed")

    def like_video(self, video):
        video.likes += 1
        print("Like added")

    def comment_on_video(self, video, text):
        comment = Comment(
            text, self
        )  # Create Comment with this User as author
        video.add_comment(comment)
        print("Comment added")
