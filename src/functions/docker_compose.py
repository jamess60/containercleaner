import os
from functions import script





def docker_compose_pull(COMPOSE_FILE):
    print("\n")
    script.info_msg("Attempting to pull new docker images for " + str(COMPOSE_FILE) + " ...")
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
    script.info_msg("Attempting to bring up compose file " + str(COMPOSE_FILE) + " ...")
    print("\n")

    try:
        # Extract the project name from the filename (without extension)
        project_name = os.path.splitext(os.path.basename(COMPOSE_FILE))[0]

        # Include -p to set the project name dynamically
        compose_recreate_cmd = f"docker compose -p {project_name} -f {COMPOSE_FILE} up -d"
            # --remove-orphans" - Remove orphans breaks multi compose file mode
            # -p added so portainer recognises each yml as a stack

        os.system(compose_recreate_cmd)
        docker_compose_pulled = True
    except Exception as e:
        docker_compose_pulled = False
        script.err_msg(f"Exception: {e}")
    
    print("\n\n")
    if docker_compose_pulled:
        script.ok_msg("Docker Compose recreate OK! - Containers should be up.")
    else:
        script.err_msg("Docker Compose recreate Failed! - Containers may not be up!")


