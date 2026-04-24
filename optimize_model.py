import tensorflow as tf
import os

def main():
    print("Carregando modelo model.h5...")
    model = tf.keras.models.load_model("model.h5")

    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    #Dynamic Range Quantization: reduz a precisão dos valores para deixar o modelo mais leve 
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    tflite_model = converter.convert()

    
    


if __name__ == "__main__":
    main()