from os import getcwd
from subprocess import Popen, PIPE

def elevated_cmd(cmd, password):
    op = Popen(
        cmd.split(),
        stdout=PIPE, stdin=PIPE,
        stderr=PIPE
    )
    op.communicate(password.encode())

def get_packages(file):
    cwd = getcwd() + '/'
    file = cwd + 'settings/' + file

    packagestxt = open(file, 'r')
    packages = packagestxt.readlines()
    package_list = ''

    for package in packages:
        package_list += package + ' '
    return package_list
