#!/usr/bin/env python3

__author__ = "james_s60"
__date__ = "04 November 2024"
__credits__ = ["james_s60"]
__version__ = "1.1"


############################
# Imports
############################
# import ast
from configparser import ConfigParser 
from colorama import Style  
import os
##
from functions import git
from functions import script
from functions import ntfy
from functions import docker_compose
from functions import docker
# from functions import docker
# from functions import podman
############################


############################
# Parse Config
############################
config = ConfigParser()
config.read('/usr/share/ContainerCleaner/conf/config.ini')
# Main
CONTAINER_ENGINE = str(config['MAIN']['CONTAINER_ENGINE'])
# Docker Compose
COMPOSE_FILE = str(config['DOCKER_COMPOSE']['COMPOSE_FILE'])
# Git
GIT_ENABLED = config['GIT'].getboolean('GIT_ENABLED')
GIT_REPO_PATH = str(config['GIT']['GIT_REPO_PATH'])
# Ntfy
NTFY_ENABLED = config['NTFY'].getboolean('NTFY_ENABLED')
# NTFY_HOST = str(config['NTFY']['NTFY_HOST'])     - This is now parsed directly in src/functions/ntfy.py!
# NTFY_TOPIC = str(config['NTFY']['NTFY_TOPIC'])   - This is now parsed directly in src/functions/ntfy.py!


# Note to future self, if accepting a list of container images, must use ast method
# Exmaple: IMAGES = ast.literal_eval(config.get("PODMAN", "IMAGES"))
############################




os.system("clear")
script.rainbow("\n \
  /$$$$$$                        /$$               /$$                              \n \
 /$$__  $$                      | $$              |__/                              \n \
| $$  \__/  /$$$$$$  /$$$$$$$  /$$$$$$    /$$$$$$  /$$ /$$$$$$$   /$$$$$$   /$$$$$$ \n \
| $$       /$$__  $$| $$__  $$|_  $$_/   |____  $$| $$| $$__  $$ /$$__  $$ /$$__  $$\n \
| $$      | $$  \ $$| $$  \ $$  | $$      /$$$$$$$| $$| $$  \ $$| $$$$$$$$| $$  \__/\n \
| $$    $$| $$  | $$| $$  | $$  | $$ /$$ /$$__  $$| $$| $$  | $$| $$_____/| $$      \n \
|  $$$$$$/|  $$$$$$/| $$  | $$  |  $$$$/|  $$$$$$$| $$| $$  | $$|  $$$$$$$| $$      \n \
 \______/  \______/ |__/  |__/   \___/   \_______/|__/|__/  |__/ \_______/|__/      \n \
  /$$$$$$  /$$                                                                      \n \
 /$$__  $$| $$                                                                      \n \
| $$  \__/| $$  /$$$$$$   /$$$$$$  /$$$$$$$   /$$$$$$   /$$$$$$                     \n \
| $$      | $$ /$$__  $$ |____  $$| $$__  $$ /$$__  $$ /$$__  $$                    \n \
| $$      | $$| $$$$$$$$  /$$$$$$$| $$  \ $$| $$$$$$$$| $$  \__/                    \n \
| $$    $$| $$| $$_____/ /$$__  $$| $$  | $$| $$_____/| $$                          \n \
|  $$$$$$/| $$|  $$$$$$$|  $$$$$$$| $$  | $$|  $$$$$$$| $$                          \n \
 \______/ |__/ \_______/ \_______/|__/  |__/ \_______/|__/                          \n \
                                                                                    \n \
                     Container Cleaner V 1.1                                        \n\n")                                                                             
print(Style.RESET_ALL)
print("\n\n")


script.warn_msg("THIS SCRIPT MAY KILL AND DELETE CONTAINERS/IMAGES WITHOUT CONFIRMATION.")
print("\n\n")


# No need to implement further if config file exists checks here as it will fail on line 31
# Could be worth implementing additional sanity checks for other variables as the config complexity grows

if CONTAINER_ENGINE == "docker_compose":
    # Run git pull
    if GIT_ENABLED == True:
        git_pulled = git.git_pull(GIT_REPO_PATH)

    if NTFY_ENABLED == True and git_pulled == False:
        ntfy.ntfy_warn_git_pull_fail()
        

    # Run docker compose pull
    docker_compose.docker_compose_pull(COMPOSE_FILE)
    

    # Run docker compose recreate
    docker_compose.docker_compose_recreate(COMPOSE_FILE)


    # Cleanup all unused docker images
    docker.docker_delete_unused_images()



elif CONTAINER_ENGINE == "docker":
    script.err_msg("Standalone docker support has not yet been implemented. Please view Readme.")
    ntfy.ntfy_err_invalid_container_engine()

    # Run git pull
    # Docker pull each image in list
    # Docker get list of containers
    # Docker stop all containers, wait for a bit, then kill
    # Docker start all containers

    # Cleanup all unused docker images
    #docker.docker_delete_unused_images()


elif CONTAINER_ENGINE == "podman":
    script.err_msg("Standalone podman support has not yet been implemented. Please view Readme.")
    ntfy.ntfy_err_invalid_container_engine()

    # Run git pull
    # Docker pull each image in list
    # Docker get list of containers
    # Docker stop all containers, wait for a bit, then kill
    # Docker start all containers

    # Cleanup all unused docker images
    #docker.docker_delete_unused_images()


else:
    script.err_msg("Invalid Configuration. Please review config.ini and README.")
    ntfy.ntfy_err_invalid_config()



print("\n\n\n")
script.ok_msg("Finished! Exiting...")
ntfy.ntfy_ok_run_complete()

exit()
