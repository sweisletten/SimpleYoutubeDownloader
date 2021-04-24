from pytube import YouTube

save_file = input("Enter save file location: ")
link = input("Enter link of Youtube video: ")

def downloader():
    try:
        yt = YouTube(link)
        print("Accepted!")
    except Exception as e:
        print("Something went wrong:",e)
    try:
        yt.streams.first().download(save_file)
        print(yt.streams)
        print("Successful download!")
    except Exception as ex:
        print("Something went wrong:",ex)

downloader()









