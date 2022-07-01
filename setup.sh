# Copy over bashrc
cp bashrc ~/.bashrc
source ~/.bashrc

# Add Flathub remote (user)
flatpak remote-add --user --if-not-exists flathub https://flathub.org/repo/flathub.flatpakrepo

# Deal with packages
. remove.sh
. install.sh

while true; do
    read -p "Setup for laptop? " yn
    case $yn in
        [Yy]* ) . laptop.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done
