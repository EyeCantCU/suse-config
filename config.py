from getpass import getpass
from subprocess import Popen, PIPE
from sys import argv

import glob
import os
import shutil

def config(conf_index, cwd, password, setup, user):
    if setup != True:
        conf_dir = cwd + '/config/' + input("In which directory is your configuration stored? ") + '/'
    else:
        conf_list = glob.glob(cwd + '/config/*/')
        conf_dir = conf_list[conf_index]
        conf_index += 1

    print("Setting up your configuration...")
    for conf in os.scandir(conf_dir):
        dest = conf.name.replace('_', '/')
        if dest.startswith('root'):
            dest = dest.removeprefix('root')
            copy_conf = 'sudo -S cp ' + conf_dir + conf.name + ' ' + dest
            copy = Popen(
                copy_conf.split(),
                stdin=PIPE, stdout=PIPE,
                stderr=PIPE
            )
            copy.communicate(password.encode())
            print("Copied " + conf.name + " to " + dest)
        else:
            dest = dest = "/home/" + user + "/"
            if conf.name.endswith('rc'):
                dest += "." + conf.name
            else:
                dest += conf.name
            shutil.copyfile(conf, dest)
            print("Copied " + conf.name + " to " + dest)

    if setup != True:
        add_config = input("Would you like to perform additional configuration? (y/N) ")
        if add_config == 'y' or add_config == 'Y':
            config(cwd, password, user, setup)
    else:
        config(conf_index, cwd, password, user, setup)

def main():
    cwd = os.getcwd()
    user = os.getlogin()
    password = getpass("Enter your password (sudo): ")
    setup = False

    if argv[1] == 'setup':
        setup = True

    config(0, cwd, password, setup, user)

main()
