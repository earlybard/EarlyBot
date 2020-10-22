import tensorflow as tf


def allow_gpu_growth():
    """
    Required for GPU usage unless you have more VRAM than me.
    """
    gpus = tf.config.experimental.list_physical_devices('GPU')
    if gpus:
        try:
            for gpu in gpus:
                tf.config.experimental.set_memory_growth(gpu, True)
        except RuntimeError as e:
            print(e)
