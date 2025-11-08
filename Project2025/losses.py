def kl_divergence(mu, log_var):
    return 0.5 * tf.reduce_sum(tf.square(mu) + tf.exp(log_var) - log_var - 1, axis=-1) 

def log_diag_mvn(x, mu, log_sigma):
    sum_axes = tf.range(1, tf.rank(mu))
    k = tf.cast(tf.reduce_prod(tf.shape(mu)[1:]), x.dtype)
    logp = - 0.5 * k * tf.math.log(2*np.pi) \
           - log_sigma \
           - 0.5*tf.reduce_sum(tf.square(x - mu)/tf.math.exp(2.*log_sigma),axis=sum_axes)
    return logp
