import random
import time
import numpy as np
from matplotlib import pyplot as plt
from matplotlib import animation
from matplotlib.pyplot import imshow, show
from PIL import Image

# ======= #
# Globals #
# ======= #

# Single Event Upsets in ms
# exagerated for teaching purposes
SEU_per_ms = 1

# if TMR is enabled or not
TMR_enabled = False

# TMR correction opportunties
TMR_correction_rate = 500
TMR_wait_count = 0

# the source image to be tested
img_src = "img/carl3.png"

# the figure for display
fig = plt.figure()

# load the initial image
im0 = Image.open(img_src) # Can be many different formats.
im1 = Image.open(img_src) # Can be many different formats.
im2 = Image.open(img_src) # Can be many different formats.
im_total = Image.open(img_src) # Can be many different formats.
pix0 = im0.load()
pix1 = im1.load()
pix2 = im2.load()
# to display the total flips
pix_total = im_total.load()

print 'loaded ' + str(img_src) + ' of size: ' + str(im_total.size)  # Get the width and hight of the image for iterating over
ani_im = plt.imshow(im_total, animated=True)

# =================================================== #
#              EDIT THIS FUNCTION CODE                #
# =================================================== #

def TMR():
    global pix0, pix1, pix2, pix_total
    # A purposefully unoptimal solution
    print "Running TMR ..."
    for x in range(0,im_total.size[0]-1):
        for y in range(0,im_total.size[1]-1):
            c0 = pix0[x,y]
            c1 = pix1[x,y]
            c2 = pix2[x,y]
            if (c0 != c1):
                if (c0 == c2):
                    pix1[x,y]      = pix0[x,y]
                    pix_total[x,y] = pix0[x,y]
                else:
                    pix0[x,y]      = pix1[x,y]
                    pix_total[x,y] = pix1[x,y]
            if (c0 != c2):
                if (c0 == c1):
                    pix2[x,y]      = pix0[x,y]
                    pix_total[x,y] = pix0[x,y]
                else:
                    pix0[x,y]      = pix1[x,y]
                    pix_total[x,y] = pix1[x,y]
            if (c1 != c2):
                if (c1 == c0):
                    pix2[x,y]      = pix1[x,y]
                    pix_total[x,y] = pix1[x,y]
                else:
                    pix1[x,y]      = pix2[x,y]
                    pix_total[x,y] = pix2[x,y]
    print 'udpated!'



# from: https://matplotlib.org/examples/animation/dynamic_image.html
def updatefig(*args):
    global TMR_enabled, TMR_wait_count
    global pix0, pix1, pix2, pix_total

    # find the location to flip a bit
    x_flip = random.randint(0,im_total.size[0]-1)
    y_flip = random.randint(0,im_total.size[1]-1)

    i_f = random.randint(0,2)
    # choose the image that will have a bit flipped
    color = pix_total[x_flip,y_flip]
    if (i_f == 0):
        color = pix0[x_flip,y_flip]
    elif (i_f == 1):
        color = pix1[x_flip,y_flip]
    elif (i_f == 2):
        color = pix2[x_flip,y_flip]

    # this is wher the TMR can occur
    if (TMR_wait_count == TMR_correction_rate):
        TMR_wait_count = 0
        TMR()
    else:
        TMR_wait_count += 1

    # find where to flip the bit
    c_flip = random.randint(0,2)
    partial_color = 0
    n = random.randint(0,7)
    val = 2**n

    # flip the bits
    if (int(color[c_flip]) + val > 255):
        partial_color = color[c_flip] - val
    else:
        partial_color = color[c_flip] + val

    # the 3 flip options
    if c_flip == 0:
        color = (c_flip,color[1],color[2])
    elif c_flip == 1:
        color = (color[0],c_flip,color[2])
    elif c_flip == 2:
        color = (color[0],color[1],c_flip)

    # now actually change the color!
    if (i_f == 0):
        pix0[x_flip,y_flip] = color
    elif (i_f == 1):
        pix1[x_flip,y_flip] = color
    elif (i_f == 2):
        pix2[x_flip,y_flip] = color
    pix_total[x_flip,y_flip] = (color)
    color = pix_total[x_flip,y_flip]

    # set and return for the animation loop
    ani_im.set_array(im_total)
    return ani_im,

# show the animation
ani = animation.FuncAnimation(fig, updatefig, interval=SEU_per_ms, blit=True)
# ani.save('img/animation.gif', writer='imagemagick', fps=60)
plt.show()
