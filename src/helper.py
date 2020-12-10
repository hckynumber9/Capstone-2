def seasons(df, filtered_df):
    

    # now calc cumulative stats
    filtered['gpg'] = (filtered.groupby('team_id')['goals'].cumsum() - filtered['goals']) /           filtered.groupby('team_id').cumcount()
    filtered['win_per'] = (filtered.groupby('team_id')['won'].cumsum() - filtered['won']) / filtered.groupby('team_id').cumcount()
    filtered['shots_pg'] = (filtered.groupby('team_id')['shots'].cumsum() - filtered['shots']) / filtered.groupby('team_id').cumcount()
    filtered['hits_pg'] = (filtered.groupby('team_id')['hits'].cumsum() - filtered['hits']) / filtered.groupby('team_id').cumcount()
    filtered['pim_pg'] = (filtered.groupby('team_id')['pim'].cumsum() - filtered['pim']) / filtered.groupby('team_id').cumcount()
    filtered['hits_pg'] = (filtered.groupby('team_id')['hits'].cumsum() - filtered['hits']) / filtered.groupby('team_id').cumcount()
    filtered['fo_per'] = (filtered.groupby('team_id')['faceOffWinPercentage'].cumsum() - filtered['faceOffWinPercentage']) /        filtered.groupby('team_id').cumcount()
    filtered['giveaways_pg'] = (filtered.groupby('team_id')['giveaways'].cumsum() - filtered['giveaways']) / filtered.groupby('team_id').cumcount()
    filtered['takeaways_pg'] = (filtered.groupby('team_id')['takeaways'].cumsum() - filtered['takeaways']) / filtered.groupby('team_id').cumcount()
    filtered['ppg_per'] = ((filtered.groupby('team_id')['powerPlayGoals'].cumsum() - filtered['powerPlayGoals'])) / ((filtered.groupby('team_id')['powerPlayOpportunities'].cumsum() - filtered['powerPlayOpportunities']))

    return filtered

def filter_home_away(df_filtered, df):
    
    # filter home team stats
    filtered_h = df_filtered[df_filtered.HoA == 'home']
    filtered_h = filtered_h.filter(items=['game_id', 'season', 'streak', 'time_travel', 'gpg', 'win_per', 'ppg_per', 'shots_pg', 'hits_pg', 'pim_pg', 'fo_per', 'giveaways_pg', 'takeaways_pg'])
    filtered_h = filtered_h.rename(columns={'streak': 'home_streak', 'time_travel': 'home_time_travel', 'gpg': 'home_gpg', "win_per": "home_win_per", "ppg_per": "home_ppg_per", 'shots_pg': 'home_shots_pg', 'hits_pg': 'home_hits_pg', 'pim_pg': 'home_pim_pg', 'fo_per': 'home_fo_per', 'giveaways_pg': 'home_giveaways_pg',
       'takeaways_pg': 'home_takeaways_pg'})
    # merge home team stats
    df = df.merge(filtered_h, on='game_id', how='left')

    # filter away team stats
    filtered_a = df_filtered[df_filtered.HoA == 'away']
    filtered_a = filtered_a.filter(items=['game_id', 'season', 'streak', 'time_travel', 'gpg', 'win_per', 'ppg_per', 'shots_pg', 'hits_pg', 'pim_pg', 'fo_per', 'giveaways_pg', 'takeaways_pg'])
    filtered_a = filtered_a.rename(columns={'streak': 'away_streak', 'time_travel': 'away_time_travel', 'gpg': 'away_gpg', "win_per": "away_win_per", "ppg_per": "away_ppg_per", 'shots_pg': 'away_shots_pg', 'hits_pg': 'away_hits_pg', 'pim_pg': 'away_pim_pg', 'fo_per': 'away_fo_per', 'giveaways_pg': 'away_giveaways_pg',
       'takeaways_pg': 'away_takeaways_pg'})

    # merge away team stats
    df = df.merge(filtered_a, on='game_id', how='left')
    
    return df

def replace_bools_fillna(df):
    
    df = df.drop(columns=['season_x', 'season_y', 'game_id', 'type', 'date_time', 'date_time_GMT'])
    df = df.replace({'home_streak': False}, 0)
    df = df.replace({'home_streak': True}, 1)
    df = df.replace({'away_streak': False}, 0)
    df = df.replace({'away_streak': True}, 1)
    df = df.replace({'outcome': 'loss'}, 0)
    df = df.replace({'outcome': 'win'}, 1)
    df = df.fillna(0)
    
    return df

### replace_bools_fillna(filter_home_away(seasons(season_20122013_test, season), season_20122013_test))