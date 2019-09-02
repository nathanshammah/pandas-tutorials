import operator
import urllib.parse
import pandas


page_views = pandas.read_parquet(PAGE_VIEWS_FNAME)
page_views.index = (page_views.index
                              .to_series()
                              .apply(urllib.parse.urlparse)
                              .apply(operator.attrgetter('path'))
                              .str.split('/')
                              .str[-1]
                              .str.rstrip('.html'))


docstring_errors = (pandas.read_hdf(DOCSTRING_ERRORS_FNAME)
                          .join(page_views.groupby('Page')['Pageviews'].sum()))
