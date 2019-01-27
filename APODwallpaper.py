import urllib.request as url
import json
import os

#open and serialize json data
jdata = url.urlopen("https://api.nasa.gov/planetary/apod?api_key=bNHPdxQMifXa2VIgQdqNFDNN6ghGVRc6vL8Z0Xls").read()
d = json.loads(jdata)

#create path to store picture
myPath = '/home/andru/Pictures'
fullfilename = os.path.join(myPath, 'wallpaper.jpg')

#retrieve image from json data and save to path
url.urlretrieve(d["hdurl"], fullfilename)

#Reset uri so image isn't cached
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri nothing")

#set background
os.system("/usr/bin/gsettings set org.gnome.desktop.background picture-uri file:///home/andru/Pictures/wallpaper.jpg")
