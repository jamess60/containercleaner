import git
from functions import script



def git_pull(GIT_REPO_PATHS):
    script.info_msg("Attempting to run Git Pull(s)...")

    all_success = True


    for GIT_REPO_PATH in GIT_REPO_PATHS:
        try:
            repo = git.Repo(GIT_REPO_PATH)
            repo.remotes.origin.pull()
            script.ok_msg("Git Pull OK! (" + str(GIT_REPO_PATH) + ")")
        except:
            all_success = False
            script.err_msg("Git Pull Failed! (" + str(GIT_REPO_PATH) + ")")


    return all_success

