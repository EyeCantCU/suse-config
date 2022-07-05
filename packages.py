from getpass import getpass
from subprocess import Popen, PIPE

import os
import subprocess

def elevated_cmd(cmd, password):
    run = Popen(
        cmd.split(),
        stdout=PIPE, stdin=PIPE,
        stderr=PIPE
    )
    run.communicate(password.encode())

def get_packages(file):
    cwd = os.getcwd() + '/'
    file = cwd + file

    packagestxt = open(file, 'r')
    packages = packagestxt.readlines()
    package_list = ''

    for package in packages:
        package_list += package + ' '
    return package_list

def zypper(password):
    ar_zypp = 'sudo -S zypper --non-interactive --quiet ar -C ' # link name
    ref_zypp = 'sudo -S zypper --gpg-auto-import-keys ref'
    in_zypp = 'sudo -S zypper in -y --auto-agree-with-licenses '
    rm_zypp = 'sudo -S zypper rm -y '

    while True:
        print("Zypper Options:\n1. Import repos\n2. Install packages\n3. Remove packages\n4. Exit\n")
        opt = int(input("Enter an option: "))
        match opt:
            case 1:
                print("Adding repos...\n")
                repostxt = open('repos.txt', 'r')
                repos = repostxt.readlines()
                for repo in repos:
                    ar = ar_zypp + repo
                    elevated_cmd(ar, password)
                    elevated_cmd(ref_zypp, password)
            case 2:
                print("Installing packages... (may take a while)\n")
                in_zypp += get_packages('zypper.txt')
                elevated_cmd(in_zypp, password)
            case 3:
                print("Removing packages...")
                rm_zypp += get_packages('remove.txt')
                elevated_cmd(rm_zypp, password)
            case 4:
                print("Returning to menu\n")
                return
            case _:
                print("Invalid option. Please enter 1 to 4")
                continue

def opi(password):
    opt = input("Install packages? (y/N) ")
    if opt == 'y' or opt == 'Y':
        print("Installing packages... (may take a while)\n")
        in_opi = 'opi '
        in_opi += get_packages('opi.txt')
        elevated_cmd(in_opi, password)
    else:
        print("Returning to menu\n")

def flatpak():
    while True:
        print("Flatpak Configuration:\n1. Add remote\n2. Install packages\n3. Exit\n")
        opt = int(input("Enter an option: "))
        match opt:
            case 1:
                add_remote = "flatpak remote-add --user --if-not-exists "
                remotestxt = open('remotes.txt', 'r')
                remotes = remotestxt.readlines()
                for remote in remotes:
                    install_remote = add_remote + remote
                    subprocess.run(install_remote.split())
            case 2:
                fp_install = 'flatpak install ' + get_packages('flatpaks.txt')
                subprocess.run(fp_install.split())
            case 3:
                return
            case _:
                print("Invalid option. Please enter 1 to 3\n")
                continue

def main():
    password = getpass("Enter your password (sudo): ")

    while True:
        print("Package Management:\n1. Zypper\n2. OPI\n3. Flatpak\n4. Exit\n")
        opt = int(input("Enter an option: "))
        match opt:
            case 1:
                zypper(password)
            case 2:
                opi(password)
            case 3:
                flatpak()
            case 4:
                print("Exiting...\n")
                return
            case _:
                print("Invalid option. Please enter 1 to 4\n")
                continue

main()
