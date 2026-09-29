import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 120

fielding_df = pd.read_csv('sample_fielding_data.csv')
fielding_df['Player Name'] = fielding_df['Player Name'].astype(str)
fielding_df['Team'] = fielding_df['Team'].astype(str)
fielding_df['Pick'] = fielding_df['Pick'].astype(str).str.upper()
fielding_df['Throw'] = fielding_df['Throw'].astype(str).str.upper()
fielding_df['Runs'] = pd.to_numeric(fielding_df['Runs'], errors='coerce').fillna(0)
fielding_df['Ball Count'] = pd.to_numeric(fielding_df['Ball Count'], errors='coerce').fillna(0).astype(int)
fielding_df['Position'] = pd.to_numeric(fielding_df['Position'], errors='coerce').fillna(0).astype(int)
fielding_df['Overcount'] = pd.to_numeric(fielding_df['Overcount'], errors='coerce').fillna(0).astype(int)
fielding_df['Venue'] = fielding_df['Venue'].astype(str)
fielding_df['Stadium'] = fielding_df['Stadium'].astype(str)

for col in ['Catch_Successful', 'Dropped_Catch', 'Stumping', 'Run_Out', 'Missed_Run_Out', 'Direct_Hit']:
    fielding_df[col] = fielding_df[col].astype(str).str.upper()
    fielding_df[col] = fielding_df[col].map({'Y': 1, 'YES': 1, 'TRUE': 1, '1': 1, 'N': 0, 'NO': 0, 'FALSE': 0, '0': 0}).fillna(0).astype(int)

selected_players = ['Rohit Sharma', 'Suryakumar Yadav', 'Hardik Pandya']
analysis_df = fielding_df[fielding_df['Player Name'].isin(selected_players)].copy()

player_summary = (
    analysis_df.groupby('Player Name', as_index=False)
    .agg(
        Position=('Position', 'first'),
        CP=('Pick', lambda s: (s == 'Y').sum()),
        GT=('Throw', lambda s: (s == 'Y').sum()),
        C=('Catch_Successful', 'sum'),
        DC=('Dropped_Catch', 'sum'),
        ST=('Stumping', 'sum'),
        RO=('Run_Out', 'sum'),
        MRO=('Missed_Run_Out', 'sum'),
        DH=('Direct_Hit', 'sum'),
        RS=('Runs', 'sum')
    )
)

player_summary['PS'] = (
    player_summary['CP'] * 1
    + player_summary['GT'] * 1
    + player_summary['C'] * 3
    - player_summary['DC'] * 3
    + player_summary['ST'] * 3
    + player_summary['RO'] * 3
    - player_summary['MRO'] * 2
    + player_summary['DH'] * 2
    + player_summary['RS']
)

player_summary = player_summary[['Player Name', 'Position', 'CP', 'GT', 'C', 'DC', 'ST', 'RO', 'MRO', 'DH', 'RS', 'PS']]

print(player_summary.to_string(index=False))

best_player = player_summary.sort_values('PS', ascending=False).iloc[0]
print(f"\nTop fielder: {best_player['Player Name']} (PS = {best_player['PS']})")

plt.figure(figsize=(9, 5))
ax = sns.barplot(data=player_summary, x='Player Name', y='PS', hue='Player Name', dodge=False, palette='viridis', legend=False)
ax.set_title('Performance Score Comparison by Player')
ax.set_xlabel('Player')
ax.set_ylabel('Performance Score (PS)')
for container in ax.containers:
    ax.bar_label(container, padding=3, fmt='%.0f')
plt.tight_layout()
plt.savefig('ps_chart.png', dpi=150)

stack_df = player_summary[['Player Name', 'CP', 'GT', 'C', 'DC', 'ST', 'RO', 'MRO', 'DH']].melt(id_vars='Player Name', var_name='Action Type', value_name='Value')
plt.figure(figsize=(11, 6))
ax = sns.barplot(data=stack_df, x='Player Name', y='Value', hue='Action Type', palette='Set2')
ax.set_title('Fielding Action Breakdown by Player')
ax.set_xlabel('Player')
ax.set_ylabel('Count')
plt.legend(title='Action Type', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout()
plt.savefig('action_breakdown.png', dpi=150)

print('\nCharts saved: ps_chart.png and action_breakdown.png')
