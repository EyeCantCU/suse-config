# Copy over bashrc
cp bashrc ~/.bashrc
source ~/.bashrc

# Add Flathub remote (user)
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Deal with packages
. remove.sh
. install.sh
