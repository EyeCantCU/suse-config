# Steam
sudo zypper in steam

# Proton
echo "Before setting up Proton GE, you must go through Steam's initial setup."
while true; do
    read -p "Have you ran Steam? " yn
    case $yn in
        [Yy]* ) mkdir ~/.steam/root/compatibilitytools.d/ && pip3 install protonup-ng && protonup -d "~/.steam/root/compatibilitytools.d/" && protonup; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done
