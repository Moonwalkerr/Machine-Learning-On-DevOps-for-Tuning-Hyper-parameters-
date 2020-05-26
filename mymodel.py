#!/usr/bin/env python
# coding: utf-8

# In[3]:


from keras.layers import Convolution2D
from keras.layers import MaxPooling2D
from keras.layers import Flatten
from keras.layers import Dense
from keras.models import Sequential
model = Sequential()
model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                   input_shape=(64, 64, 3)
                       ))
model.add(MaxPooling2D(pool_size=(2, 2)))
n=0
model.add(Flatten())
model.add(Dense(units=100, activation='relu'))
model.add(Dense(units=1, activation='sigmoid'))
ep=1
opx='RMSprop'
model.summary()
model.compile(optimizer=x, loss='binary_crossentropy', metrics=['accuracy'])
from keras_preprocessing.image import ImageDataGenerator
train_datagen = ImageDataGenerator(
        rescale=1./255,
        shear_range=0.2,
        zoom_range=0.2,
        horizontal_flip=True)
test_datagen = ImageDataGenerator(rescale=1./255)
training_set = train_datagen.flow_from_directory(
        '/root/training_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
test_set = test_datagen.flow_from_directory(
        '/root/test_set/',
        target_size=(64, 64),
        batch_size=32,
        class_mode='binary')
model.fit(
        training_set,
        steps_per_epoch=8000,
        epochs=ep,
        validation_data=test_set,
        validation_steps=800)
print(metrics)

model.save('mycnnmodel.h5')


# In[ ]:




