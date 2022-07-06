from getpass import getpass
from subprocess import Popen, PIPE

import os

def elevated_cmd(cmd, password):
    run = Popen(
        cmd.split(),
        stdout=PIPE, stdin=PIPE,
        stderr=PIPE
    )
    run.communicate(password.encode())

def scripts():
    cwd = os.getcwd() + '/'
    scripts_dir = cwd + 'scripts/'
    password = getpass("Enter your password (sudo): ")

    with os.scandir(scripts_dir) as dir:
        for script in dir:
            if script.is_file():
                print(script.name)
                cmd = 'sudo -S ' + scripts_dir + script.name
                elevated_cmd(cmd, password)

def main():
    scripts()

main()
