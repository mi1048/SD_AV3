## Sumário

- [Visão Geral](#visão-geral)
- [Objetivos](#objetivos)
- [Recorte do Projeto](#recorte-do-projeto)
- [Arquitetura Distribuída](#arquitetura-distribuída)
- [Navegação e Experiência do Usuário](#navegação-e-experiência-do-usuário)
- [Estrutura e Organização do Código](#estrutura-e-organização-do-código)
- [Como Executar](#como-executar)
- [Banco de Dados](#banco-de-dados)
- [Docker](#docker)
- [Exemplos de Uso da API](#exemplos-de-uso-da-api)
- [Dicas](#dicas)
- [Ferramentas Utilizadas](#ferramentas-utilizadas)
- [Imagem no DockerHub](#imagem-no-dockerhub)

---

# SDPP_AV3_2 - QuizVerse

---

**Disciplina:** Sistemas Distribuídos e Programação Paralela  
**Docente:** Edson Mota da Cruz 
**Data:** 15/06/2025  
**Equipe:**  
- Rodrigo Dias Sarno
- Eric Menezes  

---
## Visão Geral

O **QuizVerse** é uma aplicação web distribuída para gerenciamento de quizzes educacionais em escolas. Cada "servidor" representa uma disciplina (ex: Matemática, História), permitindo que professores cadastrem perguntas e alunos respondam, acumulando pontos conforme o desempenho. O sistema foi modelado com princípios de arquitetura distribuída, orientação a objetos e SOLID, utilizando o padrão Model-View-Controller (MVC). Usuários podem se cadastrar, fazer login/logout, acessar servidores (matérias), responder perguntas e acompanhar sua pontuação, com persistência dos dados em MongoDB.

---

## Objetivos

- Demonstrar a modelagem de um sistema distribuído com múltiplos serviços complementares.
- Garantir separação de responsabilidades e modularidade do código (SOLID).
- Prover uma API RESTful para gerenciamento de usuários, servidores, perguntas e respostas.
- Persistir dados de forma segura e confiável usando MongoDB.
- Facilitar o deploy e a escalabilidade via conteinerização Docker.

---

## Recorte do Projeto

Neste recorte, o sistema foi pensado como uma plataforma de quizzes para escolas, onde:
- **Cada servidor representa uma disciplina** (ex: Matemática, História, Ciências).
- **Professores** podem cadastrar perguntas para suas matérias.
- **Alunos** podem se cadastrar, escolher uma disciplina, responder perguntas e acumular pontos.
- O sistema permite cadastro, login/logout de usuários, criação de servidores (matérias), cadastro e consulta de perguntas, envio de respostas e atualização de pontuação dos alunos.

---

## Arquitetura Distribuída

O sistema é composto por:
- **Serviço FastAPI**: expõe a API RESTful, responsável por toda a lógica de negócio.
- **Serviço MongoDB**: banco de dados NoSQL para persistência dos dados.

Ambos os serviços são conteinerizados e orquestrados via Docker Compose.  
O código está organizado em pacotes (controllers, services, models), promovendo separação de responsabilidades.

---

## Navegação e Experiência do Usuário

- A API pode ser explorada via [Swagger UI](http://localhost:8000/docs) após subir os containers.
- Endpoints disponíveis para usuários, servidores, perguntas e respostas.
- Fluxo típico: criar usuário → criar servidor → cadastrar perguntas → responder perguntas → ver pontuação.

---

## Estrutura e Organização do Código

```
app/
├── main.py                # Inicialização do FastAPI e inclusão das rotas
├── database.py            # Conexão com o MongoDB
├── controllers/           # Rotas da API (usuários, servidores, perguntas, respostas)
├── models/                # Modelos Pydantic e acesso às coleções do MongoDB
├── services/              # Lógica de negócio (serviços)
├── requisitos.txt         # Dependências Python
Dockerfile                 # Imagem Docker do serviço FastAPI
docker-compose.yml         # Orquestração dos serviços (FastAPI + MongoDB)
```
- **Separação clara** entre camadas de controle, serviço e modelo.
- **Princípios SOLID** aplicados na organização dos serviços e controllers.

---

## Como Executar

1. **Clone o repositório:**
   ```sh
   git clone <URL_DO_REPOSITORIO>
   cd SDPP_AV3_2
   ```

2. **Suba os containers:**
   ```sh
   docker-compose up --build
   ```

3. **Acesse a API:**
   - [http://localhost:8000/docs](http://localhost:8000/docs) (Swagger UI)
   - [http://localhost:8000/redoc](http://localhost:8000/redoc) (ReDoc)

4. **Utilize os métodos HTTP POST e GET:**
   - Utilize os comandos POST para criar os objetos e para enviar as suas respostas de acordo com a estrutura;
   - Utilize os comandos GET para receber informações em relação aos servidores que existem e as perguntas presentes em cada servidor;
   - Não foram criados métodos GET para os usuários para mantêr o sigilo deles.

5. **Verifique tudo através do MongoDB Compass:**
   A interface do MongoDB Compass é perfeita para visualizar o manuseio dos métodos POST e GET feitos no FastAPI, verificando o povoamento do banco em tempo real (utilize sempre o "Refresh" para verificar as atualizações)
---

## Banco de Dados

- MongoDB roda em container próprio, com volume nomeado para a persistência dos dados.
- Os dados não são perdidos entre reinicializações, exceto se o volume for removido manualmente.

---

## Docker

- Todos os serviços são conteinerizados.
- Basta rodar `docker-compose up --build` para iniciar o sistema completo.

---

## Exemplos de Uso da API

### Criar Pergunta

**Endpoint:**  
`POST /api/perguntas/`

**Exemplo de corpo da requisição (JSON):**
```json
{
  "servidor_id": "ID_DO_SERVIDOR",
  "enunciado": "INSIRA_O_ENUNCIADO_DA_QUESTAO_AQUI",
  "alternativas": [
    "ALTERNATIVA_1",
    "ALTERNATIVA_2",
    "ALTERNATIVA_3",
    "ALTERNATIVA_4"
  ],
  "resposta_correta": 0 
}
```
- `servidor_id`: O ID do servidor onde a pergunta será cadastrada (você pode obter usando o endpoint GET `/api/servidores/`) ou através do MongoDB Compass.
- `alternativas`: Lista de alternativas para a pergunta (mínimo de 1, máximo de 4).
- `resposta_correta`: Índice da alternativa correta (0 a 3).

---

### Responder Perguntas

**Endpoint:**  
`POST /api/respostas/`

**Exemplo de corpo da requisição (JSON):**
```json
{
  "usuario_nome": "nome_do_usuario",
  "servidor_id": "ID_DO_SERVIDOR",
  "respostas": {
    "ID_DA_PERGUNTA_1": 2,
    "ID_DA_PERGUNTA_2": 0
  }
}
```
- `usuario_nome`: Nome do usuário criado que está respondendo.
- `servidor_id`: ID do servidor.
- `respostas`: Um dicionário onde a chave é o ID da pergunta e o valor é o índice da alternativa escolhida.

---

## Dicas

- Use o Swagger UI ([http://localhost:8000/docs](http://localhost:8000/docs)).
- Para obter os IDs necessários, utilize os endpoints de listagem, como `GET /api/servidores/` e `GET /api/perguntas/{servidor_id}`.

---

## Ferramentas Utilizadas

- **FastAPI**: Framework web para APIs rápidas e modernas.
- **MongoDB**: Banco de dados NoSQL para persistência dos dados.
- **Docker & Docker Compose**: Conteinerização e orquestração dos serviços.
- **Docker Desktop**: Ambiente Docker local para Windows/Mac.
- **MongoDB Compass**: Interface gráfica para visualizar e manipular dados do MongoDB.
- **Python 3.11+**: Linguagem de programação principal do projeto.

## Imagem no DockerHub

```docker build test2313123/quizverse```
