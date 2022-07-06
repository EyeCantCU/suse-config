from getpass import getpass
from os import getcwd, scandir
from subprocess import Popen, PIPE
from tools import elevated_cmd

def scripts():
    cwd = getcwd() + '/'
    scripts_dir = cwd + 'scripts/'
    password = getpass("Enter your password (sudo): ")

    with scandir(scripts_dir) as dir:
        for script in dir:
            if script.is_file():
                cmd = 'sudo -S ' + scripts_dir + script.name
                elevated_cmd(cmd, password)

def scripts_setup():
    scripts()

scripts_setup()
