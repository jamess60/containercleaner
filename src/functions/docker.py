import docker # apt install python3-docker
from functions import script




def docker_delete_unused_images():
    print("\n")
    script.info_msg("Attempting to wipe unused images...")
    # Connect to Docker Daemon and extract images/containers
    try:    
        client = docker.from_env()
        all_images = client.images.list()
        all_containers = client.containers.list()

        # Extract image IDs from running containers
        used_image_ids = {container.image.id for container in all_containers}

        docker_connected = True
    except:
        docker_connected = False


    if docker_connected == True:
        script.ok_msg("Connected to Docker Daemon!")
    else:
        script.err_msg("Failed to connect to Docker Daemon! - Cannot delete unused images!")
        


    # Iterate through all images and delete those which are not used by any container
    for image in all_images:
        if image.id not in used_image_ids:
            try:
                # Delete the image
                client.images.remove(image.id, force=True)
                print(f"Deleted image {image.id}")
            except docker.errors.APIError as e:
                print(f"Error deleting image {image.id}: {e}")


    script.ok_msg("No unused images")










