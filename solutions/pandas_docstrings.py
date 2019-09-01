import os
import pandas


(pandas.read_json(DATA_FNAME, orient='index')
       .query('not deprecated')
       .assign(problems=lambda df: df.errors + df.warnings,
               section=lambda df: df['section'].astype('category'),
               type=lambda df: df['type'].astype('category'),
               docstring_length=lambda df: df['docstring'].str.len())
       .explode('problems')
       .pipe(lambda df: df.join(df['problems'].apply(pandas.Series)
                                              .rename(columns={0: 'code',
                                                               1: 'message'})))
       .assign(code=lambda df: df['code'].astype('category'))
       .loc[:, ['docstring_length', 'section', 'type', 'code', 'message']]
       .to_hdf(os.path.join('data', 'docstring_errors_pandas023.hd5'),
               key='main',
               mode='w',
               format='table'))
