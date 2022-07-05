# Perform initial configuration
echo Running configuration script...
python3 config.py setup

# Open package manager
echo Launching package manager...
python3 packages.py setup

# Ham radio setup
while true; do
    read -p "Setup for ham radio? " yn
    case $yn in
        [Yy]* ) . scripts/ham.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

# Laptop setup
while true; do
    read -p "Setup for laptop? " yn
    case $yn in
        [Yy]* ) . scripts/laptop.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

# Steam
while true; do
    read -p "Setup Steam? " yn
    case $yn in
        [Yy]* ) . scripts/steam.sh; break;;
        [Nn]* ) break;;
        * ) echo "Invalid option. Input yes (y) or no (n).";;
    esac
done

echo Setup has completed. Please reboot...
