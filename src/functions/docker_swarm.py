import os
import os.path
import yaml
from functions import script





def docker_swarm_extract_imagenames_from_swarm_file(SWARM_FILE):
    try:
        with open(SWARM_FILE, 'r') as f:
            data = yaml.safe_load(f)
    except Exception as e:
        print(f"Failed to load YAML file: {e}")
        return []

    images = []
    services = data.get("services", {})

    for service_name, service_config in services.items():
        image = service_config.get("image")
        if image:
            images.append(image)

    return images



def docker_swarm_pull_images(image_list):
    print("\n")
    script.info_msg("Attempting to pull images used by this Docker Swarm stack...\n")

    all_success = True

    for image in image_list:
        print(f"Pulling: {image}")
        result = os.system(f"docker pull {image}")
        if result != 0:
            script.err_msg(f"Failed to pull image: {image}")
            all_success = False
        else:
            script.ok_msg(f"Pulled image: {image}")

    print("\n")
    if all_success:
        script.ok_msg("All images pulled successfully.")
    else:
        script.err_msg("One or more image pulls failed.")



def docker_swarm_recreate(SWARM_FILE):
    # Derive stack name from the SWARM_FILE
    stack_name = os.path.splitext(os.path.basename(SWARM_FILE))[0]

    print("\n")
    script.info_msg(f"Attempting to re-deploy Docker stack '{stack_name}' with swarm file {SWARM_FILE} ...")
    print("\n")

    try:
        deploy_cmd = f"docker stack deploy -c {SWARM_FILE} {stack_name} --detach=false"
        os.system(deploy_cmd)
        deploy_success = True
    except Exception as e:
        deploy_success = False

    print("\n\n")
    if deploy_success:
        script.ok_msg("Docker Swarm stack deploy OK! Services should be updating.")
    else:
        script.err_msg("Docker Swarm stack deploy FAILED! Services may not be up.")