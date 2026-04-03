"""
buscar_dados.py
---------------
Busca e exibe todos os dados relevantes de um perfil público do Instagram.
Refatorado na Aula 8 para usar o módulo instaloader_client.

Aula 6 (refatorado na Aula 8) — Módulo 3: Script Core em Python
Curso: Instagram Downloader
"""

import instaloader
from instaloader_client import buscar_perfil, carregar_sessao, criar_loader

# ─── Configurações ────────────────────────────────────────────────────────────

MINHA_CONTA = "seu_usuario"   # substitua pelo seu username
PERFIL_ALVO = "nasa"


def exibir_dados_perfil(perfil: instaloader.Profile) -> None:
    """Exibe todos os dados relevantes de um perfil no terminal."""

    print("\n" + "=" * 60)
    print("👤 IDENTIFICAÇÃO")
    print("=" * 60)
    print(f"  🔑 Username:      @{perfil.username}")
    print(f"  📛 Nome completo: {perfil.full_name or '(não informado)'}")
    print(f"  🆔 ID do perfil:  {perfil.userid}")

    print("\n" + "=" * 60)
    print("📝 SOBRE O PERFIL")
    print("=" * 60)
    if perfil.biography:
        print(f"  📄 Bio:\n     {perfil.biography}")
    else:
        print("  📄 Bio:           (sem bio)")

    if perfil.external_url:
        print(f"  🔗 Link externo:  {perfil.external_url}")
    else:
        print("  🔗 Link externo:  (sem link)")

    print(f"  🔒 É privado?     {'Sim' if perfil.is_private else 'Não'}")
    print(f"  ✅ É verificado?  {'Sim' if perfil.is_verified else 'Não'}")
    print(f"  🏢 É comercial?   {'Sim' if perfil.is_business_account else 'Não'}")

    print("\n" + "=" * 60)
    print("📊 NÚMEROS")
    print("=" * 60)
    print(f"  👥 Seguidores:    {perfil.followers:,}")
    print(f"  👣 Seguindo:      {perfil.followees:,}")
    print(f"  📸 Total de posts:{perfil.mediacount:,}")

    print("\n" + "=" * 60)
    print("🖼️  IMAGEM")
    print("=" * 60)
    print(f"  🔗 Foto de perfil: {perfil.profile_pic_url}")

    print("\n" + "=" * 60)


def main():
    print("🏭 Criando o Instaloader...")
    L = criar_loader()

    print(f"🔐 Carregando sessão de @{MINHA_CONTA}...")
    if not carregar_sessao(L, MINHA_CONTA):
        return
    print("✅ Sessão carregada com sucesso!")

    print(f"\n🔍 Buscando perfil @{PERFIL_ALVO}...")
    perfil = buscar_perfil(L, PERFIL_ALVO)
    if perfil is None:
        return

    exibir_dados_perfil(perfil)
    print("\n✅ Busca concluída!")


if __name__ == "__main__":
    main()