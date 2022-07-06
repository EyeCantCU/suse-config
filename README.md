## For personal use. The openSUSE wiki should be consulted instead as configurations change frequently.


# Scripts:


* __setup.py:__ Runs all scripts while bypassing as much needed user interaction as possible
* __config.py:__ Installs configurations found in config folder. To move a file that requires escalated privledges, append 'root' to the file name's prefix. Note that an '_' is used to differentiate directories therefore you can not use it in a filename
* __packages.py:__ Installs all packages in 'zypper.txt', 'opi.txt', and 'flatpaks.txt'. Removes packages defined in 'remove.txt'. Also adds remotes defined in 'repos.txt' to zypper and to flatpak via 'remotes.txt'
* __scripts.py:__ Runs all shell scripts found in the 'scripts' folder currently only with escalated privledges
* __tools.py:__ Contains commonly used functions


# Shell Scripts:


* __laptop.sh:__ Installs audio firmware and configures GPU offload

* __ham.sh:__ Installs packages needed for ham radio

* __steam.sh:__ Installs Steam, protonup-ng, and Proton GE

* __remove.sh:__ Currently just removes Firefox

* __starwars.sh:__ Telnet Star Wars (for fun)


# Configuration files:


* __bashrc:__ Sets the default editor to nano and updates path
* __xkeybindkeysrc:__ Enables scroll based zoom on KDE
