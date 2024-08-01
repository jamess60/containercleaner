ContainerCleaner
=========================


About
-----------------
ContainerCleaner is a port of my CERN Project, PodmanCleaner. It runs automatically, via cron, and will pull the git repo, pull the latest container images, recreate the compose file containers and remove any old images. 

This keeps storage use to a minimum on the host, ensures all services are up to date and prevents any hung processes/containers remaining active.    

It currently only supports docker compose setups, but I may restore support for standalone docker/podman setups in future versions if there is enough demand.

______________________

How to Install
---------------------

1) Ensure you have the required pip packages
Debian: `sudo apt install python3-colorama python3-git python3-docker`
pip: `pip install colorama git docker`

2) Clone the git repo 
`cd /usr/share/ && git clone https://github.com/jamess60/containercleaner.git`

3) Edit conf/config.ini and add the file path for your docker compose file
`nano config/config.ini`

4) Optional - If you do not wish for the script to run daily at 2am (default), Edit conf/ContainerCleaner.cron and change the cron value
`nano config/ContainerCleaner.cron`

5) Manually test the script works as expected 
`python3 /usr/share/ContainerCleaner/src/ContainerCleaner.py`

6) Enable cron
`sudo cp config/ContainerCleaner.cron /etc/cron.d/ && sudo systemctl daemon reload`
______________________


Changelog
---------------------
## V1.0
	- Refactor of CERN version
		- Removed CERN Mail
		- Removed SelfCheck
	- Removed from manual podman support in favour of docker compose
	- Added configParser to enable git pulling
	- Branched from single file to main+library

______________________


FAQ
---------------------
1. The script says "This script may KILL and DELETE containers without confirmation" - NOPE!
	- The only way to move a container to a new image is to stop the container and start it again. The only time a container will be killed is if the docker compose command would "recreate". Watchtower would do the same.
2. Why isn't this just a one liner bash script?
	- While that would be possible in v1, it would limit future feature set expansion
3. Isn't this basically watchtower with extra steps?
	- Kinda sorta but not really. Watchtower pulls new images, but is slow to recreate the container (sometimes multiple days in my case). It also doesn't always reliably remove unused images. Container cleaner doesn't directly touch docker.sock which can also be advantageous for security reasons. I wrote this to be a faster/more reliable lightweight alternative with the potential to expand features later.




______________________


Feature wishlist
---------------------
- Implement support for standalone docker
- Implement support for podman 
- Add an argument to generate a template config file 
- Add a dry run/simulation mode (doesn't make any changes)
- Implement proper logging support 
- Implement Email notifications
- Implement Ntfy notifications
- Implement support for running with multiple git repos and compose files 
- Explore options to package this as a deb, rpm, pip install etc 
______________________

![screenshot](https://jamesmaple.co.uk/downloads/gitimg/containercleaner/readme-screenshot.png)
