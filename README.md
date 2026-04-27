# Processo Seletivo – Intensivo Maker | AI

Bem-vindo(a) à **etapa prática do processo seletivo para o Intensivo Maker**.

Esta atividade tem como objetivo avaliar competências técnicas relacionadas a **Machine Learning**, **Visão Computacional** e **Otimização de modelos para sistemas embarcados (Edge AI)**, a partir da aplicação prática dos conhecimentos adquiridos nos cursos EAD da etapa anterior.

> 🎯 **Importante**  
> O foco deste desafio é avaliar sua capacidade de **projetar, treinar e otimizar um modelo de IA**.  

---

## 📌 Navegação Rápida

- 🏁 [Passo 0 – Antes de Tudo](#-passo-0-antes-de-tudo)
- ⚙ [Passo 1 – Preparando o Ambiente](#-passo-1-preparando-o-ambiente)
- 💻 [Passo 2 – O Desafio Técnico](#-passo-2-o-desafio-técnico)
  - 🎯 [Conjunto de Dados](#-conjunto-de-dados)
  - 📂 [Estrutura do Projeto](#-estrutura-do-projeto)
  - 📚 [Material de Apoio](#-material-de-apoio)
  - ⚖️ [Critérios de Avaliação](#️-critérios-de-avaliação)
- 📤 [Passo 3 – Instruções de Entrega](#-passo-3-instruções-de-entrega)
  - 📝 [Relatório do Candidato](#-relatório-do-candidato)

---

## 🏁 Passo 0: Antes de Tudo

Caso você **nunca tenha utilizado Git ou GitHub**, não se preocupe.  
Siga atentamente as etapas abaixo.


### 1️⃣ Criação de Conta no GitHub

1. Acesse: https://github.com  
2. Clique em **Sign up**  
3. Crie sua conta gratuita seguindo as instruções da plataforma  

(*O GitHub será utilizado para envio, versionamento e correção automática do seu projeto.*)


### 2️⃣ Instalação do Git

O **Git** é a ferramenta que permite versionar e enviar seu código para o GitHub.

- **Windows**  
  Baixe e instale o **Git Bash**:  
  https://git-scm.com/downloads

- **Linux / macOS**  
  Verifique se o Git já está instalado:
  ```bash
  git --version
  ```

---

## ⚙ Passo 1: Preparando o Ambiente

Para desenvolver o desafio, você deverá criar uma cópia deste repositório.

### 1️⃣ Fork do Repositório

<img width="219" height="45" alt="image" src="https://github.com/user-attachments/assets/5d629626-513a-445c-ba0f-e5bb3e225187" />

1. No canto superior direito desta página, clique em **Fork**  
2. Uma cópia deste repositório será criada no **seu perfil do GitHub**
(*O Fork permite que você trabalhe de forma independente sem alterar o repositório original.*)



### 2️⃣ Clone do Repositório

<img width="149" height="52" alt="image" src="https://github.com/user-attachments/assets/abbd331b-a005-4633-89c6-afd16acbe828" />

No repositório do **seu Fork**, clique em **<> Code**, copie a URL e execute:

```bash
git clone https://github.com/SEU_USUARIO/nome-do-repositorio.git
cd nome-do-repositorio
```
(*O comando `git clone` cria uma cópia do repositório.*)



### 3️⃣ Preparação do Ambiente de Execução

Você pode executar o projeto de **Três formas**. Escolha apenas uma.



#### Opção A – Ambiente Python Local 
Requisitos:
- Python **3.10 ou 3.11**
- pip

Instale as dependências com:

```bash
pip install -r requirements.txt
```



#### Opção B – Dev Container 
Este repositório inclui um **Dev Container** para facilitar a criação de um ambiente Python padronizado.

**Requisitos**
- VS Code
- Docker instalado
- Extensão **Dev Containers**

**Passos**
1. Abra o repositório no VS Code  
2. Selecione **“Reopen in Container”**  
3. Aguarde a criação automática do ambiente  

➡️ As dependências serão instaladas automaticamente.


#### Opção C - via browser
Você também pode abrir o container via github codespace

1. Clique em **<> Code**
2. Clique em **Codespaces**
3. Clique em **Create codespace on image**

<img width="482" height="436" alt="image" src="https://github.com/user-attachments/assets/37a1e99d-66d2-4730-b824-26f834bd8cc3" />


>  Será aberto uma instância do VS Code no seu navegador com o container configurado


---

## 💻 Passo 2: O Desafio Técnico

O desafio consiste em desenvolver um **modelo de Visão Computacional** capaz de **classificar dígitos manuscritos**, e posteriormente **otimizá-lo para execução em dispositivos Edge**, como sistemas embarcados e IoT.

O foco não é apenas obter alta acurácia, mas também **compreender o fluxo completo**:

**treinamento → salvamento → conversão → otimização**



### 🎯 Conjunto de Dados

Será utilizado o dataset **MNIST**, composto por imagens de dígitos manuscritos de **0 a 9**.
<img width="500" height="294" alt="image" src="https://github.com/user-attachments/assets/f323b4cc-d759-4e05-bb58-13e4d6dc7e5b" />

✔️ O dataset já está disponível na biblioteca **TensorFlow/Keras**, não sendo necessário download manual.

📌 *O MNIST é amplamente utilizado para introdução à Visão Computacional e Redes Neurais.*



###  ✅ Requisitos Obrigatórios

**Etapa 1:**  Treinamento do Modelo (`train_model.py`)

Implemente no arquivo `train_model.py` um código que realize:

- Carregamento do dataset MNIST via TensorFlow
- Construção e treinamento de um modelo de classificação baseado em **Redes Neurais Convolucionais (CNN)**  
  (utilizando camadas `Conv2D` e `MaxPooling`)
- Treinamento do modelo
- Exibição da **acurácia final** no terminal
- Salvamento do modelo treinado no formato **Keras** (`.h5`)

(*O modelo salvo será utilizado na etapa de otimização.*)



**Etapa 2:** Otimização do Modelo (`optimize_model.py`)

No arquivo `optimize_model.py`, implemente:

- Carregamento do modelo treinado
- Conversão para **TensorFlow Lite (`.tflite`)**
- Aplicação de técnica de otimização, como:
  - **Dynamic Range Quantization**

(**Objetivo:** reduzir o tamanho do modelo, mantendo desempenho adequado para aplicações de **Edge AI**.)



### 📂 Estrutura do Projeto

⚠️ **Atenção:**  
A estrutura e os nomes dos arquivos **não devem ser alterados**.

```plaintext
seu-repositorio/
├── .github/
│   └── workflows/
│       └── ci.yml            # 🤖 Pipeline de correção automática (NÃO ALTERAR)
├── .devcontainer/            # 🐳 Dev Container (opcional)
│   └── devcontainer.json
├── train_model.py            # ✏️ Treinamento do modelo
├── optimize_model.py         # ✏️ Conversão e otimização
├── requirements.txt          # 📄 Dependências do projeto
├── model.h5                  # 🤖 Modelo treinado (gerado)
├── model.tflite              # ⚡ Modelo otimizado (gerado)
└── README.md                 # 📝 Relatório final do candidato
```



### ⚠️ Restrições e Considerações de Engenharia

Este desafio é avaliado automaticamente por meio de um pipeline de
**integração contínua (CI)**, executado em um ambiente controlado e com
restrições de recursos computacionais.

Você **não precisa conhecer GitHub Actions** para realizar o desafio.
No entanto, é importante respeitar as diretrizes abaixo.

**Diretrizes para o Modelo**

- O modelo deve ser uma **CNN simples**, adequada para **Edge AI**
- Evite arquiteturas muito profundas ou complexas
- Recomenda-se utilizar **até 3 camadas convolucionais**
- **Não utilize modelos pré-treinados**
- Número de épocas **limitado** (ex: até 5)

#### Diretrizes de Execução

- Treinamento apenas em **CPU**
- Tempo total reduzido (compatível com CI)
- Código deve executar do início ao fim **sem intervenção manual**

> **Importante:**  
> O objetivo não é obter a maior acurácia possível, mas sim demonstrar
> **engenharia eficiente**, compatível com ambientes automatizados e
> restrições típicas de aplicações reais de Edge AI.



### 📚 Material de Apoio

Os cursos realizados na etapa anterior **devem ser utilizados como referência**.

- 📘 **Fundamentos de Inteligência Artificial para Sistemas Embarcados**
- 👁️ **Sistemas de Visão Computacional Embarcada**
- ⚙️ **Otimização de Modelos em Sistemas Embarcados**

(*Os exemplos apresentados nesses cursos podem ser adaptados e reutilizados neste desafio.*)



### ⚖️ Critérios de Avaliação

A avaliação considerará:

- **Funcionalidade**  
  Execução correta dos scripts e geração dos arquivos `.h5` e `.tflite`

- **Edge AI**  
  Conversão correta para `.tflite` e aplicação de técnica de otimização

- **Documentação**  
  Preenchimento adequado do relatório (README.md)

---

## 📤 Passo 3: Instruções de Entrega

### ✔️ Validação 

Antes do envio, execute os scripts e confirme a geração dos arquivos:
- `model.h5`
- `model.tflite`



### ⬆️ Envio do Código

```bash
git add .
git commit -m "Entrega do desafio técnico - Seu Nome"
git push origin main
```



### 🔍 Verificação Automática

1. Acesse a aba **Actions** no GitHub  
2. Verifique se o workflow foi executado com sucesso (✅)  
3. Em caso de erro (❌), consulte os logs, corrija e envie novamente

<img width="807" height="363" alt="image" src="https://github.com/user-attachments/assets/d991d35b-2bc2-48f7-9ac7-cf5ca9dc452a" />



### 📎 Submissão Final

Copie o link do seu repositório e envie conforme orientações do processo seletivo no Moodle.

---

## 📝 Relatório do Candidato

O arquivo (`README.md`) deve ser utilizado como **relatório final do desafio**.

Preencha todas as seções de forma clara e objetiva.

> 💡 Dica: não é necessário um relatório extenso.  
> O mais importante é demonstrar **clareza nas decisões técnicas**.

# 🧠 Classificação de Dígitos Manuscritos com CNN e Otimização para Edge AI PNAAT

---

## 👤 Identificação

**Nome Completo:** André Castro Saraiva Leite

---

## 1️⃣ Resumo da Arquitetura do Modelo

O modelo implementado consiste em uma **Rede Neural Convolucional (CNN)** simples e eficiente, projetada especificamente para o problema de classificação de dígitos manuscritos do dataset MNIST.

A arquitetura segue o seguinte fluxo:

- **Entrada:** imagens 28x28 em escala de cinza, com adição de canal (28x28x1)
- **Bloco Convolucional 1:**
  - Conv2D com 16 filtros (3x3) e ativação ReLU
  - MaxPooling2D (2x2)
- **Bloco Convolucional 2:**
  - Conv2D com 32 filtros (3x3) e ativação ReLU
  - MaxPooling2D (2x2)
- **Camadas finais:**
  - Flatten (transformação para vetor)
  - Dense com 64 neurônios (ReLU)
  - Dense com 10 neurônios (Softmax)

### 🎯 Justificativa da Arquitetura

A arquitetura foi projetada com foco em simplicidade, eficiência computacional, boa capacidade de generalização e compatibilidade com ambientes de execução limitados, como aplicações de Edge AI.

Foram utilizadas apenas duas camadas convolucionais, o que é suficiente para o problema MNIST, evitando aumento desnecessário de complexidade, tempo de treinamento e custo computacional.

---

## 2️⃣ Bibliotecas Utilizadas

Principais bibliotecas utilizadas no projeto:

- **TensorFlow / Keras:** utilizada para construção, treinamento, salvamento e conversão do modelo.
- **Python 3.11:** linguagem utilizada no desenvolvimento do projeto.

---

## 3️⃣ Técnica de Otimização do Modelo

A técnica utilizada foi a **Dynamic Range Quantization**, ou **Quantização de Faixa Dinâmica**.

Ela foi implementada por meio da seguinte configuração no conversor TensorFlow Lite:

    converter.optimizations = [tf.lite.Optimize.DEFAULT]

### 🔍 O que essa técnica faz

A quantização de faixa dinâmica reduz a precisão dos pesos do modelo, convertendo representações em `float32` para formatos mais leves. Com isso, o tamanho final do arquivo `.tflite` é reduzido, mantendo uma boa precisão para o problema tratado.

### 🎯 Por que essa escolha

Essa técnica foi escolhida porque é compatível com aplicações de Edge AI, reduz o uso de memória e armazenamento, não exige dados adicionais para calibração e mantém o pipeline de otimização simples.

---

## 4️⃣ Resultados Obtidos

Após o treinamento, o modelo apresentou aproximadamente:

- **Acurácia no teste:** ~98.4%
- **Loss no teste:** valor baixo, indicando bom ajuste do modelo.

### 📊 Interpretação

A acurácia obtida demonstra que o modelo aprendeu corretamente os padrões dos dígitos manuscritos presentes no dataset MNIST. Além disso, o baixo valor de loss indica que o modelo não apenas acerta boa parte das previsões, mas também apresenta boa confiança em suas classificações.

### ⚖️ Trade-off 

Neste projeto, foi priorizada a eficiência, a rapidez de treinamento e o baixo custo computacional em vez da busca pela maior acurácia possível. Essa decisão está alinhada com os objetivos de Edge AI e com a necessidade de execução em ambientes automatizados de Integração Contínua (CI).

---

## 5️⃣ Comentários Adicionais

### 🧩 Dificuldades Encontradas

Durante o desenvolvimento, uma das principais dificuldades foi compreender o fluxo completo do projeto, envolvendo as etapas de treinamento, salvamento, conversão e otimização do modelo.

Também foi necessário organizar corretamente a separação entre os arquivos `train_model.py`, responsável pelo treinamento e salvamento do modelo, e `optimize_model.py`, responsável pela conversão e otimização para TensorFlow Lite.

### ⚙️ Decisões Técnicas Importantes

Foi utilizada uma CNN simples com duas camadas convolucionais, pois essa estrutura já é suficiente para atingir bom desempenho no MNIST, além de reduzir o risco de overfitting e diminuir o tempo de execução.

O treinamento foi limitado a 3 épocas, pois essa quantidade foi suficiente para obter boa convergência no problema, além de reduzir o risco de falhas em ambientes automatizados de CI.

Também foi utilizado `batch_size = 128`, buscando um equilíbrio entre desempenho de treinamento e uso de memória.

### ⚠️ Limitações do Modelo

O modelo desenvolvido é simples e não foi projetado para alcançar a máxima acurácia possível. Não foram utilizadas técnicas mais avançadas.

Além disso, a avaliação foi focada principalmente nas métricas básicas de `accuracy` e `loss`.

### 📚 Aprendizados Durante o Desafio

Durante o desafio, foram consolidados aprendizados importantes sobre a separação entre as etapas de treinamento e otimização de modelos, o uso prático do TensorFlow Lite,conceitos de Edge AI,versionamento de código, integração com GitHub Actions e organização de projetos para execução automática.

## 🆘 Suporte

Em caso de dúvidas:

- Consulte o material dos cursos EAD
- Leia atentamente este README
- Analise os logs das GitHub Actions
- Utilize os canais oficiais para contato com os instrutores

Boa sorte no processo seletivo.
****
