from user import User


def main():
    # Create Users
    user1 = User("Ali Nawab Haider", "haider@gmail.com")
    user2 = User("usman", "usman@gmail.com")

    # User1 creates a Channel
    channel1 = user1.create_channel("cartoon")
    print(f"{user1.name} created the channel: {channel1.name}")

    # User1 uploads a Video
    video1 = channel1.upload_video(
        "Tom and Jerry", "Review of the latest Episode."
    )
    print(f"Video uploaded: {video1.title}")

    # User2 subscribes to User1's Channel
    user2.subscribe_channel(channel1)

    # User1 likes the video they uploaded
    user1.like_video(video1)

    # User2 likes the video
    user2.like_video(video1)

    # User2 comments on the Video
    user2_comment = user2.comment_on_video(
        video1, "This was super helpful, thanks!"
    )
    print(f"Comment added by {user2.name}: {user2_comment.text}")

    # User1 replies to the comment made by User2
    user1_reply = user2_comment.add_reply(
        "Glad you found it useful!", user1
    )

    # Display video information after interactions
    print("\nVideo Info After User Interactions:")
    print(video1.get_video_info())

    # Upload a Short Video
    short_video1 = channel1.upload_short(
        "pink panther", "A quick overview of the cartoon."
    )
    print(f"\nShort Video uploaded: {short_video1.title}")

    # Display short video information
    print(short_video1.get_video_info())

    # Show the number of subscribers to the channel
    print(
        f"\nTotal Subscribers of {channel1.name}: {channel1.get_subscriber_count()}"
    )


if __name__ == "__main__":
    main()
