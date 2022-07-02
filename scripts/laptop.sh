echo Setting up laptop...

# Install firmware needed for audio
echo Installing needed audio firmware...
sudo zypper in sof-firmware

# Disable 1650 Ti when not in use
echo Disabling Nvidia GPU when not utilized...
cp ../rules/etc_udev_rules.d_80-nvidia-pm.rules /etc/udev/rules.d/80-nvidia-pm.rules
cp ../conf/etc_modprobe.d_nvidia-pm.conf /etc/modprobe.d/nvidia-pm.conf
sudo systemctl enable nvidia-persistenced.service
