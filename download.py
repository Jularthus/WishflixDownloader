import os
from chemin import dir

def downloadList(list, name, season):
    curdir = os.getcwd()
    dir = dir + f"/{name}/{season}"
    try:
        os.chdir(dir) 
    except:
        os.makedirs(dir)

    os.chdir(curdir)
    for i in range(len(list)):
        newname = ""
        if len(str(i+1)) > 9:
            newname = str(i+1) + "-" + name + ".mp4"
        else:
            newname = "0" + str(i+1) + "-" + name + ".mp4"

        os.system(f'cmd /c' + r'%CD%\lib\uqload_downloader.exe ' + f'{list[i]} "{dir}/{newname}"')
        print(f'{dir}/{newname}')