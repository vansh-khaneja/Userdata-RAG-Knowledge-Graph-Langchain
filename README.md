# Userdata RAG Using Knowledge Graph and LangChain
This project implements multi-query retrieval using Matryoshka Representation Learning (MRL) embeddings with `text-embedding-3-small` and `text-embedding-3-large`. The embeddings are stored and queried using the [Qdrant](https://qdrant.tech/) vector database. To learn more about the project please refer this [article](https://medium.com/@vanshkhaneja/multi-stage-vector-querying-using-matryoshka-representation-learning-mrl-in-qdrant-ddbe425d88f4).

![Alt Text - description of the image](https://github.com/vansh-khaneja/Userdata-RAG-Knowledge-Graph-Langchain/blob/main/graph1.png?raw=true)


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Execution](#execution)
- [Contact](#contact)

## Introduction

In this project, we used Matryoshka Representation Learning embeddings for efficient multi-query retrieval. The embeddings are generated using `text-embedding-3-small` and `text-embedding-3-large` models and stored in the Qdrant vector database. This approach allows for scalable and accurate retrieval of relevant information from large datasets.

## Features

- Fast and efficient way for data retrieval
- Supports `llama 3` and other models with groq
- Two stage retrieval for better searching
- Scalable and high-performance retrieval system

## Installation

1. Clone the repository:

    ```sh
    git clone https://github.com/vansh-khaneja/Userdata-RAG-Knowledge-Graph-Langchain
    cd Userdata-RAG-Knowledge-Graph-Langchain
    ```

2. Set up the Python environment and install dependencies:

    ```sh
    python3 -m venv venv
    source venv/bin/activate
    pip install -r requirements.txt
    ```

3. Set up Neo4j for knowledge graph:

    Follow the [Neo4j documentation](https://console.neo4j.io/) to setup the instance.

4. Set up Groq API key:

    Access the groq api key [GroqCloud](https://console.groq.com/keys) to setup the api key.


## Execution
1.Create a .env file and store all the credentials in it.

    ```sh
    NEO4J_URI="YOUR_NEO4J_URL"
    NEO4J_USERNAME="YOUR_NEO4J_USERNAME"
    NEO4J_PASSWORD="YOUR_NEO4J_PASSWORD"
    GROQ_API_KEY="YOUR_GROQ_API_KEY"
    ```


2.Download the dataset for this project [here](https://www.kaggle.com/datasets/arnavsmayan/amazon-prime-userbase-dataset) or you can try with your own dataset. Just upload it over github and use the repo link.

```sh
    LOAD CSV WITH HEADERS FROM 'https://raw.githubusercontent.com/vansh-khaneja/test5/main/amazon_prime_users.csv' AS row
```


3.Execute the ```main.py``` file by running this command in terminal.

```sh
    python main.py
```


## Contact

For any questions or issues, feel free to open an issue on this repository or contact me at vanshkhaneja2004@gmail.com.

Happy coding!
