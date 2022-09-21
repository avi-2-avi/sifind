#!/usr/bin/env python
# coding: utf-8

from typing import ForwardRef
import pandas as pd
import matplotlib.pyplot as plt
from matplotlib.ticker import PercentFormatter
import random

class Graphs:
    data = {}
    name = None

    def __init__(self, data, name):
        self.data = data
        self.name = name


    def graph(self):
        def rancolor():
            return "#" + ''.join(random.choice('0123456789AB') for j in range(6))

        plt.style.use('seaborn-dark')

        df = pd.DataFrame([self.data])
        df = df.stack().reset_index()
        df.columns = ['i', 'Palabras', 'Frec_abs']
        df = df.drop(['i'], axis=1)
        df = df.sort_values(by=['Frec_abs'], ascending=False)

        lista = []
        for i in range(0, len(df)):
            lista.append(rancolor())
        df['Colors'] = lista

        size = df['Frec_abs'].sum()
        df["Frec_rel_%"]=100*df["Frec_abs"]/size

# Frecuencias absolutas
        Frec_rel_val = df["Frec_rel_%"].values
        acum = []
        acum_val = 0

        for val in Frec_rel_val:
            acum_val = acum_val + val
            acum.append(acum_val)

        df["Frec_rel_%_acum"] = acum
        df["Longitud_palabra"] = df["Palabras"].str.len()

        # Diagrma de Pareto 
        fig, ax = plt.subplots()
        ax.set_title('Diagrama de Pareto - {} palabras'.format(self.name), size=16)
        ax.bar(df["Palabras"], df["Frec_abs"], color=df["Colors"])
        ax.set_ylabel("Número de palabras", color="Black", size=14)
        ax.tick_params(axis="y", colors="Black")
        tick_labels = tuple(df["Palabras"])
        x_max = int(max(plt.xticks()[0]))
        plt.xticks(range(0, x_max+1), tick_labels, rotation=20, size=12)
        ax2 = ax.twinx()
        ax2.plot(df["Palabras"], df["Frec_rel_%_acum"], color=rancolor(), marker="D", ms=7)
        ax2.yaxis.set_major_formatter(PercentFormatter())
        ax2.tick_params(axis="y", colors="Black")

        plt.savefig('img/{}_pareto.png'.format(self.name))
        plt.clf()

        # Grafico de Donut
        plt.title('Gráfico de Donut - {} palabras'.format(self.name), size=16)
        plt.pie(x=df['Frec_abs'], labels=df['Palabras'], autopct='%.2f%%',
                startangle=90, colors=df['Colors'])
        plt.axis('equal')
        plt.legend(loc='upper left')
        donut = plt.Circle(xy=(0,0), radius=.75, facecolor='white')
        plt.gca().add_artist(donut)
        plt.savefig('img/{}_donut.png'.format(self.name))
        plt.clf()

        # Diagrama de Burbuja
        df['Area'] = (25 * df['Frec_abs']/2)**2
        plt.scatter(df['Longitud_palabra'], df['Frec_abs'], s=df['Area'], c=df['Colors'],
                    edgecolors='black', alpha=0.5)
        plt.xlim([0, df['Longitud_palabra'].max() + 2])
        plt.ylim([0, df['Frec_abs'].max() + 1])
        plt.xlabel("Longitud de palabra", size=14)
        plt.ylabel("Frecuencia de palabra", size=14)
        plt.title("Diagrama de burbuja - {} palabras".format(self.name), size=16)
        plt.savefig('img/{}_burbuja.png'.format(self.name))
        plt.clf()

        return 0