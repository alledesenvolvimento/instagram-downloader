"""
buscar_dados.py
---------------
Busca e exibe todos os dados relevantes de um perfil público do Instagram.

Aula 6 — Módulo 2: Conhecendo o instaloader
Curso: Instagram Downloader
"""

import instaloader

# ─── Configurações ────────────────────────────────────────────────────────────

# Conta secundária que você usa para autenticar (sem @)
MINHA_CONTA = "amanda_souto2025"

# Perfil público que vamos buscar (sem @)
PERFIL_ALVO = "natgeo"

# ─── Funções ──────────────────────────────────────────────────────────────────


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


# ─── Ponto de entrada ──────────────────────────────────────────────────────────

def main():
    # 1. Cria o Instaloader
    print("🏭 Criando o Instaloader...")
    L = instaloader.Instaloader(quiet=True)

    # 2. Carrega a sessão
    print(f"🔐 Carregando sessão de @{MINHA_CONTA}...")
    try:
        L.load_session_from_file(MINHA_CONTA)
        print("✅ Sessão carregada com sucesso!")
    except FileNotFoundError:
        print(f"❌ Arquivo de sessão não encontrado para @{MINHA_CONTA}.")
        print("   Execute o Passo 4 da Aula 5 para gerar o arquivo de sessão.")
        return

    # 3. Busca o perfil
    print(f"\n🔍 Buscando perfil @{PERFIL_ALVO}...")
    try:
        perfil = instaloader.Profile.from_username(L.context, PERFIL_ALVO)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"❌ Perfil @{PERFIL_ALVO} não encontrado.")
        return

    # 4. Exibe os dados
    exibir_dados_perfil(perfil)

    print("\n✅ Busca concluída!")


if __name__ == "__main__":
    main()