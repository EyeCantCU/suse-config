# Ham radio
while true; do
    read -p "Setup for ham radio? " yn
    case $yn in
        [Yy]* ) break;;
        [Nn]* ) exit;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

echo Installing ham radio software...
opi chirp wsjtx
sudo zypper in fldigi
