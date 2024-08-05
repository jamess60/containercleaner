import git  # pip install gitpython or apt install python3-git
from functions import script



def git_pull(GIT_REPO_PATH):
    script.info_msg("Attempting to run Git Pull...")
    try:
        repo = git.Repo(GIT_REPO_PATH)
        repo.remotes.origin.pull()
        git_pulled = True
    except:
        git_pulled = False

    if git_pulled == True:
        script.ok_msg("Git Pull OK!")

    if git_pulled == False:
        script.err_msg("Git Pull Failed!")

