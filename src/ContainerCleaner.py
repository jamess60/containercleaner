#!/usr/bin/env python3

__author__ = "james_s60"
__date__ = "05 August 2024"
__credits__ = ["james_s60"]
__version__ = "1.0.1"


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
CONTAINER_ENGINE = config['MAIN']['CONTAINER_ENGINE']
# Docker Compose
COMPOSE_FILE = config['DOCKER_COMPOSE']['COMPOSE_FILE']
# Git
GIT_ENABLED = str(config['GIT']['GIT_ENABLED'])
GIT_REPO_PATH = str(config['GIT']['GIT_REPO_PATH'])

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
                     Container Cleaner V 1.0                                        \n\n")                                                                             
print(Style.RESET_ALL)
print("\n\n")


script.warn_msg("THIS SCRIPT MAY KILL AND DELETE CONTAINERS/IMAGES WITHOUT CONFIRMATION.")
print("\n\n")


if CONTAINER_ENGINE == "docker_compose":
    # Run git pull
    if GIT_ENABLED == "true":
        git.git_pull(GIT_REPO_PATH)
        

    # Run docker compose pull
    docker_compose.docker_compose_pull(COMPOSE_FILE)
    

    # Run docker compose recreate
    docker_compose.docker_compose_recreate(COMPOSE_FILE)


    # Cleanup all unused docker images
    docker.docker_delete_unused_images()



elif CONTAINER_ENGINE == "docker":
    script.err_msg("Standalone docker support has not yet been implemented. Please view Readme.")

    # Run git pull
    # Docker pull each image in list
    # Docker get list of containers
    # Docker stop all containers, wait for a bit, then kill
    # Docker start all containers

    # Cleanup all unused docker images
    #docker.docker_delete_unused_images()


elif CONTAINER_ENGINE == "podman":
    script.err_msg("Standalone podman support has not yet been implemented. Please view Readme.")

    # Run git pull
    # Docker pull each image in list
    # Docker get list of containers
    # Docker stop all containers, wait for a bit, then kill
    # Docker start all containers

    # Cleanup all unused docker images
    #docker.docker_delete_unused_images()


else:
    script.err_msg("Invalid Configuration. Please review config.ini and README.")


print("\n\n\n")
script.ok_msg("Finished! Exiting...")

exit()
