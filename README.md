# SD_AV3
Trabalho de Sistemas Distribuidos e Programacao Paralela

# Equipe

- Eric Menezes
- Rodrigo Dias Sarno


# Sobre o tema do trabalho

A Escolha do Tema proposta pela equipe para o projeto foi de um jogo de quiz, ou seja um jogo de pergunta e respostas.Aonde o usuario recebera a resposta e tera alternativas para escolher onde apenas uma e a correta.

# Nome do trabalho
?


▪ Usem a criatividade, vocês estão em um ambiente cercado de inovação.
Essa é uma boa oportunidade para por em prática os conhecimentos
práticos das disciplinas.
▪ Se o projeto pensado se mostrar grande demais, trabalhe em um
recorte. Nesse caso, apenas defina e descreva no canvas, de forma
clara, o recorte no qual a equipe vai atuar.


# Sistemas de Jogos API

API voltada para gerenciamento usuários, clientes e servidores com perguntas de conteúdos exclusivos, juntamente com o MongoDB.

# Pré-Requisitos:

- Python 3.8+
- MongoDB instalado localmente
- Pip (gerenciador de pacotes Python)

--------------------------------------------------------------------------------------------------------------------------------------------------------------------
(TUDO ABAIXO É UM RASCUNHO)
# Instalação

1. Clone o repositório:
```bash
git clone [URL_DO_REPOSITORIO]
cd nome-do-repositorio

2. Instale as dependências:
pip install -r requisitos.txt

3. Inicie o servidor MongoDB (feito no Windows):
net start MongoDB


# Execução

1. Inicie a API:
uvicorn app.main:app --reload

2. Acesse a documentação interativa com o link abaixo:
http://localhost:8000/docs


# Teste Básico & Verificação no MongoDB

1. Acesse http://localhost:8000/docs

2. Expanda a seção POST /api/usuarios/

3. Clique em "Try it out"

4. Modifique o JSON exemplo:

{
  "nome": "novo_usuario",
  "senha": "senha123"
}

5. Clique em "Execute". Se aparecer a resposta 200, então ocorreu com sucesso.

6. Abra o MongoDB Compass

7. Conecte-se a mongodb://localhost:27017

8. Acesse o banco sistema_jogos

9. Verifique a coleção usuarios. Se aparecer lá, então ocorreu com sucesso.
