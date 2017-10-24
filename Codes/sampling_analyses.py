# -*- coding: utf-8 -*-
"""
Created on Tue Oct 24 17:59:35 2017

@author: LK
"""

import pandas as pd
import numpy as np

def random_sampling_distri(num_obs, seeds):
    summary = pd.DataFrame()
    for obs in xrange(0, num_obs, 500):
        for seed in xrange(0, seeds, 50):
            df = pd.DataFrame(index = range(obs), columns = ['ID', 'event', 'sample'])
            np.random.seed(seed)
            df['rand_num'] = np.random.random(df.shape[0])
            df['event'] = np.where(df['rand_num'] <= 0.12, 1, 0)
            np.random.seed(seed + 1)
            df['rand_num'] = np.random.random(df.shape[0])
            df['sample'] = np.where(df['rand_num'] <= 0.63, 'dev', 'val')
            summ = df.groupby(['sample']).agg({'ID': np.size, 'event': np.mean})
            summ['num_ids'] = summ['ID'].sum()
            summary = summary.append(summ)
    return summary

summary = random_sampling_distri(5000, 250)