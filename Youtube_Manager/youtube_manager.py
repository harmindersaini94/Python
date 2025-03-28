# Just like out usual C# and Javascript code, where there is a main function or a load function
# here in python as well we have a main function, which act as the starting function
import json

def LoadVideos():
    try:
        with open("videos.txt", "r") as file:
            return json.load(file)
    except FileNotFoundError:
        return []

def ListAllVideo(videos):
    #print(videos)
    if videos:
        for index, video in enumerate(videos, start=1):
            print(f"{index}. {video['video']} - {video['duration']}")
    else:
        print("No videos found")


def AddVideo(video):
    with open("videos.txt", "w") as file:
        json.dump(video, file)

def UpdateVideo(video):
    pass

def DeleteVideo(video):
    pass

def main():
    while True:
        print(
            "\nPlease enter the task number that you want to perform\n"
            "1. List all the video\n"
            "2. Add a video\n"
            "3. Update a Video\n"
            "4. Delete a Video\n"
            "5. Exit the App\n"
        )
        user_input = int(input("Enter the task number: "))
        print(f"User input: {user_input}")

        all_videos = LoadVideos()

        match user_input:
            case 1:
                ListAllVideo(all_videos)
            case 2:
                video = input("Enter the video name: ")
                duration = input("Enter the video duration: ")
                # Remember pass a list of dictionary to the AddVideo function
                all_videos.append({'video': video, 'duration': duration})
                AddVideo(all_videos)

                print("Video added successfully")
            case 3:
                ListAllVideo(all_videos)
                video_index = int(input("Enter the video index to update: "))
                video = input("Enter the new video name: ")
                duration = input("Enter the video duration: ")

                all_videos[video_index-1] = {'video': video, 'duration': duration}
                AddVideo(all_videos)

                print("Video Updated successfully")
            case 4:
                ListAllVideo(all_videos)
                video_index = int(input("Enter the video index to delete: "))
                # dont' use pop here, will get exception
                # dont use this as well, all_videos[video_index-1] = {}, this also give exception
                del all_videos[video_index-1]
                AddVideo(all_videos)

                print("Video Deleted successfully")
            case 5:
                exit()
            case _:
                print("Invalid input\n")
                exit()

if __name__ == "__main__":
    main()


'''
So __name__ is a special variable in python, that holds the name of the script that is being executed
If the script is being executed as the main program, then __name__ is set to "__main__"

But why not run without the if condition, why do we need it?
Well, the if condition is used to check if the script is being run as the main program or not
If the script is being run as the main program, then the main function is called
If the script is being imported into another script, then the main function is not called
the script is just imported and the functions and classes are used in the other script
So the other script is the one that is in __name__

if not done, then the main function will be called even if the script is imported into another script
'''