import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from matplotlib.patches import Patch
from matplotlib.patches import Ellipse

df = pd.read_excel(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\NMDS.xlsx', sheet_name='all', usecols=[0,1,2,3,4])
print(df.head())

fig, ax = plt.subplots(figsize=(10, 8))
ax.set_facecolor('#EAEAF2')
ax.grid(True, color='white')
for spine in ax.spines.values():
    spine.set_edgecolor(ax.get_facecolor())
sns.scatterplot(x='axis1', y='axis2', data=df, s=200, hue='pH',
                style='group2', markers=['o', 's', 'D', '^'],
    palette=sns.cubehelix_palette(as_cmap=True), ax=ax, legend=False)

legend_elements = [plt.Line2D([0], [0], marker='o', color='w', label='pH 10.2', markerfacecolor='black', markersize=10),
                   plt.Line2D([0], [0], marker='s', color='w',  label='pH 10.7', markerfacecolor='black', markersize=10),
                   plt.Line2D([0], [0], marker='D', color='w', label='pH 11.2', markerfacecolor='black', markersize=10),
                   plt.Line2D([0], [0], marker='^', color='w', label='FS-pH 10.5', markerfacecolor='black', markersize=10)]
plt.legend(handles=legend_elements, loc='upper right')

plt.xlabel("NMDS1", fontsize=14)
plt.ylabel("NMDS2", fontsize=14)
plt.title('Bray-Curtis Dissimilarities',fontsize=16)
plt.text(0.79, 0.05, "Stress = 0.244", transform=ax.transAxes, fontsize=14)
# make colorbar
sc = ax.scatter([], [], c=[], vmin=10.283, vmax=11.393, cmap=sns.cubehelix_palette(as_cmap=True))
cbar_ax = fig.add_axes([0.92, 0.15, 0.03, 0.7])
cbar = plt.colorbar(sc, cax=cbar_ax)
cbar.set_label('pH', fontsize=14)

plt.savefig(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\figures\NMDS_pycharm.png', bbox_inches='tight')
