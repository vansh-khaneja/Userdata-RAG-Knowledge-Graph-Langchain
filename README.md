# Userdata RAG Using Knowledge Graph and LangChain
This project implements Retrieval Augmented Generation using Neo4j knowledge grphs and Langhcain framework. Using Llama 3 as the language model for beter graphs and response generation. To learn more about the project please refer this [article](...).


## Table of Contents

- [Introduction](#introduction)
- [Features](#features)
- [Installation](#installation)
- [Execution](#execution)
- [Contact](#contact)

## Introduction

This repository will guide you in buiding a user ineractive RAG application with the help of ```knowledge graphs``` and ```langchain```. Using ```Llama 3``` as the language model and ```streamlit``` to create a user interative web inteface.

## Features

- Fast and efficient way for data retrieval
- Supports `llama 3` and other models with groq
- Better Graphs Visualtization
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
streamlit run main.py
```


## Contact

For any questions or issues, feel free to open an issue on this repository or contact me at vanshkhaneja2004@gmail.com.

Happy coding!
