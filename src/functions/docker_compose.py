import os
from functions import script





def docker_compose_pull(COMPOSE_FILE):
    print("\n")
    script.info_msg("Attempting to pull new docker images...")
    print("\n")

    try:
        compose_pull_cmd = "docker compose -f " + COMPOSE_FILE + " pull"
        os.system(compose_pull_cmd)
        docker_compose_pulled = True
    except:
        docker_compose_pulled = False

    print("\n\n")
    if docker_compose_pulled == True:
        script.ok_msg("Docker Compose Pull OK!")
    if docker_compose_pulled == False:
        script.err_msg("Docker Compose Pull Failed!")




def docker_compose_recreate(COMPOSE_FILE):
    print("\n")
    script.info_msg("Attempting to bring up compose file...")
    print("\n")

    try:
        compose_recreate_cmd = "docker compose -f " + COMPOSE_FILE + " up -d --remove-orphans"
        os.system(compose_recreate_cmd)
        docker_compose_pulled = True
    except:
        docker_compose_pulled = False
    
    print("\n\n")
    if docker_compose_pulled == True:
        script.ok_msg("Docker Compose recreate OK! - Containers should be up.")
    elif docker_compose_pulled == False:
        script.err_msg("Docker Compose recreate Failed! - Containers may not be up!")
