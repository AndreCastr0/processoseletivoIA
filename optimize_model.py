import tensorflow as tf
import os

def main():
    print("Carregando modelo model.h5...")
    model = tf.keras.models.load_model("model.h5")

    

if __name__ == "__main__":
    main()