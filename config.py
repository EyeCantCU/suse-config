from getpass import getpass
from subprocess import Popen, PIPE

import os
import shutil

def config(cwd, password, user):
	conf_dir = cwd + '/' + input("In which directory is your configuration stored? ") + '/'

	print ("Setting up your configuration...")
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

	add_config = input("Would you like to perform additional configuration? (y/N) ")
	if add_config == 'y' or add_config == 'Y':
		config(cwd, password, user)

def main():
	cwd = os.getcwd()
	user = os.getlogin()
	password = getpass("Enter your password (sudo): ")

	config(cwd, password, user)

main()
