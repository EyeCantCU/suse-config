# Copy over bashrc
cp conf/bashrc ~/.bashrc
source ~/.bashrc

# Add Flathub remote (user)
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Deal with packages
. scripts/remove.sh
. scripts/install.sh

# Setup wayland session
sudo cp conf/etc_sddm.conf.d_10-wayland.conf /etc/sddm.conf.d/10-wayland.conf

# Autologin
echo -e "[Autologin]\nUser=$USER\nSession=plasmawayland" | sudo tee -a /etc/sddm.conf.d/autologin.conf > /dev/null

# Laptop setup
while true; do
    read -p "Setup for laptop? " yn
    case $yn in
        [Yy]* ) . scripts/laptop.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done
