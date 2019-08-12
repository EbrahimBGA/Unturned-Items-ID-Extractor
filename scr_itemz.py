import os

itemsList = []


def check_file(pdir,pfile):
    filename = pdir+pfile
    file = open(filename,"r")
    itemDict = {}
    itemDict["Name"]=pfile[:-4]
    itemDict["Description"] = "-"
    myType = ["Type", "ID", "Rarity"]
    while True:
        line = file.readline()
        for x in myType:
            if (line.find(x) != -1):
                txt = line.split()
                if txt[0] == x:
                    itemDict[x] = txt[1]
        if(not line):
            break

    file.close()

    ## check name in English.dat
    if check_engfile(pdir+"English.dat") == True:
        engf = open(pdir+"English.dat","r")
        en_myType = ["Name", "Description"]
        while True:
            eline = engf.readline()
            for x in en_myType:
                if eline.find(x) != -1:
                    if x == "Name":
                        txt = eline.replace("Name ","")
                        txt2 = txt.replace("\n","")
                        itemDict[x] = txt2
                    elif x== "Description":
                        txt = eline.replace("Description ","")
                        txt2 = txt.replace("\n", "")
                        txt = txt2.replace("\t", "")
                        itemDict[x] = txt
            if not eline:
                break
        engf.close()
    ##
    itemsList.append(itemDict)

def check_dir(dir):
    list = os.listdir(dir)
    for file in list:
        if os.path.isdir(dir+file):
            check_dir(dir+file+"/")
        elif (file[-4:] == ".dat" and file != "English.dat"):
            check_file(dir,file)

def check_engfile(eng_path):
    if os.path.exists(eng_path) and os.path.isfile(eng_path):
        return True
    else:
        return False



##########todo: change unturnedpath
def main():
    unturnedpath = "D:/Program Files (x86)/Steam/steamapps/common/Unturned/Bundles/Items/"
    check_dir(unturnedpath)
    for y in itemsList:
        print(y)


main()