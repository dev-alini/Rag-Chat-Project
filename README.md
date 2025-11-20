# Rag-Chat-Project

🧠 RAG Chat – Chat com Busca em Banco SQL usando FastAPI + React

Este projeto implementa um chat inteligente com RAG (Retrieval-Augmented Generation), capaz de consultar um banco de dados SQL, recuperar informações relevantes usando vetores de embeddings, gerar contexto e produzir respostas através de um modelo de linguagem (LLM).

📌 Tecnologias principais

Backend: FastAPI

Frontend: React

Banco: SQLite 

RAG: SentenceTransformers + FAISS

Testes: Pytest

Este repositório foi criado para fins de estudo, demonstração técnica e entrega para avaliação.

📁 Estrutura do Projeto
rag-chat-project/
│
├── backend/
│   ├── main.py
│   ├── rag_pipeline.py
│   ├── database.py
│   ├── requirements.txt
│   └── tests/
│       └── test_api.py
│
└── frontend/
    ├── src/
    │   ├── App.jsx
    │   └── api.js
    ├── package.json
    └── public/

🔍 Arquitetura do Sistema
[React Frontend] 
       ↓ pergunta
[FastAPI Backend]
       ↓ consulta SQL
[Embeddings + FAISS Retrieval]
       ↓ contexto relevante
[LLM (Groq / Mistral / OpenAI / Ollama)]
       ↓ resposta
[Frontend exibe em tempo real]

🚀 Funcionalidades Principais
✔ Chat com respostas inteligentes
✔ Busca no banco SQL
✔ Recuperação vetorial via embeddings
✔ Pipeline RAG completo
✔ API em FastAPI com Swagger
✔ Frontend em React para interação
✔ Configuração plugável para diferentes provedores de LLM
✔ Testes com Pytest

⚙️ Tecnologias Utilizadas
Backend

FastAPI

Uvicorn

SQLAlchemy

SQLite

SentenceTransformers

FAISS

OpenAI API (opcional)

Groq API (recomendado)

Pytest

Frontend

React

Vite ou CRA

Axios

Tailwind (opcional)

🔍 Fluxo Completo RAG

Usuário envia uma pergunta pelo frontend

O backend consulta o banco SQL e busca registros relacionados

O texto é convertido em embeddings

FAISS encontra os vetores mais relevantes

O backend monta o contexto ideal

Envia para um LLM

O LLM produz a resposta final

O frontend exibe em tempo real

⚠️ Limitações no Ambiente de Teste

Durante o desenvolvimento, não foi possível executar e validar o backend (FastAPI) e o frontend (React) localmente, pois o computador utilizado possuía bloqueios de privacidade e políticas corporativas, afetando:

execução de scripts PowerShell

ativação do ambiente virtual venv

instalação de pacotes Python (pip)

execução de servidores (uvicorn, npm start)

Essas restrições impediram os testes locais completos, mas:

🔹 O código foi inteiramente escrito
🔹 A estrutura está completa para demonstração e avaliação


🤝 Contribuições

Contribuições são bem-vindas!
Para mudanças maiores, abra uma issue antes.

