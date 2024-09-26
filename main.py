from user import User


def main():
    # Create a User
    user1 = User("Ali", "ali@gmail.com")

    # Create a Channel
    channel1 = user1.create_channel("cartoon Reviews")

    # Upload a video
    video1 = channel1.upload_video("Latest Review", "In-depth review ")

    # User likes the video
    user1.like_video(video1)

    # User comments on the video
    user1.comment_on_video(video1, "Great review!")

    # View video info
    print(video1.get_video_info())

    # Upload a short video
    short_video1 = channel1.upload_short(
        "Quick Smartphone Review", "A short review of short."
    )

    # View short video info with correct method name

    print(short_video1.get_video_info())


if __name__ == "__main__":
    main()
