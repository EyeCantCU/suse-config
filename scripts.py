from getpass import getpass
from subprocess import Popen, PIPE

import os
import tools

def scripts():
    cwd = os.getcwd() + '/'
    scripts_dir = cwd + 'scripts/'
    password = getpass("Enter your password (sudo): ")

    with os.scandir(scripts_dir) as dir:
        for script in dir:
            if script.is_file():
                cmd = 'sudo -S ' + scripts_dir + script.name
                tools.elevated_cmd(cmd, password)

def main():
    scripts()

main()
