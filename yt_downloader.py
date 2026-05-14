# from pytube import YouTube 
# from sys import argv 

# link = argv[1]
# yt = YouTube(link) 

# print("Title: ", yt.title) 

# print("View: ", yt.views) 

# yd = yt.streams.get_highest_resolution() 
# yd.download('E:\YouTube_Videos')

# from pytube import YouTube 
# from sys import argv 

# # Check if the required command-line argument is provided
# if len(argv) < 2:
#     print("Usage: python3 script_name.py <YouTube_link>")
#     exit(1)

# link = argv[1]
# yt = YouTube(link) 

# print("Title:", yt.title) 
# print("Views:", yt.views) 

# yd = yt.streams.get_by_itag(22)  # OR #yt.streams.get_highest_resolution() 
# yd.download('E:\YouTube_Videos')  # Escape the backslash

# import youtube_dl
# from sys import argv

# # Check if the required command-line argument is provided
# if len(argv) < 2:
#     print("Usage: python3 script_name.py <YouTube_link>")
#     exit(1)

# link = argv[1]

# ydl_opts = {'outtmpl': r'C:\Users\Topu\Documents\Python\%(title)s.%(ext)s'}

# with youtube_dl.YoutubeDL(ydl_opts) as ydl:
#     ydl.download([link])

from pytube import YouTube 
link = input("Enter the YouTube link: ")

video = YouTube(link) 
stream = video.streams.get_highest_resolution() 
stream.download()
 