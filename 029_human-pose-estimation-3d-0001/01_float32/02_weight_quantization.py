### tf-nightly-2.2.0-dev20200502

import tensorflow as tf

# Weight Quantization - Input/Output=float32
converter = tf.lite.TFLiteConverter.from_saved_model('saved_model')
converter.optimizations = [tf.lite.Optimize.OPTIMIZE_FOR_SIZE]
#converter.target_spec.supported_ops = [tf.lite.OpsSet.TFLITE_BUILTINS,tf.lite.OpsSet.SELECT_TF_OPS]
tflite_quant_model = converter.convert()
with open('human_pose_estimation_3d_0001_256x448_weight_quant.tflite', 'wb') as w:
    w.write(tflite_quant_model)
print("Weight Quantization complete! - human_pose_estimation_3d_0001_256x448_weight_quant.tflite")
