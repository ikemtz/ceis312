import tensorflow as tf
from tensorflow import keras

import tensorflowjs as tfjs

print(tf.version.VERSION)

new_model = tf.keras.models.load_model('2x1.keras')

# Show the model architecture
new_model.summary()

tfjs.converters.save_keras_model(new_model, './2x1.json')
