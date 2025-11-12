import tensorflow as tf

# XXX Note that your data has been normalized between [0 1], so before you plot
# the gird of images you need to scale the output of the decoder (x_hat) to the
# range [0 255] and change the dtype to unit 8. Just use this function
img = tf.clip_by_value(255*x_hat, clip_value_min=0, clip_value_max=255).numpy().astype(np.uint8)

# Adam optimizer is my default choice 
optimizer = tf.keras.optimizers.Adam(learning_rate=1e-4) 

'''
train function to update the VAE trainable variables
'''
@tf.function
def train(self, x, optimizer):
    with tf.GradientTape() as tape:
        loss = self.call(x)
    # self.vae_los = - ELBO
    # where ELBO is given in Equation 1
    gradients = tape.gradient(self.vae_loss, self.trainable_variables)
    optimizer.apply_gradients(zip(gradients, self.trainable_variables))

    return loss

"""
Code to plot a 10x10 grid of images,
images have size (N, H, W, C), where N (=100) is
number of samples, H (=28) is height, W (=28) is width,
and C (=1 black-white,=3 color) is channels.
"""
from mpl_toolkits.axes_grid1 import ImageGrid
def plot_grid(images,N=10,C=10,figsize=(24., 28.),name='posterior'):
    fig = plt.figure(figsize=figsize)
    grid = ImageGrid(fig, 111,  # similar to subplot(111)
                     nrows_ncols=(N, C),  
                     axes_pad=0,  # pad between Axes in inch.
                     )
    for ax, im in zip(grid, images):
        # Iterating over the grid returns the Axes.
        ax.imshow(im)
        ax.set_xticks([])
        ax.set_yticks([])
    
    plt.subplots_adjust(wspace=0, hspace=0)
    plt.savefig('./xhat_bw_'+name+'.pdf')
    plt.close()

"""
addresses to get the dataset mnist_bw, which are npy files 
corresponding to images of size (28,28,1)
"""
# train dset
'https://www.dropbox.com/scl/fi/fjye8km5530t9981ulrll/mnist_bw.npy?rlkey=ou7nt8t88wx1z38nodjjx6lch&st=5swdpnbr&dl=0'
# test det
'https://www.dropbox.com/scl/fi/dj8vbkfpf5ey523z6ro43/mnist_bw_te.npy?rlkey=5msedqw3dhv0s8za976qlaoir&st=nmu00cvk&dl=0'
# labels, which are useful to color scatters of the latent space
'https://www.dropbox.com/scl/fi/8kmcsy9otcxg8dbi5cqd4/mnist_bw_y_te.npy?rlkey=atou1x07fnna5sgu6vrrgt9j1&st=m05mfkwb&dl=0'


"""
addresses to get the dataset mnist_color, which are pkl files 
corresponding to images of size (28,28,3) and labels are npy
"""
# train dset
'https://www.dropbox.com/scl/fi/w7hjg8ucehnjfv1re5wzm/mnist_color.pkl?rlkey=ya9cpgr2chxt017c4lg52yqs9&st=ev984mfc&dl=0'
# test dset
'https://www.dropbox.com/scl/fi/w08xctj7iou6lqvdkdtzh/mnist_color_te.pkl?rlkey=xntuty30shu76kazwhb440abj&st=u0hd2nym&dl=0'
# labels, which are useful to color scatters of the latent space
'https://www.dropbox.com/scl/fi/fkf20sjci5ojhuftc0ro0/mnist_color_y_te.npy?rlkey=fshs83hd5pvo81ag3z209tf6v&st=99z1o18q&dl=0'
