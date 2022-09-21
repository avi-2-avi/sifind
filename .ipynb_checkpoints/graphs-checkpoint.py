#!/usr/bin/env python
# coding: utf-8

import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
from src import logic

class Pareto:
    data = {} 
    name = None

    def __init__(self, data, name):
        self.data = data
        self.name = name

# In[4]:
    def get_pareto(self):
        
        df = pd.DataFrame([self.data])
        df = df.stack().reset_index()
        df.columns = ['i', 'Palabras', 'Frec_abs']
        df = df.drop(['i'], axis=1)
        df = df.sort_values(by=['Frec_abs'], ascending=False)

# In[5]:
        size = df['Frec_abs'].sum()
        df["Frec_rel_%"]=100*df["Frec_abs"]/size

# In[6]:
# Frecuencias absolutas
        Frec_rel_val = df["Frec_rel_%"].values
        acum = []
        acum_val = 0

        for val in Frec_rel_val:
            acum_val = acum_val + val
            acum.append(acum_val)

        df["Frec_rel_%_acum"] = acum

# In[7]:
        fig, ax = plt.subplots()
        ax.set_title('Diagrama de Pareto')

        ax.bar(df["Palabras"], df["Frec_abs"], color="C0")
        ax.set_ylabel("Número de palabras", color="C0")
        ax.tick_params(axis="y", colors="C0")

        tick_labels = tuple(df["Palabras"])
        x_max = int(max(plt.xticks()[0]))
        plt.xticks(range(0, x_max+1), tick_labels, rotation=45)

        ax2 = ax.twinx()
        ax2.plot(df["Palabras"], df["Frec_rel_%_acum"], color="C3", marker="D", ms=7)
        ax2.yaxis.set_major_formatter(PercentFormatter())
        ax2.tick_params(axis="y", colors="C3")

        plt.savefig('{}_pareto.png'.format(self.name)
