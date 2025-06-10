class Pergunta(BaseModel):
    id: str
    servidor_id: str  # ID do servidor temático
    enunciado: str
    alternativas: list  # Ex: ["A) Opção 1", "B) Opção 2"]
    resposta_correta: str  # Letra da alternativa correta
    nivel_dificuldade: int  # 1-5
    tempo_resposta: int  # Segundos