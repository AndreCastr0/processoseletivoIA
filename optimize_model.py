import tensorflow as tf
import os

def main():
    print("Carregando modelo model.h5...")
    model = tf.keras.models.load_model("model.h5")

    converter = tf.lite.TFLiteConverter.from_keras_model(model)

    #Dynamic Range Quantization: reduz a precisão dos valores para deixar o modelo mais leve 
    converter.optimizations = [tf.lite.Optimize.DEFAULT]

    tflite_model = converter.convert()

    with open("model.tflite", "wb") as f:
        f.write(tflite_model)

    print("Modelo otimizado salvo como model.tflite \n")


    size_h5 = os.path.getsize("model.h5") / 1024
    size_tflite = os.path.getsize("model.tflite") / 1024

    print("\n")

    print(f"Tamanho original do modelo(h5): {size_h5:.2f} KB \n")
    print(f"Tamanho otimizado do modelo (tflite): {size_tflite:.2f} KB \n")

if __name__ == "__main__":
    main()