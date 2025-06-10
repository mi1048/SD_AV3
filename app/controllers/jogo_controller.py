@rota.post("/servidores/{servidor_id}/responder")
async def responder_pergunta(
    servidor_id: str,
    resposta: dict  # {usuario: str, pergunta_id: str, alternativa: str}
):
# Lógica para validar resposta e atualizar pontuação