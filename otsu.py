import matplotlib.pyplot as plt
from skimage import io, data
from skimage import filters
from skimage import exposure
from skimage.color import rgb2gray
from skimage.measure import label, regionprops
from skimage.morphology import closing, square, opening
from skimage.segmentation import clear_border
import matplotlib.patches as mpatches
from skimage.filters import threshold_otsu
from skimage.color import label2rgb
from skimage.filters import rank
from skimage.morphology import disk, binary_opening
from skimage.filters.rank import mean, mean_bilateral
from skimage.filters.rank import median
import numpy as np
from skimage.transform import resize
from skimage.transform import hough_line, probabilistic_hough_line
from matplotlib import cm
from skimage.feature import canny
#def increase_y ()

camera1 = io.imread("1.jpg", as_gray=True)
camera1 = resize(camera1, (300, 600))

camera1 = exposure.equalize_adapthist(camera1)
camera1 = exposure.rescale_intensity(camera1)
#camera1 = exposure.adjust_gamma(camera1)
camera1 = exposure.adjust_sigmoid(camera1)
#camera1 = exposure.adjust_log(camera1)
#noise = np.random.random(camera1.shape)
#noisy_image = camera1
#noisy_image[noise > 0.98] = 1
#noisy_image[noise < 0.02] = 0
#camera1 = median(noisy_image, disk(1))
#selem = disk(30.0)
#camera1 = rank.equalize(camera1, selem=selem)
#plt.imshow(camera1, cmap='gray', interpolation='nearest')
camera =  rgb2gray(camera1)
camera = mean(camera, disk(1))
#camera = mean_bilateral(camera, disk(10))
camera = median(camera, disk(1))
from scipy.misc import imsave
print(camera)
val = filters.threshold_otsu(camera)
camera = closing(camera > val, square(3))
camera = opening(camera, square(2))

#camera = closing(camera, square(3))
#camera = opening(camera, square(2))
#camera = opening(camera, square(2))

#camera = mean(camera, disk(1))
#plt.imshow(camera, cmap='gray', interpolation='nearest')
camera = clear_border(camera)
#camera = label(camera)
#plt.imshow(camera , cmap='gray', interpolation='nearest')
camera2 = label(camera)

#plt.imshow(camera , cmap='gray', interpolation='nearest')
h, theta, d = hough_line(camera2)

# Generating figure 1
'''
fig, axes = plt.subplots(1, 3, figsize=(15, 6))

ax = axes.ravel()

ax[0].imshow(camera2, cmap=cm.gray)
ax[0].set_title('Input image')
ax[0].set_axis_off()
ax[1].imshow(np.log(1 + h),
             extent=[np.rad2deg(theta[-1]), np.rad2deg(theta[0]), d[-1], d[0]],
             cmap=cm.gray, aspect=1/1.5)
ax[1].set_title('Hough transform')
ax[1].set_xlabel('Angles (degrees)')
ax[1].set_ylabel('Distance (pixels)')
ax[1].axis('image')

ax[2].imshow(camera2, cmap=cm.gray)
'''
edges = canny(camera2, 2, 1, 25)
lines = probabilistic_hough_line(edges, threshold=10, line_length=5,
                                 line_gap=3)

# Generating figure 2
fig, axes = plt.subplots(1, 3, figsize=(15, 5), sharex=True, sharey=True)
ax = axes.ravel()

#camera = clear_border(camera)
#hist, bins_center = exposure.histogram(camera)
#print(val)
#plt.figure(figsize=(18, 8))

#plt.subplot(131)
camera = label2rgb(camera2, image=camera1)
fig, ax = plt.subplots(figsize=(10, 6))
ax.imshow(camera , cmap='gray', interpolation='nearest')
#ax.imshow(camera , cmap='gray', interpolation='nearest')
count = 0
for region in regionprops(camera2):
    # take regions with large enough areas
    if region.area >= 650:
        # draw rectangle around segmented coins
        minr, minc, maxr, maxc = region.bbox
        slice_hei = int((maxr - minr)* 0.1)
        #print(minr, minc, maxr, maxc)
        croped = camera[minr-slice_hei:maxr+slice_hei, minc:maxc]
        imsave('image'+str(count)+'.png', croped)
        count+=1
        #plt.imshow(croped , cmap='gray', interpolation='nearest')
        rect = mpatches.Rectangle((minc, minr), maxc - minc, (maxr - minr)*(1.05),
                                  fill=False, edgecolor='red', linewidth=2)
        ax.add_patch(rect)
ax.set_axis_off()
plt.tight_layout()
plt.show()
