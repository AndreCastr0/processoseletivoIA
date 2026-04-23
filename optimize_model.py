import tensorflow as tf
import os


def load_images():
    #Carregar dataset MNIST (divisão de treino e validação pré definida)
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    #Normalizando os pixels da imagem para intervalo 0-1
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # Adiciona dimensão do canal: (28, 28) para (28, 28, 1)
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    return (x_train, y_train), (x_test, y_test)


def main():

if __name__ == "__main__":
    main()