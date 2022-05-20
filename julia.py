import imageio
import numpy as np
import matplotlib.pyplot as plt
import matplotlib.cm as cm


# Image width and height; parameters for the plot
im_width, im_height = 500, 500

zabs_max = 100
nit_max = 250
xmin, xmax = -2, 2
xwidth = xmax - xmin
ymin, ymax = -2, 2
yheight = ymax - ymin
img_no = 0

for n in range(0, 100):
    var = n/100
    c = complex(-var, 5*var)
    img_no += 1
    julia = np.zeros((im_width, im_height))
    for ix in range(im_width):
        for iy in range(im_height):
            nit = 0
            # Map pixel position to a point in the complex plane
            z = complex(ix / im_width * xwidth + xmin,
                        iy / im_height * yheight + ymin)
            # Do the iterations
            while abs(z) <= zabs_max and nit < nit_max:
                z = z**2 + c
                nit += 1
            shade = 1-np.sqrt(nit / nit_max)
            ratio = nit / nit_max
            julia[ix, iy] = ratio

    fig, ax = plt.subplots()
    ax.imshow(julia, interpolation='nearest', cmap=cm.cubehelix_r)

    plt.axis('off')
    fig.patch.set_visible(False)
    plt.tight_layout()
    plt.savefig(f"test{img_no}.png", bbox_inches='tight')
    plt.close()


filenames = []

for i in range(1, 101):
    filenames.append(f'test{i}.png')

images = []
for filename in filenames:
    images.append(imageio.imread(filename))
imageio.mimsave('frc_img\movie.gif', images)
