import numpy as np
import pandas as pd

from scipy.stats import chi2_contingency, mannwhitneyu

# data
from data import *

# saved_commands
"""
# Convert relevant columns to numeric, coercing errors to NaN
# df['Adult literacy rate  (%)'] = pd.to_numeric(df['Adult literacy rate  (%)'], errors='coerce')

# group by dataframe and calculate mean for numeric columns
# grouped_df = df.groupby('Continent').mean(numeric_only=True)
# print(grouped_df['Adult literacy rate  (%)'])
# df.fillna(0, inplace=True)
# grouped_df = df.groupby('Country').mean()
"""


def main():
    # dest = pd.read_csv('dest.csv')
    # print(dest.head(), '\n')

    # tips = pd.read_csv('tips.csv')
    # print(tips.head(), '\n')

    # # join dataframes using inner join (matching values in both dataframes), outer join (all values in both dataframes), right join (all values in right dataframe), left join (all values in left dataframe),
    # df_inner = pd.merge(dest, tips, on='EmpNr', how='left')
    # print(df_inner.head())

    # purchase = pd.read_csv('purchase.csv')
    # pivot_table = pd.pivot_table(purchase, values='Number', margins=True, index=['Weather',], columns=['Food'], aggfunc='sum')
    # print(pivot_table)

    # data = pd.DataFrame(sample_data, columns=['name', 'gender', 'communication_skill_score', 'quantitative_skill_score'])
    # print(data.describe(), '\n')

    data1 = [7, 8, 4, 9, 8]
    data2 = [3, 4, 2, 1, 1]

    stat, p = mannwhitneyu(data1, data2)
    print("p-values:", p)

    if p < 0.01:
        print("Hypothesis Rejected")
    else:
        print("Hypothesis Accepted")


if __name__ == "__main__":
    main()
