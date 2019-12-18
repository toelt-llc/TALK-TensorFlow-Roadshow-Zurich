import tensorflow as tf
import pathlib

model = tf.keras.applications.MobileNetV2(weights="imagenet", input_shape=(224,224,3))
model.save('mobilenetv2.h5')

converter = tf.lite.TFLiteConverter.from_keras_model(model)
tflite_model = converter.convert()

tflite_model_file = pathlib.Path('mobilenetv2.tflite')
tflite_model_file.write_bytes(tflite_model)

# With optimization
converter2 = tf.lite.TFLiteConverter.from_keras_model(model)
converter2.optimizations = [tf.lite.Optimize.DEFAULT]
tflite_model2 = converter2.convert()
tflite_model_file2 = pathlib.Path('mobilenetv2_opt.tflite')
tflite_model_file2.write_bytes(tflite_model2)
