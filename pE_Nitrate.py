import pandas as pd
import matplotlib.pyplot as plt
from pandas.plotting import register_matplotlib_converters
register_matplotlib_converters()
df = pd.read_excel('pH experiment.xlsx',
                   sheet_name='nitrate', usecols=[5,6,7,8,9,10,11,12,13,14])    # path, sheet and columns
print(df.head())     # check the correction
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
ln1,=plt.plot(x, y1, color='lightgreen',marker='>',label='pH 10',linestyle=':')
ln2,=plt.plot(x, y2, color='cornflowerblue',marker='o',label='pH 10',linestyle=':')
ln3,=plt.plot(x, y3, color='silver',marker='*',label='pH 10',linestyle=':')
ln4,=plt.plot(x, y4, color='gold',marker='^',label='pH 10.5',linestyle=':')
ln5,=plt.plot(x, y5, color='darkorange',marker='p',label='pH 10.5',linestyle=':')
ln6,=plt.plot(x, y6, color='lightcoral',marker='h',label='pH 10.5',linestyle=':')
ln7,=plt.plot(x, y7, color='darkblue',marker='s',label='pH 11',linestyle=':')
ln8,=plt.plot(x, y8, color='indigo',marker='d',label='pH 11',linestyle=':')
ln9,=plt.plot(x, y9, color='darkslategray',marker='8',label='pH 11',linestyle=':')
plt.legend(ncol=3)
plt.xlabel('Cultivated days',fontsize=16)
plt.ylabel('Nitrate concentration (mM)',color='brown',fontsize=16)
plt.xticks(range(1,47,3)) #设置x轴刻度：range(最低值，最高值，步长）
ticks=[0,0.7,1.4,2.1,2.8,3.5,4.2,4.9] #指定坐标轴的刻度显示
plt.yticks(ticks)
plt.grid()
#plt.grid(color='0.5',linestyle='--',linewidth='1')
plt.title('Nitrate concentration (mM)',fontsize=16)
#ax1.legend(loc='center left')
#ax2.legend(loc='upper right')
plt.show()