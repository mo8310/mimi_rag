# mini-rag

This is a minimal implementation of the RAG model for question answering.

## Requirements

- Python 3.8 or later

#### Install Python using MiniConda

1) Download and install MiniConda from [here](https://docs.anaconda.com/free/miniconda/#quick-command-line-install)
2) Create a new environment using the following command:
```bash
$ conda create -n mini-rag python=3.8
```
3) Activate the environment:
```bash
$ conda activate mini-rag
```

## Installation

### Install the required packages

```bash
$ pip install -r requirements.txt
```

### Setup the environment variables

```bash
$ cp .env.example .env
```

Set your environment variables in the `.env` file. Like `OPENAI_API_KEY` value.

## Run the FastAPI server
```bash
$ cd src
$ pip install -r requirements.txt
$ uvicorn main:app --reload --host 0.0.0.0 --port 5000
```

The welcome endpoint is `http://127.0.0.1:5000/api/v1/`. Import the Postman collection from `src/assets/mini-rag-app.postman_collection.json` after starting the server.

## POSTMAN Collection

Download the POSTMAN collection from /assets/mini-rag-app.postman_collection.json


