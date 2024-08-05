



# Placeholder file












# print("\n\nStopping all containers gracefully...")
# os.system("podman stop -a")

# print("\n\nSleeping for 15 seconds before killing hung containers.")
# time.sleep(15)

# print("\n\nKilling any remaining containers...")
# os.system("podman kill -a")

# print("\n\nRemoving all containers...")
# os.system("podman rm --all --force")

# print("\n\nRemoving all images...")
# os.system("podman rmi --all --force")

# print("\n\nRemoving all Podman data...")
# os.system("podman system prune --all --force")








# import subprocess
# import paramiko
# from functions import script
# from functions import ssh



# def is_docker_installed():
#     print(script.info_msg("Checking if Docker is installed..."))

#     try:
#         subprocess.check_output(["docker", "--version"])
#         docker_installed = True
#     except subprocess.CalledProcessError:
#         docker_installed = False

#     if docker_installed == True:
#         print(script.info_msg("Docker is installed.\n\n"))
#         return True
#     else:
#         print(script.info_msg("Docker is not installed.\n\n"))

#         return False



# def is_podman_installed():
#     print(script.info_msg("Checking if Podman is installed..."))
#     try:
#         subprocess.check_output(["podman", "--version"])
#         podman_installed = True
#     except subprocess.CalledProcessError:
#         podman_installed = False

#     if podman_installed == True:
#         print(script.info_msg("Podman is installed.\n\n"))
#         return True
#     else:
#         print(script.info_msg("Podman is not installed.\n\n"))
#         return False



# def kill_and_delete_docker_containers():
#     print(script.info_msg("Attempting to kill and remove all Docker containers..."))

#     ls_cont_cmd = "docker ps -aq"   
#     container_ids = subprocess.check_output(ls_cont_cmd, shell=True).decode().strip().split('\n')

#     if len(container_ids) == 1: 
#         print(script.ok_msg("No containers to stop and remove.\n\n"))
#     else:  
#         for container_id in container_ids:
#             stop_cmd = f"docker stop {container_id}"
#             subprocess.run(stop_cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#             remove_cmd = f"docker rm -f {container_id}"
#             subprocess.run(remove_cmd, shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#             print(f"Container {container_id} stopped and removed.") # Cant easily implement ok_msg here...
#         print("\n\n")




# def kill_and_delete_podman_containers():
#     print(script.info_msg("Attempting to kill and remove all Podman containers..."))

#     subprocess.run('podman kill -a', shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)
#     subprocess.run('podman rm -f -a', shell=True, check=True, stdout=subprocess.DEVNULL, stderr=subprocess.DEVNULL)

#     print(script.ok_msg("Containers stopped and removed.\n\n"))





# def is_docker_installed_remote(RECOVERY_HOST):
#     print(script.info_msg("Checking if Docker is installed..."))

#     cmdout, cmderr = ssh.run_ssh_cmd(RECOVERY_HOST, "docker --version")

#     if "Docker version " in cmdout:
#         print(script.info_msg("Docker is installed.\n\n"))
#         return True
#     else:
#         print(script.info_msg("Docker is not installed.\n\n"))
#         return False



# def is_podman_installed_remote(RECOVERY_HOST):
#     print(script.info_msg("Checking if Podman is installed..."))

#     cmdout, cmderr = ssh.run_ssh_cmd(RECOVERY_HOST, "podman --version")

#     if "podman version " in cmdout:
#         print(script.info_msg("Podman is installed.\n\n"))
#         return True
#     else:
#         print(script.info_msg("Podman is not installed.\n\n"))
#         return False



# def kill_and_delete_docker_containers_remote(RECOVERY_HOST):
#     print(script.info_msg("Attempting to kill and remove all Docker containers..."))
#     sshcmd1 = "docker stop $(docker ps -aq)"
#     sshcmd2 = "docker rm $(docker ps -aq)"
#     ssh.run_ssh_cmd(RECOVERY_HOST, sshcmd1)
#     ssh.run_ssh_cmd(RECOVERY_HOST, sshcmd2)
#     print(script.ok_msg("Containers stopped and removed.\n\n"))


# def kill_and_delete_podman_containers_remote(RECOVERY_HOST):
#     print(script.info_msg("Attempting to kill and remove all Podman containers..."))
#     sshcmd1 = "podman kill -a"
#     sshcmd2 = "podman rm -a"
#     ssh.run_ssh_cmd(RECOVERY_HOST, sshcmd1)
#     ssh.run_ssh_cmd(RECOVERY_HOST, sshcmd2)
#     print(script.ok_msg("Containers stopped and removed.\n\n"))

