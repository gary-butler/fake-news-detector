import pandas as pd
import numpy as np

df = pd.read_csv('news_cleaned_2018_02_13.csv.zip', index_col = 0, compression = 'zip')
working_df = df.loc[df['tag'].isin(['fake', 'reliable']), ['content', 'type']]
working_df.to_csv('news_content_type.csv', index=False)
print(working_df.head)