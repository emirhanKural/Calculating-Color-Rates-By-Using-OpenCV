from __future__ import print_function
import binascii
import struct
from PIL import Image
import numpy as np
import scipy
import scipy.misc
import scipy.cluster
import matplotlib.pyplot as plt


NUM_CLUSTERS = 9 # change number of colors

print('reading image')
im = Image.open('images.jpg')
im = im.resize((150, 150))      # optional, to reduce time
ar = np.asarray(im)
shape = ar.shape
ar = ar.reshape(scipy.product(shape[:2]), shape[2]).astype(float)

print('finding clusters')
codes, dist = scipy.cluster.vq.kmeans(ar, NUM_CLUSTERS)
print('cluster centres:\n', codes)


vecs, dist = scipy.cluster.vq.vq(ar, codes)         # assign codes
counts, bins = scipy.histogram(vecs, len(codes))    # count occurrences

index_max = scipy.argmax(counts)                    # find most frequent
peak = codes[index_max]
colour = binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii')
print('most frequent is %s (#%s)' % (peak, colour))

colors=[]
for i in codes:
    peak=i

    colors.append("#"+ binascii.hexlify(bytearray(int(c) for c in peak)).decode('ascii'))
    print(colors)



# Data
names =colors #rgb değerleri
size = counts #miktarları

# create a figure and set different background
fig = plt.figure()
fig.patch.set_facecolor('white')

# Change color of text
plt.rcParams['text.color'] = 'black'

# Create a circle for the center of the plot
my_circle = plt.Circle((0, 0), 0.7, color='white')

# Pieplot + circle on it
plt.pie(size,labels=names,colors=colors, autopct='%1.1f%%') #dilimin üstünde isimler, miktarlar ve renkleri
p = plt.gcf()
p.gca().add_artist(my_circle)
plt.show()






