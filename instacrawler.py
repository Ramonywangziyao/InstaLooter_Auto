
#          Author: Ziyao Wang
#           copyright 2017
#   Questions contact tonywangziyao@gmail.com


import os

# starting folder name. auto starts with 0
counter = 0
num_craw = -1
instaUsername = ""
instaPassword = ""

def run():
    global counter,instaUsername,instaPassword,num_craw
    f = open("list.txt")
    name = f.readline().rstrip('\n')
    while name != "":
        #check total number of pics to craw
        if num_craw == -1:
            num_craw = name
            name = f.readline().rstrip('\n')
            continue
        #check username
        if instaUsername == "":
            instaUsername = name
            name = f.readline().rstrip('\n')
            continue
        #check password
        if instaPassword == "":
            instaPassword = name
            name = f.readline().rstrip('\n')
            continue

        dirNum = str(counter)
        os.system("mkdir ./"+dirNum)
        #hashtag
        if name[0] == "#":
            name = name[1:]
            para = name+" ./"+dirNum+" -n "+num_craw+" -c "+instaUsername+":"+instaPassword
            systemCommand = "python -m instaLooter hashtag "
        #profile
        else:
            para = name+" ./"+dirNum+" -n "+num_craw
            systemCommand = "python -m instaLooter "

        os.system(systemCommand+para)
        counter+=1
        name = f.readline().rstrip('\n')

run()
