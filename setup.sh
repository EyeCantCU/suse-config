# Copy over bashrc
cp bashrc ~/.bashrc
source ~/.bashrc

# Add Flathub remote (user)
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Deal with packages
. remove.sh
. install.sh

# Setup wayland session
sudo cp etc_sddm.conf.d_10-wayland.conf /etc/sddm.conf.d/10-wayland.conf

while true; do
    read -p "Setup for laptop? " yn
    case $yn in
        [Yy]* ) . laptop.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done
