from user import User  # Import the User class from user.py


def main():
    # Step 1: Create a User
    print("Creating a new user...")
    user1 = User("Ali Nawab Haider", "haider@gmail.com")
    print(f"User '{user1.name}' created with email: {user1.email}\n")

    # Step 2: User creates a channel
    print("User is creating a channel...")
    channel1 = user1.create_channel("Tech Reviews")
    print(f"Channel '{channel1.name}' created by {channel1.owner.name}\n")

    # Step 3: Upload a regular video to the channel
    print("Uploading a regular video to the channel...")
    video1 = channel1.upload_video(
        "Latest Smartphone Review",
        "In-depth review of the latest smartphone.",
    )
    print(f"Video '{video1.title}' uploaded to channel '{channel1.name}'\n")

    # Step 4: User likes the video
    print("User likes the video...")
    user1.like_video(video1)
    print(f"Video '{video1.title}' now has {video1.likes} like(s)\n")

    # Step 5: User comments on the video
    print("User comments on the video...")
    comment1 = user1.comment_on_video(video1, "Great review! Very informative.")
    print(f"Comment '{comment1.text}' added by {comment1.author.name}\n")

    # Step 6: Upload a short video
    print("Uploading a short video to the channel...")
    short_video1 = channel1.upload_short(
        "Quick Smartphone Overview",
        "A quick overview of the new smartphone.",
    )

    # Step 7: Display video information
    print("Displaying information of the uploaded videos...")
    print(video1.get_video_info())
    print(short_video1.get_video_info())

    # Step 8: Display channel information
    print("\nDisplaying channel information...")
    print(channel1.display_channel_info())


if __name__ == "__main__":
    main()
