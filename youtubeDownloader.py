from pytube import YouTube

url = input("Enter the url of the YouTube video:")
ytube = YouTube(url)

print(f"The title of the youtube video which you want to download is")
print(ytube.title)

print("\n\n\n")

array = ytube.streams.all()
# list of different available resolution with index number
vid = list(enumerate(array))

for i in vid:
    print(i)

type_of_resolution = int(input("Enter streaming resolution:"))
array[type_of_resolution].download()
print('Successfully downloaded')
