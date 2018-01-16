"""
this example shows the construction of a convolutional layer.
"""
from keras.models import Sequential
from keras.layers import Conv2D

model = Sequential()
model.add(Conv2D(filters=32, kernel_size=3, strides=2, padding='valid',
                 activation='relu', input_shape=(128,128,3)))
model.summary()




