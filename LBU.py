# Login Background Updater by Greg Flynn
# http://www.freakeffects.net/
# https://github.com/Nuckinfuts/Login-Background-Updater

from shlex import split
from subprocess import Popen, check_output

stdout = check_output(split("defaults read com.apple.desktop Background"))
stdout = stdout.decode("utf-8")

std = []
std.append("")

index = 0

defaultString    = "default ="
backgroundString = "ImageFilePath ="
inDefault        = False
path             = "Error"

for c in stdout: #for every outputted char, gotta clean this up!
    if not c == '\n':
        std[index]+=c
    else:
        std.append("")
        index+=1

for line in std: #for every line outputted in std
    if inDefault:
        if line.find(backgroundString) != -1:
            begin = line.find("\"")
            end   = line.rfind("\"")
            path = line[begin+1:end]
            break
    else:
        if line.find(defaultString) != -1:
            inDefault = True
            
if not path == "Error":
    cp = split(str('cp %s /.LoginBackground' % path))
    cmd = split(str('defaults write /Library/Preferences/com.apple.loginwindow DesktopPicture "/.LoginBackground"'))
    Popen(cp)
    Popen(cmd)