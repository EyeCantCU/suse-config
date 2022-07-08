from getpass import getpass
from subprocess import run
from os import getcwd
from sys import argv
from tools import elevated_cmd, get_packages

def zypper(password, settings_dir, setup):
    ar_zypp = 'sudo -S zypper --non-interactive --quiet ar -C ' # link name
    ref_zypp = 'sudo -S zypper --gpg-auto-import-keys ref'
    in_zypp = 'sudo -S zypper in -y --auto-agree-with-licenses '
    rm_zypp = 'sudo -S zypper rm -y '

    opt = 1
    while True:
        if setup != True:
            print("Zypper Options:\n1. Import repos\n2. Install packages\n3. Remove packages\n4. Exit\n")
            opt = int(input("Enter an option: "))
        match opt:
            case 1:
                opt += 1
                print("Adding repos...\n")
                repostxt = open(settings_dir + 'repos.txt', 'r')
                repos = repostxt.readlines()
                for repo in repos:
                    repo_name = repo.split()[1]
                    print("Adding repo: " + repo_name)
                    ar = ar_zypp + repo
                    elevated_cmd(ar, password)
                    elevated_cmd(ref_zypp, password)
            case 2:
                opt += 1
                print("Packages marked for installation:")
                in_zypp += get_packages('zypper.txt')
                elevated_cmd(in_zypp, password)
                print("Packages installed.\n")
            case 3:
                opt += 1
                print("Packages marked for removal:")
                rm_zypp += get_packages('remove.txt')
                elevated_cmd(rm_zypp, password)
                print("Packages removed.")
            case 4:
                print("Returning to menu...\n")
                return
            case _:
                print("Invalid option. Please enter 1 to 4.")
                continue

def opi(password, setup):
    opt = 'N'
    if setup != True:
        opt = input("Install packages? (y/N) ")
    if opt == 'y' or opt == 'Y' or setup == True:
        print("Installing packages... (may take a while)\n")
        in_opi = 'opi '
        in_opi += get_packages('opi.txt')
        elevated_cmd(in_opi, password)
    else:
        print("Returning to menu...\n")

def flatpak(settings_dir, setup):
    opt = 1
    while True:
        if setup != True:
            print("Flatpak Configuration:\n1. Add remote\n2. Install packages\n3. Exit\n")
            opt = int(input("Enter an option: "))
        match opt:
            case 1:
                opt += 1
                add_remote = "flatpak remote-add --user --if-not-exists "
                remotestxt = open(settings_dir + 'remotes.txt', 'r')
                remotes = remotestxt.readlines()
                for remote in remotes:
                    remote_name = remote.split()[0]
                    print("Adding remote: " + remote_name)
                    install_remote = add_remote + remote
                    run(install_remote.split(), shell=True)
            case 2:
                opt += 1
                fp_install = 'flatpak install -y ' + get_packages('flatpaks.txt')
                run(fp_install.split(), shell=True)
            case 3:
                print("Returning to menu...\n")
                return
            case _:
                print("Invalid option. Please enter 1 to 3.\n")
                continue

def packages_setup(setup):
    password = getpass("Enter your password (sudo): ")
    settings_dir = getcwd() + '/settings/'

    if argv[1] == 'setup':
        setup = True

    opt = 1
    while True:
        if setup != True:
            print("Package Management:\n1. Zypper\n2. OPI\n3. Flatpak\n4. Exit\n")
            opt = int(input("Enter an option: "))
        match opt:
            case 1:
                opt += 1
                zypper(password, settings_dir, setup)
            case 2:
                opt += 1
                opi(password, setup)
            case 3:
                opt += 1
                flatpak(settings_dir, setup)
            case 4:
                print("Exiting...\n")
                return
            case _:
                print("Invalid option. Please enter 1 to 4.\n")
                continue

packages_setup(False)
