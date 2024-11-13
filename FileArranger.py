#!/usr/bin/env python3
import os
import subprocess

#_______________________-___________________importing
class Arrange:
    path="/home/siddhant/Desktop"    # change it like Downloads
    def __init__(self):
        self.path=Arrange.path
        self.images=folders_names["imagesfolder"]
        self.videos=folders_names["videosfolder"]
        self.music=folders_names["musicfolder"]
        self.documents=folders_names["documentsfolder"]

        if not os.path.exists(self.path) :
              print("The default path is different Please check code")
              exit()
        else:

              os.chdir(self.path)
              self.files=subprocess.check_output(["ls"]).decode().split()
    def make(self):
            for folder in [self.images,self.music,self.videos,self.documents]:
                if not os.path.isdir(folder):
                  os.makedirs(folder)

    def scan(self):
        for file_name in self.files:


            if not os.path.isdir(file_name):
                each_file=os.path.splitext(file_name)

                try:


                    if each_file[1] in file_extensions["MusicExtension"]:
                        os.system("mv {} {} ".format(file_name,self.music))

                    if each_file[1] in file_extensions["ImageExtension"]:
                        os.system("mv {} {} ".format(file_name,self.images))


                    if each_file[1] in file_extensions["VideoExtension"]:
                        os.system("mv {} {} ".format(file_name,self.videos))
                    if each_file[1] in file_extensions["DocumentExtension"]:
                        os.system("mv {} {} ".format(file_name,self.documents))


                except:
                    pass

if __name__ =="__main__":
    file_extensions={
    "MusicExtension":[".mp3",".wav",".3gp"],
    "ImageExtension":[".jpeg",".jpg",".png"],
    "VideoExtension":[".mp4",".webm",".mkv"],
    "DocumentExtension":[".txt",".pdf",".py"]
}
    folders_names={
     "musicfolder":"Songs_By_Python",
     "imagesfolder":"Images_By_Python",
     "videosfolder":"Videos_By_Python",
     "documentsfolder":"Documents_By_Python"

    }
    start=Arrange()
    start.make()
    start.scan()
# done made by CoolSidOfficial  on 16feb2021
