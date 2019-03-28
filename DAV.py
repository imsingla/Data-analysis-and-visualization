#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Wed Mar 27 11:09:21 2019

@author: Pranav
"""
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

import seaborn as sns
sns.set(style="darkgrid", color_codes=True)



from IPython import get_ipython
get_ipython().run_line_magic('matplotlib', 'inline')

plt.rcParams["figure.figsize"] = [20, 20]
np.random.seed(0)
df = pd.read_csv('/users/apple/downloads/pucho/language.csv')


"""This dataset was designed to make interactive maps of language features. 
Can you make an interactive map that shows different linguistic features?
"""
#Lnguistics
#macroarea attribute

sns.lmplot(x='longitude', y='latitude', hue='macroarea', 
           data=df, 
           fit_reg=False, scatter_kws={'alpha':0.8})

#family attribute

sns.lmplot(x='longitude', y='latitude', hue='family', 
           data=df, 
           fit_reg=False, scatter_kws={'alpha':0.8})

#genus attribute 
sns.lmplot(x='longitude', y='latitude', hue='genus', 
           data=df, 
           fit_reg=False, scatter_kws={'alpha':0.8})

