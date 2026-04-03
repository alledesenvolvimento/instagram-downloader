"""
Aula 5 — Explorando o instaloader
"""

import instaloader


def main():
    print("🏭 Criando o Instaloader...")
    L = instaloader.Instaloader()

    username = "teste_user1"

    print(f"🔐 Carregando sessão salva para @{username}...")
    try:
        L.load_session_from_file(username)
    except FileNotFoundError:
        print("❌ Arquivo de sessão não encontrado.")
        return

    print("✅ Sessão carregada!")

    perfil_alvo = "teste_user2"
    print(f"\n🔍 Buscando perfil @{perfil_alvo}...")
    try:
        perfil = instaloader.Profile.from_username(L.context, perfil_alvo)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"❌ Perfil @{perfil_alvo} não encontrado.")
        return

    print("\n" + "=" * 50)
    print(f"👤 Username:       @{perfil.username}")
    print(f"📛 Nome completo:  {perfil.full_name}")
    print(f"👥 Seguidores:     {perfil.followers:,}")
    print(f"📸 Total de posts: {perfil.mediacount:,}")
    print(f"🔒 É privado?      {'Sim' if perfil.is_private else 'Não'}")
    print("=" * 50)

    print("\n✅ Exploração concluída!")


if __name__ == "__main__":
    main()