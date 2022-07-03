# NOTE: All of this will require interaction

# First update
echo Updating...
sudo zypper dup

# Now the rest
echo Installing opi...
sudo zypper in opi
echo Installing codecs...
opi codecs
echo Installing Brave...
opi brave

# Nvidia driver
echo Installing Nvidia driver...
sudo zypper addrepo --refresh https://download.nvidia.com/opensuse/tumbleweed NVIDIA
sudo zypper in x11-video-nvidiaG06 x11-video-nvidiaG06-32bit nvidia-glG06 nvidia-glG06-32bit nvidia-computeG06 nvidia-computeG06-32bit libnvidia-egl-wayland1 libnvidia-egl-wayland1-32bit

# Needed for full modmic functionality
echo Installing alsa firmware...
sudo zypper in alsa-firmware

# Android
echo Installing android tools...
sudo zypper in android-tools android-udev-rules

# VS Code
while true; do
    read -p "Install VS Code? " yn
    case $yn in
        [Yy]* ) opi vscode; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

# ProtonVPN
echo Installing ProtonVPN...
sudo zypper in protonvpn-gui

# xbindkeys
echo Installing xbindkeys...
sudo zypper in xbindkeys

# Flatpak
echo Installing Tidal...
flatpak install tidal-hifi
