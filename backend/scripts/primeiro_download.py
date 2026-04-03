"""
primeiro_download.py
--------------------
Baixa a mídia e lê a legenda de um post específico do Instagram.
Refatorado na Aula 8 para usar o módulo instaloader_client.

Aula 7 (refatorado na Aula 8) — Módulo 3: Script Core em Python
Curso: Instagram Downloader
"""

from pathlib import Path

from instaloader_client import buscar_post, carregar_sessao, criar_loader

# ─── Configurações ────────────────────────────────────────────────────────────

MINHA_CONTA = "seu_usuario"   # substitua pelo seu username
SHORTCODE   = "cole_o_shortcode_aqui"  # substitua pelo shortcode do post
PASTA_DOWNLOADS = Path("downloads")


def main():
    print("🏭 Criando o Instaloader...")
    L = criar_loader(download_midia=True)

    print(f"🔐 Carregando sessão de @{MINHA_CONTA}...")
    if not carregar_sessao(L, MINHA_CONTA):
        return
    print("✅ Sessão carregada com sucesso!")

    print(f"\n🔍 Buscando post com shortcode: {SHORTCODE}...")
    post = buscar_post(L, SHORTCODE)
    if post is None:
        return

    print("\n" + "=" * 60)
    print("📋 INFORMAÇÕES DO POST")
    print("=" * 60)
    print(f"  👤 Perfil:        @{post.owner_username}")
    print(f"  🗓️  Publicado em:  {post.date.strftime('%d/%m/%Y às %H:%M')} (UTC)")
    print(f"  🎬 Tipo:          {post.typename}")
    print(f"  🎥 É vídeo?       {'Sim' if post.is_video else 'Não'}")
    print(f"  ❤️  Curtidas:      {post.likes:,}")
    if post.caption:
        print(f"  📝 Legenda:\n     {post.caption[:200]}")
    else:
        print("  📝 Legenda:       (sem legenda)")
    print("=" * 60)

    pasta_destino = PASTA_DOWNLOADS / post.owner_username
    pasta_destino.mkdir(parents=True, exist_ok=True)

    print(f"\n⬇️  Baixando post para: {pasta_destino}/")
    L.download_post(post, target=pasta_destino)
    print("✅ Download concluído!")

    print(f"\n📁 Arquivos em {pasta_destino}/:")
    for arquivo in sorted(pasta_destino.iterdir()):
        tamanho_kb = arquivo.stat().st_size / 1024
        print(f"   {arquivo.name}  ({tamanho_kb:.1f} KB)")

    print("\n✅ Tudo certo!")


if __name__ == "__main__":
    main()