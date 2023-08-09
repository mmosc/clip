import zipfile
import pandas as pd
CLIP_PATH = '/home/marta/jku/clip/'
DATA_PATH = '/home/marta/jku/clip/data/mpd/'
#%%
# Extract test set
with zipfile.ZipFile(f'{CLIP_PATH}/spotify_million_playlist_dataset_challenge.zip', 'r') as zip_ref:
    zip_ref.extractall(f'{DATA_PATH}/raw_files/')
#%%
test_set = pd.read_json(f'{DATA_PATH}/raw_files/challenge_set.json')
#%%
test_set = test_set.drop(columns=['date', 'version', 'description', 'name'])

#%%
test_set_df = pd.DataFrame(list(test_set['playlists'])).set_index('pid')
print(test_set_df.tail(1).tracks)
#%%
#test_set_df = test_set_df[['name', 'tracks']]
print(test_set_df.head())
#%%