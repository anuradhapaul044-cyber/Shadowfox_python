import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
import seaborn as sns

sns.set_style('whitegrid')
plt.rcParams['figure.dpi'] = 120

df = pd.read_excel('fielding_data.xlsx')

df['Player Name'] = df['Player Name'].astype(str)
df['Team'] = df['Team'].astype(str)
df['Pick'] = df['Pick'].astype(str).str.upper()
df['Throw'] = df['Throw'].astype(str).str.upper()
df['Runs'] = pd.to_numeric(df['Runs'], errors='coerce').fillna(0)
df['Position'] = pd.to_numeric(df['Position'], errors='coerce').fillna(0).astype(int)
df['Ball Count'] = pd.to_numeric(df['Ball Count'], errors='coerce').fillna(0).astype(int)
df['Overcount'] = pd.to_numeric(df['Overcount'], errors='coerce').fillna(0).astype(int)
for col in ['Catch_Success', 'Dropped_Catches', 'Stumping', 'Run_Out', 'Missed_RunOut', 'Direct_Hit']:
    df[col] = pd.to_numeric(df[col], errors='coerce').fillna(0).astype(int)

selected_players = ['Rohit Sharma', 'Suryakumar Yadav', 'Hardik Pandya']
fielding_data = df[df['Player Name'].isin(selected_players)].copy()

player_summary = (
    fielding_data.groupby('Player Name', as_index=False)
    .agg(
        Position=('Position', lambda s: ', '.join(sorted(map(str, set(s.astype(int).tolist()))))),
        CP=('Pick', lambda s: (s == 'Y').sum()),
        GT=('Throw', lambda s: (s == 'Y').sum()),
        C=('Catch_Success', 'sum'),
        DC=('Dropped_Catches', 'sum'),
        ST=('Stumping', 'sum'),
        RO=('Run_Out', 'sum'),
        MRO=('Missed_RunOut', 'sum'),
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
summary_table = player_summary.sort_values('PS', ascending=False).reset_index(drop=True)
print(summary_table.to_string(index=False))
print('\nTop fielder:', summary_table.iloc[0]['Player Name'], '(PS =', summary_table.iloc[0]['PS'], ')')

plt.figure(figsize=(8, 5))
ax = sns.barplot(data=summary_table, x='Player Name', y='PS', hue='Player Name', dodge=False, palette='viridis', legend=False)
ax.set_title('Performance Score Comparison by Player')
ax.set_xlabel('Player')
ax.set_ylabel('Performance Score (PS)')
for container in ax.containers:
    ax.bar_label(container, padding=3, fmt='%.0f')
plt.tight_layout(); plt.savefig('ps_bar.png', dpi=150)

stack_df = summary_table[['Player Name', 'CP', 'GT', 'C', 'DC', 'ST', 'RO', 'MRO', 'DH']].melt(id_vars='Player Name', var_name='Action Type', value_name='Value')
plt.figure(figsize=(11, 6))
ax = sns.barplot(data=stack_df, x='Player Name', y='Value', hue='Action Type', palette='Set2')
ax.set_title('Fielding Action Breakdown by Player')
ax.set_xlabel('Player')
ax.set_ylabel('Count')
plt.legend(title='Action Type', bbox_to_anchor=(1.02, 1), loc='upper left')
plt.tight_layout(); plt.savefig('fielding_breakdown.png', dpi=150)

print('\nSaved plots: ps_bar.png and fielding_breakdown.png')
