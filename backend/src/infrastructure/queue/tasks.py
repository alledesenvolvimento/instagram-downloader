async def baixar_perfil(ctx: dict, perfil_id: str, username: str) -> dict:
    """
    Job ARQ: processa o download de um perfil do Instagram em background.
    Implementação completa na Aula 22.
    """
    print(f"[worker] Iniciando download do perfil @{username}...")
    # TODO: implementar na Aula 22
    return {"status": "pendente", "perfil_id": perfil_id}