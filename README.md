# Spotifeature

> *Spotifeature* is a project for the [Data Wrangling](https://studiegids.vu.nl/en/Minor/2023-2024/data-science/XB_0014#/) course @ Vrije Universiteit Amsterdam aiming to investigate possible relations between audio features of a playlist and playlist metadata (e.g., popularity measured in followers). The [project report](project_report.pdf) outlines the findings of the research.

## Notebooks
The code for this project is distributed over multiple notebooks as many parts can be seen as individual (isolated) steps. 

### Pre-Tasks
- [`visualization_initial.ipynb`](notebooks/visualization_initial.ipynb) is used for gaining a first understanding of the dataset based on which further decisions (e.g., the minimum followers threshold) are based. The notebook offers tools for generating

### Acquisition & Cleaning
- [`acquisition_playlists.ipynb`](notebooks/acquisition_playlists.ipynb) is used for processing the initial dataset (1,000,000 public Spotify playlists).
The notebook can be used to create 2 different outputs:
    1. The original dataset, stripped of some (unneeded) playlist attributes, serialized as a Python pickle file.
    2. A list of all unique track IDs (used for audio feature acquisition), also as a Python pickle file.

- [`acquisition_features.ipynb`](notebooks/acquisition_features.ipynb) is used for building a dataset of audio features for the track IDs identified in the previous notebook. The resulting dataset is saved as a `csv` file.

### Processing
- [`processing.ipynb`](notebooks/processing.ipynb) (with [`process_playlist.py`](notebooks/process_playlists.py)) is used for generating playlist metrics based on the audio features. The results are stored serialized in a Python pickle file.

### Visualization
- [`data_visualizatoin.ipynb`](notebooks/data_visualization.ipynb) is used to generate all graphs used for feature trend discovery according to the research questions, and the individual graphs used for the report/presentation.

## Data
As most of the generated (intermediate) data is substantial in size, the files are stored separately in a [Google Drive Folder](https://drive.google.com/drive/folders/1uozdLI_VAu_U0oygjIEomJ1-8po1eavS?usp=sharing).


## Authors
| Name | Profile |
|---|---|
| Lennart K.M. Schulz | [GitHub](https://github.com/lkm-schulz), [LinkedIn](https://www.linkedin.com/in/lkm-schulz/) |
| Laura I.M. Stampf | [GitHub](https://github.com/laustam), [LinkedIn](https://www.linkedin.com/in/laura-stampf/) |
| Dovydas Vadišius | [GitHub](https://github.com/DovydasVad), [LinkedIn](https://www.linkedin.com/in/dovydas-vadisius/) |