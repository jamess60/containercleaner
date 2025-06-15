Changelog
---------------------
## V1.2
	- Improved readme installation steps and added section explaining config file
	- Fixed missing screenshot in readme 
	- Removed all traces of podman & docker standalone support as this is unlikely to be implemented in the near future
		- Little benefit/sustainability to auto updates on adhoc single containers + podman has single digit marketshare
	- Fixed a path inconsistency bug ("containercleaer" vs "ContainerCleaner") causing configs to fail to load
	- Fixed a bug where the script would fail to run if Ntfy was disabled (as Ntfy did not always respect disabled parameter and tried to push anyway)
	- Added support for pulling multiple git repos 
	- Added support for running multiple yml files 
	- Added support for Docker Swarm


## V1.1.1
	- Tweaked formatting of Ntfy notifications to make them more iOS friendly



## V1.1
	- Updated readme 
	- Implemented support for Ntfy notifications
	- Removed email notifications from the feature wish list for the moment (Ntfy can handle this), may re-add if there is demand	


## V1.0.1
	- Update readme 
	- Remove some debug print statements that slipped through
	- Added systemd timer and service, updated README to reflect that this is prefered over cron	


## V1.0
	- Refactor of CERN version
		- Removed CERN Mail
		- Removed SelfCheck
	- Removed from manual podman support in favour of docker compose
	- Added configParser to enable git pulling
	- Branched from single file to main+library

______________________


