import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\results_by_groups.xlsx',
                   sheet_name='11.2', usecols=range(0, 26))
sheet_name='11.2'
register_matplotlib_converters()
x = df.iloc[:, 0].values
num_subplots = 8
fig, axes = plt.subplots(nrows=2, ncols=4, figsize=(15,5.5),dpi=150)
y_labels = ['pH', '$\mathrm{HCO_3^-}$ (mmol/L)', '$\mathrm{NH_4^+}$ (mmol/L)',
            '$\mathrm{NO_3^-}$ (mmol/L)', 'Fe (mg/L)', 'OD (750 nm)', 'AFDW (g/L)',
            'Light intensity (μmol/m$^{2}$/s)']
labels = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h']
axes = axes.flatten()
for i in range(num_subplots):
    y = df.iloc[:, i * 3 + 1:i * 3 + 4].values
    label = y_labels[i]
    axes[i].plot(x, y, color="#2CA02C", marker='.', markersize=10, linestyle='none', alpha=0.5, markeredgecolor='none')
    #colors: 10.2 "#1F77B4", 10.7 "#FF7F0E", 11.2 "#2CA02C", FS-10.5 "#a51b0b"
    axes[i].set_ylabel(label)
    axes[i].text(-0.25, 1, labels[i], transform=axes[i].transAxes, fontsize=12, fontweight='bold')
    axes[i].set_xlim(x[0] - 2, x[-1] + 2)
    axes[i].set_xticks(range(0, 22, 3)) #(0, 46, 5) (0, 22, 3) (0, 29, 4)
    axes[i].set_xlabel('Cultivated days')
    if i == num_subplots - 1:
        y_light_intensity = df.iloc[:, -1].values
        axes[i].plot(x, y_light_intensity, color="grey", marker='.', markersize=10,
                     alpha=0.5, linestyle='none', markeredgecolor='none', label='Provided lights')
        axes[i].legend(loc='upper right', bbox_to_anchor=(1.0, 0.9), prop={'size': 9})
    else:
        axes[i].set_xlabel('Cultivated days')
        if label != 'pH':
            axes[i].set_ylim(bottom=0)
plt.subplots_adjust(hspace=0.05, wspace=0.28)
plt.savefig(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\figures_by_groups\%s.png' % sheet_name,
            bbox_inches='tight')
plt.close()
