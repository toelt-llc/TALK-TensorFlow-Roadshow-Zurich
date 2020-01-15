#
# (C) Umberto Michelucci, TOELT LLC
# www.toelt.ai

#
# This script will run a model NOT compiled for the EDGE TPU
# and will do 10 different runs to measure the inference time
# needed by each inference
#

import numpy as np
import tflite_runtime.interpreter as tflite
import time

print("Loading the data...")
mnist_test = np.loadtxt('mnist_test.csv', delimiter = ',')
print(mnist_test.shape)
print(mnist_test[0].shape)

print("Casting the data to float32 (for training aware quantization)")
image_1 = mnist_test[0].astype(np.float32)
image_1 = image_1[1:785]
image_1 = np.expand_dims(image_1, axis=0)
print(image_1.shape)


print("Loading the model...")
model_path = 'mnist_model_bignn.tflite'
#model_path = 'mnist_model_quant.tflite'
interpreter = tflite.Interpreter(model_path)
interpreter.allocate_tensors()

interpreter.set_tensor(interpreter.get_input_details()[0]["index"], image_1)


print("Running 10 predictions...")
for i in range(10):
    start = time.monotonic()
    interpreter.invoke()
    inference_time = time.monotonic() - start
    print('%.1fms' % (inference_time * 1000))

print("Prediction is: ")
predictions = interpreter.get_tensor(
    interpreter.get_output_details()[0]["index"])

print(predictions)
