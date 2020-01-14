import numpy as np
import tensorflow as tf
import pandas as pd
import time



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

interpreter = tf.lite.Interpreter(model_path="tf_lite_model.tflite")
interpreter.allocate_tensors()

# Get input and output tensors.
input_details = interpreter.get_input_details()
output_details = interpreter.get_output_details()
print(">>>", interpreter.get_input_details())
# Test model on random input data.
input_shape = input_details[0]['shape']

# Test Data
input_data = np.array(test_plantfeatures, np.float32)
input_data_0 = input_data[0].reshape(1,4)

interpreter.set_tensor(input_details[0]['index'], input_data_0)


ntimes = 1000


# Measuring timing
start = time.time()
for i in range(ntimes):
    interpreter.invoke()
end = time.time()
print("TFLite time needed was ", end - start, "seconds")

# The function `get_tensor()` returns a copy of the tensor data.
# Use `tensor()` in order to get a pointer to the tensor.
output_data = interpreter.get_tensor(output_details[0]['index'])
print(output_data)
