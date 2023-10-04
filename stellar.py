###############
# module import
###############
import pandas as pd
import numpy as np
import tqdm
import matplotlib.pyplot as plt

###################
# function for plot
###################

def plot_size(f0,mag):
    size = f0*(10**((-mag)/2.5))
    return size

def star_plot(f0, mag_lim, season):
    fig = plt.figure(figsize=(5, 8))
    ax = fig.add_subplot(111)#, projection="polar")

    for i in tqdm.tqdm(range(len(st))):
        if st['mag'][i] < mag_lim:
            ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=plot_size(f0,st['mag'][i]), color='black')

    ax.set_xlim(ra[season])
    ax.set_ylim(dec[season])
    ax.set_rasterized(True)
    ax.axis("off")

    plt.savefig("/north_"+season+"_wh_"+str(f0)+"_"+str(mag_lim)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.close()

st = pd.read_csv("stellar.csv", names=("ra", "dec", "mag"))

ra = {'sp':[-4.0,-2.5], 'su':[-5.7,-4.0], 'fa':[-6.2,-5.2], 'wi':[-2.5,-1.0]}
dec = {'sp':[-55,70], 'su':[-55,70], 'fa':[-55,70], 'wi':[-55,70]}

# star_plot(f0(flux_const), mag_lim, season('sp','su','fa','wi'))
# input your directry 
YOUR_DIRECTRY = 

# input your parameter
flux_const = 
magnitude_limit = 
season = 
#'sp','su','fa','wi'
star_plot(flux_const, magnitude_limit, season) 
