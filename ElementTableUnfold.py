'''
@author: Fan Dong
'''

import matplotlib
matplotlib.use('TkAgg')
import matplotlib.pyplot as plt
import re
import pandas as pd
from typing import Tuple


def extract(index: str):
    search_result = re.search(r'D(\d{1,2})([A-Z]{1,2}[1-3])', index)
    return [search_result.group(1), search_result.group(2)]


def unfold(df_e: pd.DataFrame) -> pd.DataFrame:
    unfolded_list = []
    for j in range(len(df_e)):
        tmp = extract(df_e.iloc[j, 0])
        tmp.append(df_e.iloc[j, 1])
        unfolded_list.append(tmp)
    df_tmp = pd.DataFrame(unfolded_list, columns=['Day', 'Column', 'Value'])
    df_tmp['Day'] = df_tmp['Day'].astype(int)
    df_tmp.set_index(['Day', 'Column'], inplace=True)
    result = df_tmp.unstack()
    result.columns = [x[1] for x in result.columns]
    return result


def plot(df: pd.DataFrame, file_name: str):
    # df = df_preprocessed
    plt.figure(figsize=(6, 5))
    label_count = [0, 0, 0, 0]
    for j in range(df.shape[1]):
        if df.columns[j].startswith('A'):
            if label_count[0] == 0:
                label_count[0] += 1
                label = 'pH 10'
            else:
                label = None
            plt.scatter(df.index.values, df.iloc[:, j].values, color='darkorange', marker='>', label=label)
        elif df.columns[j].startswith('B'):
            if label_count[1] == 0:
                label_count[1] += 1
                label = 'pH 10.5'
            else:
                label = None
            plt.scatter(df.index.values, df.iloc[:, j].values, color='lightgreen', marker='^', label=label)
        elif df.columns[j].startswith('C'):
            if label_count[2] == 0:
                label_count[2] += 1
                label = 'pH 11'
            else:
                label = None
            plt.scatter(df.index.values, df.iloc[:, j].values, color='gold', marker='s', label=label)
        elif df.columns[j].startswith('SL'):
            if label_count[3] == 0:
                label_count[3] += 1
                label = 'SL'
            else:
                label = None
            plt.scatter(df.index.values, df.iloc[:, j].values, color='mediumpurple', marker='o', label=label)
        else:
            raise ValueError("None of [A, B, C, SL]")
    plt.legend(ncol=1, loc=1)
    plt.xlabel('Cultivated days', fontsize=16)
    plt.ylabel(f'{file_name} (mg/L)', color='brown', fontsize=16)
    plt.xticks(range(1, 48, 3))
    plt.savefig(r'D:\Pycharm\project\results\%s.pdf' % file_name, bbox_inches='tight')
    plt.close()


if __name__ == '__main__':
    # input data
    source_data = pd.read_excel(r'D:\OneDrive - University of Calgary\pH experiment\ICP\ICP.xlsx', sheet_name='Sheet1').iloc[5:, :]
    # Preprocess data
    for i in range(1, source_data.shape[1]):
        df_preprocessed = unfold(source_data.iloc[:, [0, i]])
        plot(df_preprocessed, source_data.columns[i])

