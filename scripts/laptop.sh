echo Setting up laptop...

# Install firmware needed for audio
echo Installing needed audio firmware...
sudo zypper in sof-firmware

# Disable 1650 Ti when not in use
echo Disabling Nvidia GPU when not utilized...
sudo rm /lib/modprobe.d/09-nvidia-modprobe-bbswitch-G04.conf
sudo systemctl enable nvidia-persistenced.service
