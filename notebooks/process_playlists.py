import pandas as pd

def get_playlist_metrics(df: pd.core.frame.DataFrame):
    def get_statistic(f) -> pd.core.frame.DataFrame:
        return df.apply(f).to_frame().transpose()

    assert isinstance(df, pd.core.frame.DataFrame)
    result = pd.concat({"min" : get_statistic(pd.Series.min),
                        "q1" : get_statistic(lambda x: x.quantile(0.25)),
                        "mean" : get_statistic(pd.Series.mean),
                        "median" : get_statistic(pd.Series.median),
                        "q3" : get_statistic(lambda x: x.quantile(0.75)),
                        "max" : get_statistic(pd.Series.max),
                        "standard deviation" : get_statistic(pd.Series.std),
                        "variance" : get_statistic(pd.Series.var)}, axis=1)
    
    result.columns = result.columns.swaplevel(0, 1)
    result.sort_index(axis=1, level=0, inplace=True)
    return result

def process_playlists(playlist_data, audio_features, start_index, end_index, pid):
    local_playlists_metrics = pd.DataFrame()

    for i in range(start_index, end_index):
        playlist = playlist_data[i]

        playlist_features = pd.DataFrame(columns=audio_features.columns.tolist())
        new_index = pd.Index.union(playlist_features.index, playlist['track_ids'])
        playlist_features = playlist_features.reindex(new_index)

        # Add track information to features table
        for j, track_id in enumerate(playlist["track_ids"]):
            if track_id not in audio_features.index:
                print(f'Playlist {playlist["pid"]} : missing audio features for track {j}/{playlist["num_tracks"]} with id = {track_id}')
                continue

            track_features = pd.DataFrame(audio_features.loc[track_id]).T
            playlist_features = pd.concat([playlist_features if not playlist_features.empty else None, track_features], axis=0)

        # Use features table to get metrics
        playlist_info = pd.DataFrame(data={k: [v] for k, v in playlist.items() if k != "track_ids"})
        playlist_info.columns = pd.MultiIndex.from_product([['metadata'], playlist_info.columns])
        playlist_metrics = pd.concat([playlist_info, get_playlist_metrics(playlist_features)], axis=1)

        local_playlists_metrics = pd.concat([local_playlists_metrics, playlist_metrics], ignore_index=True)

        if i % 10 == 0:
            i_normalized = i - start_index
            print(f'[{pid}]: {i_normalized / (end_index - start_index) * 100:>5.1f}% ({i_normalized:>5}/{end_index - start_index:>5})', end='\r')

    return local_playlists_metrics