import filecmp
import glob
import json
songs =[]
for file in glob.glob("compressed/*"):
    song={}
    song['speaker']= "Lecturer Name Goes Here"
    song['lecture']= "Lecture Name Goes Here %s" % file
    song['conference']= "Conference Name Goes Here"
    song['url']= file
    songs.append(song)
print(json.dumps(songs))