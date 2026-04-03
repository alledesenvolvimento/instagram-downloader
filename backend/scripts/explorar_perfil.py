"""
explorar_perfil.py
------------------
Explora os principais objetos e conceitos do instaloader.
Refatorado na Aula 8 para usar o módulo instaloader_client.

Aula 5 (refatorado na Aula 8) — Módulo 3: Script Core em Python
Curso: Instagram Downloader
"""

import instaloader
from instaloader_client import buscar_perfil, carregar_sessao, criar_loader

# ─── Configurações ────────────────────────────────────────────────────────────

MINHA_CONTA = "seu_usuario"   # substitua pelo seu username
PERFIL_ALVO = "nasa"


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

    print("\n" + "=" * 50)
    print("📋 INFORMAÇÕES DO PERFIL")
    print("=" * 50)
    print(f"👤 Username:       @{perfil.username}")
    print(f"📛 Nome completo:  {perfil.full_name}")
    print(f"📝 Bio:            {perfil.biography[:80]}...")
    print(f"👥 Seguidores:     {perfil.followers:,}")
    print(f"📸 Total de posts: {perfil.mediacount:,}")
    print(f"🔒 É privado?      {'Sim' if perfil.is_private else 'Não'}")
    print(f"✅ É verificado?   {'Sim' if perfil.is_verified else 'Não'}")
    print("=" * 50)

    print("\n🔍 Buscando o post mais recente...")
    try:
        post = next(perfil.get_posts())
        print("\n" + "=" * 50)
        print("📸 POST MAIS RECENTE")
        print("=" * 50)
        print(f"🗓️  Publicado em:  {post.date.strftime('%d/%m/%Y às %H:%M')}")
        print(f"🎬 Tipo de mídia: {post.typename}")
        print(f"❤️  Curtidas:      {post.likes:,}")
        if post.caption:
            print(f"📝 Legenda:       {post.caption[:120]}...")
        else:
            print("📝 Legenda:       (sem legenda)")
        print("=" * 50)
    except StopIteration:
        print("⚠️  Este perfil não tem posts.")

    print("\n✅ Exploração concluída!")


if __name__ == "__main__":
    main()