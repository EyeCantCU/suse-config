# NOTE: All of this will require interaction

# First update
sudo zypper dup

# Now the rest
sudo zypper in opi
opi codecs
opi brave

# Nvidia driver
sudo zypper addrepo --refresh https://download.nvidia.com/opensuse/tumbleweed NVIDIA
sudo zypper in x11-video-nvidiaG06 x11-video-nvidiaG06-32bit nvidia-glG06 nvidia-glG06-32bit nvidia-computeG06 nvidia-computeG06-32bit libnvidia-egl-wayland1 libnvidia-egl-wayland1-32bit

# Needed for full modmic functionality
sudo zypper in alsa-firmware

# Steam
sudo zypper in steam

# Android
sudo zypper in android-tools android-udev-rules

# Flatpak
flatpak install tidal-hifi
