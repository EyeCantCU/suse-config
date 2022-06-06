# Copy over bashrc
cp bashrc ~/.bashrc
source ~/.bashrc

# Deal with packages
. remove.sh
. install.sh

# Copy over xbindkeys
cp xbindkeysrc ~/.xbindkeysrc
killall xbindkeys
xbindkeys
