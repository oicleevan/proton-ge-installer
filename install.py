#!/usr/bin/python

import os,sys

if(len(sys.argv) > 1):
    opt=sys.argv[1]
else:
    opt=None

version = "6.18-GE-2"
url=f"https://github.com/GloriousEggroll/proton-ge-custom/releases/download/{version}/Proton-{version}.tar.gz"

def install(ver, link):
    print("Installing the newest version of proton-ge\n")

    Commands = [
        "wget " + link,
        "mkdir -p ~/.steam/root/compatibilitytools.d/",
        f"tar -xvf Proton-{ver}.tar.gz -C ~/.steam/root/compatibilitytools.d/",
        f"rm Proton-{ver}.tar.gz"
    ]

    for i in Commands:
        os.system(i)

    print(f"\nProton-GE {ver} installed.")
    exit

def upgrade(ver, link):
    
    print(f"Upgrading proton-ge to {ver}...\n")

    Commands = [
        "rm -rf ~/.steam/root/compatibilitytools.d/Proton*",
        "wget " + link,
        "mkdir -p ~/.steam/root/compatibilitytools.d/",
        f"tar -xvf Proton-{ver}.tar.gz -C ~/.steam/root/compatibilitytools.d/",
        f"rm Proton-{ver}.tar.gz"
    ]

    for i in Commands:
        os.system(i)

    print(f"\nProton-GE updated to version {version}")

    exit

def help():
    Messages = [
        "Proton-GE is a modified version of the Proton compatibility layer. It is just fantastic.",
        "This is an auto installer, installing the newest version of the software.",
        "",
        "Options:",
        "    -a -- auto (newest version)",
        "    -v (version) -- installs your defined version",
        "    -u -- upgrade to the newest version, delete old version(s)"
    ]

    for i in Messages:
        print(i)

    exit

if(opt == None or opt == "-h"):
    help()
elif(opt == "-a"):
    install(version, url)
elif(opt == "-v"):
    user_ver = sys.argv[2]
    user_url=f"https://github.com/GloriousEggroll/proton-ge-custom/releases/download/{user_ver}/Proton-{user_ver}.tar.gz"
    
    install(user_ver, user_url)
elif(opt == "-u"):
    upgrade(version, url)
else:
    print("Please rerun the program with no arguments.")
    exit
