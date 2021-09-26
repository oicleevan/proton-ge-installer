import os

version = "6.16-GE-1"

url=f"https://github.com/GloriousEggroll/proton-ge-custom/releases/download/{version}/Proton-{version}.tar.gz"

print("Installing the newest version of proton-ge\n")

Commands = [
    "wget " + url,
    "mkdir -p ~/.steam/root/compatibilitytools.d/",
    f"tar -xvf Proton-{version}.tar.gz -C ~/.steam/root/compatibilitytools.d/",
    "rm Proton-{version}.tar.gz"
]

for i in Commands:
    os.system(i)

print(f"\nProton-GE {version} installed.")
