import subprocess

i = input("-------------------------------Star-Wars-----------------------------------\n\nEnter a episode no.(Between 01-09):\t")
if int(i)<9:
    subprocess.Popen(["C:/Program Files/VideoLAN/VLC/vlc.exe","E:\Movies & series\star wars\Star Wars Episode "+str(i)+".mkv"])
else:
    print("try in between limit.")
