# Spotifeature

> *Spotifeature* is a project as part of the Data Wrangling course @ VU Amsterdam aiming to investigate possible relations between audio features of a playlist and playlist metadata (e.g., popularity measured in followers).

## Notebooks
The code for this project is distributed over multiple notebooks as many parts can be seen as individual (isolated) steps. 

### Pre-Tasks
- `visualization_initial.ipynb` is used for gaining a first understanding of the dataset based on which further decisions (e.g., the minimum followers threshold) are based. The notebook offers tools for generating

### Acquisition & Cleaning
- `acquisition_playlists.ipynb` is used for processing the initial dataset (1,000,000 public Spotify playlists).
The notebook can be used to create 2 different outputs:
    1. The original dataset, stripped of some (unneeded) playlist attributes, serialized as a Python pickle file.
    2. A list of all unique track IDs (used for audio feature acquisition), also as a Python pickle file.

- `acquisition_features.ipynb` is used for building a dataset of audio features for the track IDs identified in the previous notebook. The resulting dataset is saved as a `csv` file.

### Processing
- `processing.ipynb` (with `process_playlist.py`) is used for generating playlist metrics based on the audio features. The results are stored serialized in a Python pickle file.

### Visualization
- `data_visualizatoin.ipynb` is used to generate all graphs used for feature trend discovery according to the research questions, and the individual graphs used for the report/presentation.

## Data
As most of the generated (intermediate) data is substantial in size, the files are stored separately in a [Google Drive Folder](https://drive.google.com/drive/folders/1uozdLI_VAu_U0oygjIEomJ1-8po1eavS?usp=sharing).