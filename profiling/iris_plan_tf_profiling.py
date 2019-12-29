import pandas as pd
import numpy as np
import tensorflow as tf
import tensorflow.lite as tflite
import time


# Measuring timing


train_ds_url = "http://download.tensorflow.org/data/iris_training.csv"
test_ds_url = "http://download.tensorflow.org/data/iris_test.csv"
ds_columns = ['SepalLength', 'SepalWidth','PetalLength', 'PetalWidth', 'Plants']
species = np.array(['Setosa', 'Versicolor', 'Virginica'], dtype=np.object)

#Load data
categories = 'Plants'

#print("Downloading files...")
train_path = tf.keras.utils.get_file(train_ds_url.split('/')[-1], train_ds_url)
test_path = tf.keras.utils.get_file(test_ds_url.split('/')[-1], test_ds_url)

#print("Reading files in...")
train = pd.read_csv(train_path, names=ds_columns, header=0)
train_plantfeatures, train_categories = train, train.pop(categories)

test = pd.read_csv(test_path, names=ds_columns, header=0)
test_plantfeatures, test_categories = test, test.pop(categories)

y_categorical = tf.keras.utils.to_categorical(train_categories, num_classes=3)
y_categorical_test = tf.keras.utils.to_categorical(test_categories, num_classes=3)

#print("Finished data loading")


#print("Train dataset dimensions ", train.shape)
#print("Test dataset dimensions ", test.shape)


#build model
model = tf.keras.Sequential([
  tf.keras.layers.Dense(16, input_dim=4),
  tf.keras.layers.Dense(3, activation=tf.nn.softmax),
])

#print(model.summary())

print("Compiling")
model.compile(loss='categorical_crossentropy',
              optimizer='sgd',
              metrics=['accuracy'])

print("Fitting")
start = time.time()
model.fit(train_plantfeatures, y_categorical, epochs=100, batch_size = 32, verbose=0)
end = time.time()
print("Fitting time needed was ", end - start, "seconds")

#eval model
loss, accuracy = model.evaluate(test_plantfeatures, y_categorical_test)




print("Evaluating the model on the test data...")
print("loss:%f"% (loss))
print("accuracy: %f"%   (accuracy))

print("Now saving h5 version of this model")
#model.save('iris_model.h5')


# Time profiling for predict()
input_data = np.array(test_plantfeatures, np.float32)
input_data_0 = input_data[0].reshape(1,4)
start = time.time()
for i in range(1000):
    model.predict(input_data_0)
end = time.time()
print("Inference time needed was ", end - start, "seconds")


print("Converting to TFLite...")
tflite_converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = tflite_converter.convert()
open("tf_lite_model.tflite", "wb").write(tflite_model)
