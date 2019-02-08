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
TMR_correction_rate = 50
TMR_wait_count = 0

# the source image to be tested
img_src = "img/carl3.png"

# the figure for display
fig = plt.figure()

# load the initial image
im = Image.open(img_src) # Can be many different formats.
pix0 = im.load()
pix1 = pix0
pix2 = pix0

print 'loaded ' + str(img_src) + ' of size: ' + str(im.size)  # Get the width and hight of the image for iterating over
ani_im = plt.imshow(im, animated=True)



# =================================================== #
#              EDIT THIS FUNCTION CODE                #
# =================================================== #

def TMR():
    # TMR code goes here
    print 'TMR GOES HERE'



# from: https://matplotlib.org/examples/animation/dynamic_image.html
def updatefig(*args):
    global TMR_enabled, TMR_wait_count
    global pix0, pix1, pix2
    x_flip = random.randint(0,im.size[0]-1)
    y_flip = random.randint(0,im.size[1]-1)
    color = pix0[x_flip,y_flip]
    if (TMR_wait_count == TMR_correction_rate):
        TMR_wait_count = 0
        TMR()
    else:
        TMR_wait_count += 1
    #print 'Flipping bits at pix0el [' + str(x_flip) + ',' + str(y_flip) + '] ' + str(color)

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
    if c_flip == 1:
        color = (color[0],c_flip,color[2])
    if c_flip == 2:
        color = (color[0],color[1],c_flip)

    # now actually change the color!
    pix0[x_flip,y_flip] = (color)
    color = pix0[x_flip,y_flip]

    # set and return for the animation loop
    ani_im.set_array(im)
    return ani_im,

# show the animation
ani = animation.FuncAnimation(fig, updatefig, interval=SEU_per_ms, frames=500, blit=True)
# ani.save('img/animation.gif', writer='imagemagick', fps=60)
plt.show()
