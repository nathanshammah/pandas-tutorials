uint8_series = pandas.Series(numpy.empty(100_000_000, dtype=numpy.uint8))
float64_series = pandas.Series(numpy.empty(100_000_000, dtype=numpy.float64))

%timeit uint8_series.mean()
%timeit float64_series.mean()
