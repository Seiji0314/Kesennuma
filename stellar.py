###############
# module import
###############
import pandas as pd
import numpy as np
import tqdm
import matplotlib.pyplot as plt
#import mpl_interactions
#import mpl_interactions.ipyplot as iplt
#from mpl_interactions.controller import Controls

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
            #ctrls = iplt.scatter(-(st['ra'][i])*2*np.pi/360., st['dec'][i],s=(10, 1000),color='black')
            #controls = iplt.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], tau=tau, beta=(1, 10, 100), "o", markersize=plot_size(f0,st['mag'][i]), color='black')
            #_ = iplt.scatter(-(st['ra'][i])*2*np.pi/360., st['dec'][i], s=ctrls["size"])

    ax.set_xlim(ra[season])
    ax.set_ylim(dec[season])
    ax.set_rasterized(True)
    ax.axis("off")

    plt.savefig("/Users/seiji/Desktop/astro/01_asaca/plot/fig/north_"+season+"_wh_"+str(f0)+"_"+str(mag_lim)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
    plt.close()

st = pd.read_csv("/Users/seiji/Desktop/astro/01_asaca/plot/stellar.csv", names=("ra", "dec", "mag"))

seasons = ['sp','su','fa','wi']
ra = {'sp':[-4.0,-2.5], 'su':[-5.7,-4.0], 'fa':[-6.2,-5.2], 'wi':[-2.5,-1.0]}
dec = {'sp':[-55,70], 'su':[-55,70], 'fa':[-55,70], 'wi':[-55,70]}

#star_plot(f0(flux_const), mag_lim, season('sp','su','fa','wi'))
star_plot(15, 4, 'fa') 

"""
fig = plt.figure(figsize=(3, 8))
ax = fig.add_subplot(111)#, projection="polar")

for i in tqdm.tqdm(range(len(st))):
    if st['mag'][i] < 4:
    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=1, color='yellow')
        ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=plot_size(f0, st['mag'][i]), color='black')
    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=2, color='white',alpha=0.1)
    #ax.plot(st['ra'][i], st['dec'][i], "o", markersize=1, color='yellow')
    #ax.plot(st['ra'][i], st['dec'][i], "*", markersize=5*(3.-st['mag'][i]), color='orange')

#ax.set_rlim(90,-60)
#ax.set_rticks([])  # Less radial ticks
ticks1 = (np.arange(12)*np.pi*2./12.) 
labels1 = ['Sep.','Oct.','Nov.', 'Dec.','Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.','Jul.', 'Aug.']
ticks2 = (np.arange(365)*np.pi*2./365.) 
labels2 = []
#labels = ['Sep.','Oct.','Nov.', 'Dec.','Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.','Jul.', 'Aug.']
#plt.xticks(ticks1, labels1)
#plt.xticks(ticks2, labels2)
#ax.grid(linewidth=5)
ax.set_xlim(-6.2, -5.2)
ax.set_ylim(-55,70)
ax.set_rasterized(True)
ax.axis("off")

#ax.set_thetaticks([0, 6, 12, 18])  # Less radial ticks
#plt.gca().set_rasterized(True)
plt.savefig("/Users/seiji/Desktop/astro/01_asaca/plot/fig/north_fall_r_wh_"+str(f0)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)
#plt.show()
plt.close()

fig = plt.figure(figsize=(3, 8))

#plt.scatter(st['ra'], st['dec'], c='yellow', s=10**(0.25*(4.-st['mag'])))
#plt.show()
plt.style.use('dark_background')

ax = fig.add_subplot(111)#, projection="polar")

for i in tqdm.tqdm(range(len(st))):
    if st['mag'][i] < 4:
    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=1, color='yellow')
        ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=plot_size(f0, st['mag'][i]), color='yellow')
    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=2, color='white',alpha=0.1)
    #ax.plot(st['ra'][i], st['dec'][i], "o", markersize=1, color='yellow')
    #ax.plot(st['ra'][i], st['dec'][i], "*", markersize=5*(3.-st['mag'][i]), color='orange')

#ax.set_rlim(90,-60)
#ax.set_rticks([])  # Less radial ticks
ticks1 = (np.arange(12)*np.pi*2./12.) 
labels1 = ['Sep.','Oct.','Nov.', 'Dec.','Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.','Jul.', 'Aug.']
ticks2 = (np.arange(365)*np.pi*2./365.) 
labels2 = []
#labels = ['Sep.','Oct.','Nov.', 'Dec.','Jan.', 'Feb.', 'Mar.', 'Apr.', 'May', 'Jun.','Jul.', 'Aug.']
#plt.xticks(ticks1, labels1)
#plt.xticks(ticks2, labels2)
#ax.grid(linewidth=5)
ax.set_xlim(-6.2, -5.2)
ax.set_ylim(-55,70)
ax.set_rasterized(True)
ax.axis("off")

plt.savefig("/Users/seiji/Desktop/astro/01_asaca/plot/fig/north_fall_r_"+str(f0)+".png", bbox_inches="tight", pad_inches=0.05, dpi=300)

#plt.scatter(st['ra'], st['dec'], c='yellow', s=10**(0.25*(4.-st['mag'])))
#plt.show()

fig = plt.figure(figsize=(6, 6))
ax = fig.add_subplot(111)#, projection="polar")
for i in tqdm.tqdm(range(len(st))):
    if st['mag'][i] < 4:

    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=1, color='yellow')
        ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=plot_size(f0, st['mag'][i]), color='yellow')
    #ax.plot(-(st['ra'][i])*2*np.pi/360., st['dec'][i], "o", markersize=2, color='white',alpha=0.1)    #ax.plot(st['ra'][i], st['dec'][i], "o", markersize=1, color='yellow')
    #ax.plot(st['ra'][i], st['dec'][i], "*", markersize=5*(3.-st['mag'][i]), color='orange')

ax.set_rlim(-90, 60)
#ax.set_thetaticks([0, 6, 12, 18])  # Less radial ticks
ax.set_rasterized(True)
#plt.savefig("/Users/seiji/Desktop/astro/01_asaca/plot/fig/south.pdf", bbox_inches="tight", pad_inches=0.05)
#plt.close()
"""