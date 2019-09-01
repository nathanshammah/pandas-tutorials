import locale
import glob
import os
import pandas


locale.setlocale(locale.LC_ALL, 'en_US.UTF-8')


(pandas.concat(pandas.read_csv(fname,
                               comment='#',
                               dtype={'Pageviews': str})
                     .head(5_000)
               for fname in glob.glob(os.path.join(DATA_DIR, '*.csv.gz')))
       .set_index('Page')
       .dropna()
       .drop(columns='Page Value')
       .assign(**{'Pageviews': lambda df: df['Pageviews'].apply(locale.atoi),
                  'Unique Pageviews': lambda df: df['Unique Pageviews'].apply(locale.atoi),
                  'Avg. Time on Page': lambda df: pandas.to_timedelta(df['Avg. Time on Page'].str.lstrip('<')).dt.seconds,
                  'Entrances': lambda df: df['Entrances'].apply(locale.atoi),
                  'Bounce Rate': lambda df: df['Bounce Rate'].str.rstrip('%').astype(float),
                  '% Exit': lambda df: df['% Exit'].str.rstrip('%').astype(float)})
       .to_parquet(os.path.join('data', 'pandas_page_views_2018.parquet'),
                   engine='pyarrow'))
