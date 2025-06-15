import requests
import socket
from configparser import ConfigParser 


############################
# Parse NTFY Config
############################
config = ConfigParser()
config.read('/usr/share/containercleaner/conf/config.ini')

NTFY_HOST = str(config['NTFY']['NTFY_HOST'])
NTFY_TOPIC = str(config['NTFY']['NTFY_TOPIC'])
############################


hostname = str(socket.gethostname())



def ntfy_err_invalid_config():
	requests.post(NTFY_HOST + "/" + NTFY_TOPIC,
	    data="Run failed on " + hostname + " - Invalid config file",
	    headers={
	        "Title": "ContainerCleaner",
	        "Priority": "urgent",
	        "Tags": "x,pensive"
	    })



def ntfy_err_invalid_container_engine():
	requests.post(NTFY_HOST + "/" + NTFY_TOPIC,
    data="Run failed on " + hostname + " - Invalid container engine. Sanity check config file.",
    headers={
        "Title": "ContainerCleaner",
        "Priority": "urgent",
        "Tags": "x,pensive"
    })



def ntfy_warn_git_pull_fail():
	requests.post(NTFY_HOST + "/" + NTFY_TOPIC,
    data="Warning on " + hostname + " - Some/All git pulls failed. Proceeding with local copy. Please manually issue a git pull (and resolve issues) on each repo.",
    headers={
        "Title": "ContainerCleaner",
        "Priority": "high",
        "Tags": "exclamation,raised_eyebrow"
    })



def ntfy_ok_run_complete():
	requests.post(NTFY_HOST + "/" + NTFY_TOPIC,
    data="Run complete on " + hostname,
    headers={
        "Title": "ContainerCleaner",
        "Priority": "default",
        "Tags": "white_check_mark,slightly_smiling_face"
    })	




# ✅🙂 - "Tags": "white_check_mark,slightly_smiling_face"
# ❗🤨 - "Tags": "exclamation,raised_eyebrow"
# ❌😔 - "Tags": "x,pensive"
# https://docs.ntfy.sh/emojis/

# Priorities: urgent (5), high (4), default (none) (3), low (2), min (1)
# https://docs.ntfy.sh/publish/






















