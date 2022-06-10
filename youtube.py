# import the module
from re import A
from pytube import YouTube as pyt
#where to save
savePath= r"C:\Users\lenovo corei7\Desktop\Lenguajes de programacion"
#link of the video that you want to download
link = "https://www.youtube.com/watch?v=ivCY3Ec4iaU"

a =5
b = 4
r = 5*2
print(r)

try:
    #object creation 
    url = pyt(link)
except:
    print("connection error") # handele any error

# filter all the files with the extantions that we want, in this case MP4 but we can change it
typefile= pyt.filter('mp4') # choose the extension that you will need

# set the video name 
pyt.set.filename('Follow God video') # Put here the name that you will want for your file 

# get extension and resolution 
d_video = pyt.get(typefile[-1].extension,typefile[-1].resolution)

a =5
b = 4
r = 5*2
print(r)
#download the video 
try : 
    d_video.download(savePath)
except:
    print("something went wrong \n you can check the link or the extension")

print("congrats!, the file was succesfuly download")
