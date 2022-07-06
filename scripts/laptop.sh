# Laptop
while true; do
    read -p "Setup laptop? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

echo Setting up laptop...

# Install firmware needed for audio
echo Installing needed audio firmware...
sudo zypper in sof-firmware

# Disable 1650 Ti when not in use
echo Disabling Nvidia GPU when not utilized...
sudo rm /lib/modprobe.d/09-nvidia-modprobe-bbswitch-G04.conf
sudo systemctl enable nvidia-persistenced.service
