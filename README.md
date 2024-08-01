ContainerCleaner
=========================


About
-----------------
ContainerCleaner is a port of my CERN Project, PodmanCleaner. It runs automatically, via cron, and will pull the git repo, pull the latest container images, recreate the compose file containers and remove any old images. 

This keeps storage use to a minimum on the host, ensures all services are up to date and prevents any hung processes/containers remaining active.    

It currently only supports docker compose setups, but I may restore support for standalone docker/podman setups in future versions if there is enough demand.

______________________

How to use
---------------------
Tool does not accept any args, runs automatically via cron. Please ensure conf/config.ini is present and correct.

Required pip packages: colorama, configparser, git, docker 

1) Git clone this repo to /usr/share
2) edit /conf/config.ini to set your compose file path, git enable/disable etc
3) edit /conf/ContainerCleaner.cron to make it run at your chosen time(s). Runs at 2am daily by default
4) cp conf/ContainerCleaner.cron /etc/cron.d/
5) systemctl daemon-reload
6) To test manually - python3 src/ContainerCleaner.py

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

![screenshot]([http://url/to/img.png](https://jamesmaple.co.uk/downloads/gitimg/containercleaner/readme-screenshot.png))
