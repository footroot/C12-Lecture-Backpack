from pytubefix import YouTube

def get_basic_streams(url):
    yt = YouTube(url)
    streams = yt.streams.filter(progressive=True) # []
    return streams

def view_streams(streams):
    for i, stream in enumerate(streams):
        print(f"{i+1}: Resolution: {stream.height}p - {stream.filesize_mb}mb")


def main():
    menu = ("-"*80) + "\n" + (" "*31) + "Youtube Downloader\n" + ("-"*80)
    menu += "\n1: Download Video\n0: Quit"

    while True:
        print(menu)
        user_option = input()
        if user_option == "1":
            user_url = input("Please provide the url of the video you would like to download:\n")
            streams = get_basic_streams(user_url)
            view_streams(streams)
            quality_choice = input("Please select a quality:")
            quality_choice = int(quality_choice)-1
            streams[quality_choice].download()
        if user_option == "0":
            break


if __name__ == "__main__":
    main()

