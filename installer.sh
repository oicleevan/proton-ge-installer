echo "Downloading proton-ge-custom!"

wget https://github.com/GloriousEggroll/proton-ge-custom/releases/download/6.16-GE-1/Proton-6.16-GE-1.tar.gz
tar -xvf Proton-6.16-GE-1.tar.gz
mkdir -p ~/.steam/root/compatibilitytools.d/
cp -r Proton-6.16-GE-1/ ~/.steam/root/compatibilitytools.d/

echo "Installation complete."