import matplotlib
matplotlib.use('TkAgg')
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
df = pd.read_excel(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\rela_abund.xlsx',
                   sheet_name='all', usecols=range(0, 19)).dropna(how="all")
original_name = list(df.columns[1:])
new_name = ["a", "b", "c", "d", "e", "f", "g", "h", "i", "j", "k", "l", "m", "n", "o", "p", "q", "r"]
df.rename(columns=dict(zip(original_name, new_name)), inplace=True)
df_melted = pd.melt(df, id_vars=['Genus'], var_name="t")
new_name_2 = ["pH 10"] * 5 + ["pH 10.5"] * 5 + ["pH 11"] * 3 + ["FS-pH 10.5"] * 5
t_day = dict(zip(new_name, new_name_2))
df_melted['Group'] = [t_day[x] for x in df_melted['t']]
new_name_2 = ["0", "6", "20\n\n  pH 10.2", '32', '44', "0", "6", "20\n\n  pH 10.7", '32', '44',
              "0", "6\n\n  pH 11.2", "20", "0", "7", "14\n\n   FS-pH 10.5", '21', '28']
t_day = dict(zip(new_name, new_name_2))
df_melted['tt'] = [t_day[x] for x in df_melted['t']]
df_melted['value'] = [None if x == 0 else x for x in df_melted['value']]
plt.figure(figsize=(8, 10), dpi=150)
ax = sns.scatterplot(data=df_melted, x='t', y='Genus', size='value', sizes=(0, 600))
ax.legend(bbox_to_anchor=(0.995, 1.02), loc=2, labelspacing=1, handlelength=1, fontsize=15)
ax = sns.scatterplot(data=df_melted, x='t', y='Genus', size='value', hue='Group', sizes=(0, 650), legend=False)
sns.set_style('ticks')
ytick_labels = ax.get_yticklabels()
for label in ytick_labels:
    if label.get_text() in ["Sodalinema", "Nodosilinea", "Spirulina", "Caldora", "Synechocystis", "Cyanobacterium"]:
        label.set_color('purple')
    else:
        label.set_color('black')
plt.ylabel('Relative abundance (2% cut off)', color='brown', fontsize=16, labelpad=-10)
plt.gca().yaxis.set_label_coords(-0.2, 0.5)
plt.xlabel("")
xtick_labels = ax.get_xticklabels()
plt.text(-0.15, -0.025, "Cultivated days", transform=ax.transAxes, fontsize=11)
colors = ["#1F77B4"] * 5 + ["#FF7F0E"] * 5 + ["#2CA02C"] * 3 + ["#a51b0b"] * 5
for i in range(len(xtick_labels)):
    xtick_labels[i].set_color(colors[i])
xticks = plt.xticks()[0]
plt.xticks(xticks, new_name_2, fontsize=10)
plt.savefig(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\figures_by_groups\rela_abund', bbox_inches='tight')
plt.close()
