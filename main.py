from user import User


def main():
    # Create Users
    user1 = User("Ali", "alihaider@gmail.com")
    user2 = User("abdullah", "abdullahgmail.com")

    # User 1 creates a channel
    channel1 = user1.create_channel("Tech Reviews")
    channel2 = user2.create_channel("Cooking hub")

    # User 1 uploads videos to Tech Reviews
    video1 = channel1.upload_video(
        "Latest Smartphone", "Review of the latest smartphone."
    )
    video2 = channel1.upload_video(
        "Laptop Review", "Review of a new gaming laptop."
    )

    # User 2 uploads videos to Cooking Delights
    video3 = channel2.upload_video(
        "Pasta Recipe", "How to make the best pasta."
    )
    video4 = channel2.upload_short(
        "Quick Salad", "A quick recipe for a refreshing salad."
    )

    # User 1 likes a video
    user1.like_video(video1)
    user1.like_video(video3)

    # User 2 comments on a video
    user2.comment_on_video(video1, "I love this review! ")
    user2.comment_on_video(
        video2, "Can you compare it with the previous model?"
    )

    # User 1 comments on Cooking Delights videos
    user1.comment_on_video(video3, "This recipe is amazing! Thank you!")

    # Print video information
    print(video1.get_video_info())
    print(video2.get_video_info())
    print(video3.get_video_info())
    print(video4.get_video_info())

    # User 2 subscribes to User 1's channel
    user2.subscribe_channel(channel1)

    # Print subscriber counts
    print(
        f"Subscriber Count for '{channel1.name}': {channel1.get_subscriber_count()}"
    )
    print(
        f"Subscriber Count for '{channel2.name}': {channel2.get_subscriber_count()}"
    )

    # Print comments
    for comment in video1.comments:
        print(f"{comment.author.name} commented: {comment.text}")


if __name__ == "__main__":
    main()
