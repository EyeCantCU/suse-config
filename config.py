from shutil import copyfile
from getpass import getpass
from glob import glob
from os import getcwd, getlogin, scandir
from sys import argv
from tools import elevated_cmd

def config(conf_index, cwd, password, setup, user):
    if setup != True:
        conf_dir = cwd + 'config/' + input("In which directory is your configuration stored? ") + '/'
    else:
        conf_list = glob(cwd + 'config/*/')
        conf_dir = conf_list[conf_index]
        conf_index += 1

    print("Setting up your configuration...")
    for conf in scandir(conf_dir):
        dest = conf.name.replace('_', '/')
        if dest.startswith('root'):
            dest = dest.removeprefix('root')
            copy_conf = 'sudo -S cp ' + conf_dir + conf.name + ' ' + dest
            elevated_cmd(copy_conf, password)
            print("Copied " + conf.name + " to " + dest)
        else:
            dest = dest = "/home/" + user + "/"
            if conf.name.endswith('rc'):
                dest += "." + conf.name
            else:
                dest += conf.name
            copyfile(conf, dest)
            print("Copied " + conf.name + " to " + dest)

    if setup != True:
        add_config = input("Would you like to perform additional configuration? (y/N) ")
        if add_config == 'y' or add_config == 'Y':
            config(conf_index, cwd, password, user, setup)
    else:
        config(conf_index, cwd, password, user, setup)

def config_setup(setup):
    cwd = getcwd() + '/'
    user = getlogin()
    password = getpass("Enter your password (sudo): ")

    if argv[1] == 'setup':
        setup = True

    config(0, cwd, password, setup, user)

config_setup(False)
