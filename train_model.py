import tensorflow as tf
from tensorflow import keras
from tensorflow.keras import layers

    #
def load_images():

    #Carregar dataset MNIST
    (x_train, y_train), (x_test, y_test) = tf.keras.datasets.mnist.load_data()

    #Normalizando os pixels das imagens para intervalo 0-1
    
    x_train = x_train.astype("float32") / 255
    x_test = x_test.astype("float32") / 255

    # Adiciona dimensão que indica a quantidade de canais de cor, tornando: (28, 28, 1)
    
    x_train = x_train[..., tf.newaxis]
    x_test = x_test[..., tf.newaxis]

    return (x_train, y_train), (x_test, y_test)


def build_model():
    model = tf.keras.models.Sequential([
        tf.keras.layers.Input(shape=(28, 28, 1)),

        #primeira camada convolucional

        tf.keras.layers.Conv2D(16, (3, 3), activation='relu'), #quantidade de filtros, tamanho dos kernels, função de ativação (devolve os valores positivos obtidos)
        tf.keras.layers.MaxPooling2D((2, 2)), #verifica cada região 2x2 e mantém apenas o maior valor        
        
        #segunda camada convolucional
        
        tf.keras.layers.Conv2D(32, (3, 3), activation='relu'),
        tf.keras.layers.MaxPooling2D((2, 2)),
        
        tf.keras.layers.Flatten(), #transforma a matriz em um vetor
        tf.keras.layers.Dense(64, activation='relu'), #camada totalmente conectada para combinar as características
        tf.keras.layers.Dense(10, activation='softmax') #cada classe recebe um valor, onde o somatório das classes é 1. O maior valor representa o resultado

])  
    #Compilação do modelo
    model.compile(
        optimizer="adam", #atualiza os pesos da rede
        loss="sparse_categorical_crossentropy", #quantifica o erro do modelo
        metrics=["accuracy"] #verifica a acuracia: proporção de corretas em relação ao total
    )
    return model

def main():
    (x_train, y_train), (x_test, y_test) = load_images()

    model = build_model()

    model.fit( #treinamento do modelo
        x_train,
        y_train,
        epochs=3, #percorre o dataset 3 vezes
        batch_size=128, #quantidade de amostras antes de atualizar os pesos
        validation_split=0.1, #10% dos dados de treino para validação durante o treino
        verbose=1
    )

    loss, accuracy = model.evaluate(x_test, y_test, verbose=0) #avalia o modelo usando os dados de teste
    print(f"Acurácia final no teste: {accuracy:.4f}")
    print(f"Loss final no teste: {loss:.4f}")

    model.save("model.h5")
    print("Modelo salvo como model.h5")


if __name__ == "__main__":
    main()