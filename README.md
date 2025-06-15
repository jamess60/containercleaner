
# ContainerCleaner

---

## 📖 About

**ContainerCleaner** is a port of my CERN project, *PodmanCleaner*. It runs automatically via **cron** or **systemd**, and can:

- Optionally pull a git repository
- Pull the latest container images
- Recreate Docker Compose or Docker Swarm containers
- Remove unused images

This helps:

- Keep storage use to a minimum on the host
- Ensure all services are up-to-date
- Prevent hung processes or stale containers

Currently supports **Docker Compose** and **Docker Swarm** only. Future support for Podman, Kubernetes, or standalone Docker may be added based on demand.

---

## ⚙️ How to Install

> 🐧 These instructions assume a **Debian-based distro** (e.g., Ubuntu, Mint, Pop!_OS). 

### 1. Install required system packages:

```bash
sudo apt update && sudo apt install -y git curl python3 python3-pip
```

### 2. Install required Python modules:

Via **APT**:
```bash
sudo apt install -y python3-colorama python3-git python3-docker python3-requests python3-yaml
```

Or via **pip**:
```bash
pip install colorama gitpython docker requests pyyaml
```

### 3. Clone and enter the repository:

```bash
cd /usr/share/ && sudo git clone https://github.com/jamess60/containercleaner.git && cd containercleaner
```

### 4. Configure containercleaner (Refer to section below for more help):

```bash
sudo nano /usr/share/containercleaner/conf/config.ini
```

```bash
sudo nano /usr/share/containercleaner/src/functions/ntfy.py
```

### 5. Manually test the script:

```bash
python3 /usr/share/containercleaner/src/ContainerCleaner.py
```

### 6. Enable the systemd timer:

```bash
sudo cp /usr/share/containercleaner/conf/systemd/* /etc/systemd/system/ && sudo systemctl daemon-reload && sudo systemctl enable containercleaner.timer
```

---

### 📝 Additional Install Notes:

- If you prefer **cron**, an example is provided in `conf/ContainerCleaner.cron`.
- To change the timer frequency, edit `conf/systemd/containercleaner.timer` before copying it.
- **Running both `docker_compose` and `docker_swarm` modes in the same instance is not supported**. Use separate instances if needed.
- If you are running containercleaner in a none defualt location (anywhere other than /usr/share/containercleaner), you will need to modify line 10 in src/functions/ntfy.py and line 29 in ContainerCleaner.py to reflect the new location of the config file.

---


### 🧾 Configuration Keys Explained


#### conf/config.ini
| Section        | Key              | Description                                                                 | Value(s) / Example                           | Notes                                                              |
|----------------|------------------|-----------------------------------------------------------------------------|----------------------------------------------|--------------------------------------------------------------------|
| MAIN           | CONTAINER_ENGINE | Choose which container engine you are running                               | docker_compose OR docker_swarm               |                                                                    |
| DOCKER_COMPOSE | COMPOSE_FILES    | Specify the path(s) to the compose file(s) you wish to automatically update | /root/containers/compose_files/webserver.yml | Can be left blank if not using docker_compose for CONTAINER_ENGINE |
| DOCKER_SWARM   | SWARM_FILES      | Specify the path(s) to the swarm file(s) you wish to automatically update   | /root/containers/swarm_files/webserver.yml   | Can be left blank if not using docker_swarm for CONTAINER_ENGINE   |
| GIT            | GIT_ENABLED      | Disable or Enable pulling git repos before compose/swarm files are updated. | True OR False                                |                                                                    |
| GIT            | GIT_REPO_PATHS   | Paths to Dirs which are git managed                                         | /root/containers                             | Can be left blank if Git is disabled                               |
| NTFY           | NTFY_ENABLED     | Disable or Enable sending notifications to an Ntfy server                   | True OR False                                |                                                                    |
| NTFY           | NTFY_HOST        | Ntfy server URL                                                             | https://ntfy.yourdomain.co.uk                | Can be left blank if Ntfy is disabled                              |
| NTFY           | NTFY_TOPIC       | Ntfy server topic                                                           | ContainerCleaner                             | Can be left blank if Ntfy is disabled                              |





---

## ❓ FAQ

**1. The script says "This script may KILL and DELETE containers without confirmation" – is that true?**  
👉 It only kills/recreates containers the same way `docker compose up -d` or `docker stack deploy` would. No containers are stopped unless they need to be updated. This is the only way to rebase a container on to a new image, and alternative tools (such as Watchtower) would do the same. 

**2. Why not just use a one-liner bash script?**  
👉 That would limit future features like `ntfy` integration, config parsing, and Swarm support.

**3. Isn't this basically Watchtower with extra steps?**  
👉 Sort of — but Watchtower can be slow to recreate containers and doesn’t always clean up old images.  
ContainerCleaner is a faster, more secure alternative that avoids using `docker.sock` directly.

**4. I use Docker Swarm — where should I run this?**  
👉 Run it on **one manager node** only. Worker nodes can’t deploy stacks.  
If you want redundancy, install it on **two manager nodes**, spacing their timers at least an hour apart.

---

## 🌟 Feature Wishlist
- [ ] Dry run/simulation mode
- [ ] Full logging support
- [ ] Multi-repo & multi-file support
- [ ] Packaging as `.deb`, `.rpm`
- [ ] Explore ContainerCleaner as a container (although this would negate the no touching docker.sock benefit)
- [ ] Improved validation and sanity checks
- [ ] Alternative notification services (such as Discord/Telegram)


---

![screenshot](https://resources.jamesmaple.co.uk/downloads/gitimg/containercleaner/readme-screenshot.png)
