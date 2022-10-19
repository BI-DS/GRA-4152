import numba
import numpy as np
from numba import jit, prange, njit
import random
from itertools import combinations
import statsmodels.api as sm
import pandas as pd
import timeit
from sklearn.neural_network import MLPClassifier
import warnings
from multiprocessing.pool import Pool
import multiprocessing as mp
warnings.filterwarnings("ignore")

# get number of cpus
c = mp.cpu_count()

# get data from statsmodels
df = sm.datasets.get_rdataset("Guerry", "HistData").data
df = df[['Lottery', 'Literacy', 'Wealth', 'Crime_pers',
         'Donations', 'Infants', 'Suicides', 'Commerce',
         'Clergy', 'Crime_parents', 'Infanticide']].dropna()
y = df.Lottery.values
df = df.drop(columns=['Lottery'])
x = df.values

# get variables, i.e. 1, 2, ...
variables = [i for i in range(x.shape[1])]

# find all possible combinations
models = []
for k in variables:
  for i in combinations(variables,k+1):
    models.append(list(i))

# lets fit a relatively slow model
fitted_models=[]
def model_fitting(model):
  cls = MLPClassifier(batch_size=5)
  fitted_models.append(cls.fit(x[:,model],y))
  return fitted_models

# make a function that uses pool.map, i.e,
# parallel computing
def f1():
  fitted_models = []
  start = timeit.default_timer()
  with Pool(c) as pool:
    L = pool.map(model_fitting,models)
  print('elapsed time {} with parallel fitting'.format(round(timeit.default_timer()-start,2)))


def f2():
  fitted_models = []
  start = timeit.default_timer()
  for model in models:
    model_fitting(model)
  print('elapsed time {} with model-wise fitting'.format(round(timeit.default_timer()-start,2)))

# run both
f1()
f2()
