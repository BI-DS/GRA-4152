import os
os.environ['TF_CPP_MIN_LOG_LEVEL'] = '3'
from tensorflow.keras import layers
from tensorflow.keras import activations
from tensorflow.keras.models import Sequential


"""
Encoder and decoder networks for black and white images.
Both encoder and decoder are MLP models with one hidden
layer. The output of the encoder are the parameters
of the Gaussian distribution, while the output of the
decoder is only the mu parameter the Gaussian distribution
as we treat sigma=0.75 as known to make thigs easier
"""
input_shape = (28*28,)
units = 400
activation  = 'relu'
latent_dim = 20
# Gaussian Encoder for vetorized images
encoder_mlp = Sequential(
                        [ 
                        layers.InputLayer(input_shape=input_shape),
                        layers.Dense(units,activation=activation),
                        layers.Dense(2*latent_dim),
                        ]
                        )
out = encoder_mlp(x)
mu  = out[:,:latent_dim]
log_var = out[:,latent_dim:]
std = tf.math.exp(0.5*log_var)

output_dim  = 28*28
# Bernoulli Decoder for B&W images
decoder_mlp = Sequential(
                        [
                        layers.InputLayer(input_shape=latent_dim),
                        layers.Dense(units,activation=activation),
                        layers.Dense(output_dim),
                        ]
                        )
mu = decoder_mlp(z)

"""
Encoder and decoder networks for the color MNIST images. 
Both architectures are based on convolutional neural networks.
The output of the encoder are the parameters of the Gaussian 
distribution, while the output of the decoder is the mu parameter 
of the Gaussian distribution. Note that we are assuming a fixed
standard deviation of 0.75
"""
input_shape = (28,28,3)
filters     = 32
kernel_size = 3
strides     = 2
activation  = 'relu'
latent_dim  = 50
encoder_conv = Sequential(
                        [
                        layers.InputLayer(input_shape=input_shape),
                        layers.Conv2D(
                          filters=filters,   kernel_size=kernel_size, strides=strides, activation=activation, padding='same'),
                        layers.Conv2D(
                          filters=2*filters, kernel_size=kernel_size, strides=strides, activation=activation, padding='same'),
                        layers.Conv2D(
                          filters=4*filters, kernel_size=kernel_size, strides=strides, activation=activation, padding='same'),
                        layers.Flatten(),
                        layers.Dense(2*latent_dim)
                        ]
                        )
out = encoder_conv(x)
mu  = out[:,:latent_dim]
log_var = out[:,latent_dim:]
std = tf.math.exp(0.5*log_var)
eps = tf.random.normal(mu.shape)
z = mu + eps*std


target_shape=(4,4,128)
channel_out=3
units = np.prod(target_shape)
decoder_conv = Sequential(
                        [
                        layers.InputLayer(input_shape=(latent_dim,)),
                        layers.Dense(units=units, activation=activation),
                        layers.Reshape(target_shape=target_shape),
                        layers.Conv2DTranspose(
                            filters=filters*2, kernel_size=kernel_size, strides=2, padding='same',output_padding=0,
                            activation=activation),
                        layers.Conv2DTranspose(
                            filters=filters, kernel_size=kernel_size, strides=2, padding='same',output_padding=1,
                            activation=activation),
                        layers.Conv2DTranspose(
                            filters=channel_out, kernel_size=kernel_size, strides=2, padding='same', output_padding=1),
                        layers.Activation('linear', dtype='float32'),
                        ]
                        )
mu = decoder_conv(z)
# we dont need to learn sigma for this data as it is challenging
# we assume the value below
std = 0.75
eps = tf.random.normal(mu.shape)
x = mu + eps*std
