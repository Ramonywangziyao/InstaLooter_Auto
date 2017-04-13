import os

# starting folder name. auto starts with 0
counter = 0
instaUsername = ""
instaPassword = ""

def run():
    global counter,instaUsername,instaPassword
    f = open("list.txt")
    name = f.readline().rstrip('\n')
    while name != "":
        if instaUsername == "":
            instaUsername = name
            continue

        if instaPassword == ""
            instaPassword = name
            continue

        dirNum = str(counter)
        os.system("mkdir ./"+dirNum)
        #hashtag
        if name[0] == "#":
            name = name[1:]
            para = name+" ./"+dirNum+" -n 400 -c "+instaUsername+":"+instaPassword
            systemCommand = "python -m instaLooter hashtag "
        #profile
        else:
            para = name+" ./"+dirNum+" -n 400"
            systemCommand = "python -m instaLooter "

        os.system(systemCommand+para)
        counter+=1
        name = f.readline().rstrip('\n')

run()
