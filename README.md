# SD_AV3
Trabalho de Sistemas Distribuidos e Programacao Paralela

# Dicas
1)Tabela de palavras e símbolos reservados (vai estar gravadas)

Sempre que colocar caracteres verificar se sequencia de caracteres estão nas palavras e símbolos reservados

Ler o que ele quer na tabela de palavras e símbolos reservados

2)Tabela de símbolos (identificadores)

Depois que verificar que não esta reservado na tabela de palavras e símbolos reservados popular a tabela de símbolos seguindo as regras dos identificadores.

Ler o que ele quer na tabela de símbolos onde tem os identificadores


# Analise Lexica

## 2.Divisao do trabalho do analisador léxico
- Scanneamento Lexico:Separacao e montagem das partes
- Analise Lexica:Analise sobre as partes montadas(Qualquer coisa que não seja no padrao)ESSA QUE ELE QUER
# Filtros

NO TRABALHO TODO CARACTERE INVALIDO NA LINGUAGEM(CARACTERE QUE NAO ESTA SENDO USADO PARA MONTAR QUALQUER ATOMO DA LINGUAGEM) VOCE ELEMINA NO PROCESSO DE MONATEGEM

COMENTARIO DE BLOCO:
INICIA /*
TERMINA */ OU ATE FIM DE ARQUIVO

COMENTARIO DE LINHA
COMECA COM //
TERMINA COM FIM DA LINHA(\n) OU FIM DE ARQUIVO

## 3.Filtrar caracteres no texto fonte(Filtragem de primeiro nivel) ESSA ELE QUER
- Elimina caracteres durante a montagem dos atomos
- Nao chegam a ser consideradas na analise lexica
- Filtragem x erros lexicos decisao de cada implementacao
  
## 4.Remover construcao nao relevantes(Filtragem de segundo nivel) ESSA ELE QUER
- Exemplo: comentarios, espacos em branco
- Sao considerados na analise lexica como delimitadores
- Nao sao passados para as fases posteriores

. e
