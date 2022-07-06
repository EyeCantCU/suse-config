from config import config_setup
from packages import packages_setup
from scripts import scripts_setup

def main():
    print("Running configurator...")
    config_setup(True)

    print("Managing packages...")
    packages_setup(True)

    print("Running scripts...")
    scripts_setup()

    print("Setup has completed. Please reboot.")

main()
