import numpy as np
from numpy import exp
import matplotlib.pyplot as plt
from scipy.special import factorial
import pandas as pd
from mpl_toolkits.mplot3d import Axes3D
import statsmodels.api as sm
from statsmodels.api import Poisson
from scipy import stats
from scipy.stats import norm
from statsmodels.iolib.summary2 import summary_col
def MLEPlot(levels, maks_tau):
    poisson_pmf = lambda level, tau: tau**level / factorial(level) * exp(-tau)
    level_values = range(0, levels)
    tau_range = np.linspace(0,maks_tau, maks_tau+1)
    fig, ax = plt.subplots(figsize=(12, 8))

    for tau in tau_range:
        distribution = []
        for level_i in level_values:
            distribution.append(poisson_pmf(level_i, tau))
        ax.plot(level_values,
                distribution,
                label=f'$\ tau$={tau}',
                alpha=0.5,
                marker='o',
                markersize=8)

    ax.grid()
    ax.set_xlabel('$levels$', fontsize=14)
    ax.set_ylabel('$f(levels \mid \tau)$', fontsize=14)
    ax.axis(xmin=0, ymin=0)
    ax.legend(fontsize=10)

    plt.show()


