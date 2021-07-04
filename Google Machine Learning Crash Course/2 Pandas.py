# https://colab.research.google.com/github/google/eng-edu/blob/main/ml/cc/exercises/pandas_dataframe_ultraquick_tutorial.ipynb?utm_source=mlcc&utm_campaign=colab-external&utm_medium=referral&utm_content=mlcc-prework&hl=en#scrollTo=cIJEv08DMSxj

import numpy as np
import pandas as pd

column_names = ('Eleanor', 'Chidi', 'Tahani', 'Jason')
df = pd.DataFrame(np.random.randint(0,101,size=(3, 4)), columns= column_names)

print(df,'\n')

print('the value in the cell of row #1 of the Eleanor column')
print(df.iloc[1]['Eleanor'],'\n')

print('Create a fifth column named Janet, which is populated with the row-by-row sums of Tahani and Jason.')
df['Janet'] = df['Tahani'] + df['Jason']
print(df)

