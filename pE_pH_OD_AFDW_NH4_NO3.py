import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\pH experiment.xlsx',
                   sheet_name='AFDW', usecols=[5,6,7,8,9,10,11,12,13,14,15,16,17])    # path, sheet and columns
print(df.head())
sheet_name = 'AFDW'
x=df['day']
y1=df['A1']
y2=df['A2']
y3=df['A3']
y4=df['B1']
y5=df['B2']
y6=df['B3']
y7=df['C1']
y8=df['C2']
y9=df['C3']
y10=df['SL1']
y11=df['SL2']
y12=df['SL3']
ln1,=plt.plot(x, y1, color='darkorange',marker='>',label='pH 10.2')
ln2,=plt.plot(x, y2, color='darkorange',marker='>')
ln3,=plt.plot(x, y3, color='darkorange',marker='>')
ln4,=plt.plot(x, y4, color='lightgreen',marker='^',label='pH 10.7')
ln5,=plt.plot(x, y5, color='lightgreen',marker='^')
ln6,=plt.plot(x, y6, color='lightgreen',marker='^')
ln7,=plt.plot(x, y7, color='gold',marker='s',label='pH 11.2')
ln8,=plt.plot(x, y8, color='gold',marker='s')
ln9,=plt.plot(x, y9, color='gold',marker='s')
ln10,=plt.plot(x, y10, color='lightskyblue',marker='v',label='FS-pH 10.5')
ln11,=plt.plot(x, y11, color='lightskyblue',marker='v')
ln12,=plt.plot(x, y12, color='lightskyblue',marker='v')
plt.legend(ncol=2, loc=1)
plt.xlabel('Cultivated days', fontsize=16)
plt.ylabel('AFDW (g/L)',color='brown',fontsize=16)
plt.ylim(bottom=0, top=1.0)
plt.xticks(range(0,46,3))
"""
pH: ticks=[bottom=10.2,top=11.7]
OD: ticks=[bottom=0,top=0.9]
AFDW: ticks=[bottom=0,top=1.0]
Lights: ticks=[0,30,60,90,120,150], Light intensity (μmol/m$^{2}$/s)
ammonium: ticks=[0,0.09,0.18,0.27,0.36,0.45]
nitrate: ticks=[0,0.7,1.4,2.1,2.8,3.5,4.2]

"""
plt.yticks()
#plt.grid(color='0.5',linestyle='--',linewidth='1')
plt.savefig(r'D:\OneDrive - University of Calgary\pH experiment\Manuscript\Data\figures\%s.png' % sheet_name , bbox_inches='tight')
plt.close()