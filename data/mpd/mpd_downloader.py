import subprocess
# https://www.aicrowd.com/showcase/download-dataset-in-colab-notebook-via-cli
# https://stackoverflow.com/questions/4256107/running-bash-commands-in-python

API_KEY = "ce7a5bbf41c4ecb6624ad806ff98497e"
subprocess.run(f"aicrowd login --api-key {API_KEY}", shell=True)
#%%
subprocess.run(f"aicrowd dataset list --challenge spotify-million-playlist-dataset-challenge", shell=True)
#%%
subprocess.run("aicrowd dataset download --challenge spotify-million-playlist-dataset-challenge 0 1", shell=True)
#%%