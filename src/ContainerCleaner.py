#!/usr/bin/env python3

__author__ = "james_s60"
__date__ = "13 September 2025"
__credits__ = ["james_s60"]
__version__ = "1.3"


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
from functions import docker
from functions import docker_compose
from functions import docker_swarm
############################


############################
# Parse Config
############################
config = ConfigParser()
config.read('/usr/share/containercleaner/conf/config.ini')
# Main
CONTAINER_ENGINE = str(config['MAIN']['CONTAINER_ENGINE'])
# Docker Compose
COMPOSE_FILES = [line.strip() for line in config.get('DOCKER_COMPOSE', 'COMPOSE_FILES').splitlines() if line.strip()]
# Docker Swarm
SWARM_FILES = [line.strip() for line in config.get('DOCKER_SWARM', 'SWARM_FILES').splitlines() if line.strip()]
# Git
GIT_ENABLED = config['GIT'].getboolean('GIT_ENABLED')
GIT_REPO_PATHS = [line.strip() for line in config.get('GIT', 'GIT_REPO_PATHS').splitlines() if line.strip()]
# Ntfy
NTFY_ENABLED = config['NTFY'].getboolean('NTFY_ENABLED')
    # For config options such as Ntfy host and topic, please see src/functions/ntfy.py!


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
                     Container Cleaner V 1.3                                        \n\n")                                                                             
print(Style.RESET_ALL)
print("\n\n")


script.warn_msg("THIS SCRIPT MAY KILL AND DELETE CONTAINERS/IMAGES WITHOUT CONFIRMATION.")
print("\n\n")



# Run git pull
git_pulled = True  # Default to True in case GIT is disabled, prevents missing var error
if GIT_ENABLED == True:
    git_pulled = git.git_pull(GIT_REPO_PATHS)
if NTFY_ENABLED == True and git_pulled == False:
    ntfy.ntfy_warn_git_pull_fail()



if CONTAINER_ENGINE == "docker_compose":
    # Run docker compose pull
    for COMPOSE_FILE in COMPOSE_FILES:
        docker_compose.docker_compose_pull(COMPOSE_FILE)

    # Run docker compose recreate
    for COMPOSE_FILE in COMPOSE_FILES:
        docker_compose.docker_compose_recreate(COMPOSE_FILE)

    # Cleanup all unused docker images
    docker.docker_delete_unused_images()



elif CONTAINER_ENGINE == "docker_swarm":
    # For each Swarm file:
    for SWARM_FILE in SWARM_FILES:
        # Extract images and pull them
        images = docker_swarm.docker_swarm_extract_imagenames_from_swarm_file(SWARM_FILE)
        docker_swarm.docker_swarm_pull_images(images)

        # Recreate the Swarm stack
        docker_swarm.docker_swarm_recreate(SWARM_FILE)

    # Cleanup all unused docker images
    docker.docker_delete_unused_images()



else:
    script.err_msg("Invalid Configuration. Please review config.ini and README.")

    if NTFY_ENABLED == True:
        ntfy.ntfy_err_invalid_config()





print("\n\n\n")
script.ok_msg("Finished! Exiting...")
if NTFY_ENABLED == True:
        ntfy.ntfy_ok_run_complete()

exit()
