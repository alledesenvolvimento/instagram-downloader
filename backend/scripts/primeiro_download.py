"""
primeiro_download.py
--------------------
Baixa a mídia e lê a legenda de um post específico do Instagram
usando o shortcode do post.

Aula 7 — Módulo 2: Conhecendo o instaloader
Curso: Instagram Downloader
"""

import instaloader
from pathlib import Path

# ─── Configurações ────────────────────────────────────────────────────────────

# Conta secundária que você usa para autenticar (sem @)
MINHA_CONTA = "teste_user1"

# Shortcode do post que você quer baixar
# Cole aqui o shortcode que você copiou da URL do post
SHORTCODE = "DWpR3s0ieLx"

# Pasta onde os arquivos vão ser salvos
PASTA_DOWNLOADS = Path("downloads")

# ─── Ponto de entrada ──────────────────────────────────────────────────────────


def main():
    # 1. Cria o Instaloader com apenas o necessário ligado
    print("🏭 Criando o Instaloader...")
    L = instaloader.Instaloader(
        download_pictures=True,
        download_videos=True,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        post_metadata_txt_pattern="",
        quiet=True,
    )

    # 2. Carrega a sessão
    print(f"🔐 Carregando sessão de @{MINHA_CONTA}...")
    try:
        L.load_session_from_file(MINHA_CONTA)
        print("✅ Sessão carregada com sucesso!")
    except FileNotFoundError:
        print(f"❌ Arquivo de sessão não encontrado para @{MINHA_CONTA}.")
        print("   Execute o Passo 4 da Aula 5 para gerar o arquivo de sessão.")
        return

    # 3. Busca o post pelo shortcode
    print(f"\n🔍 Buscando post com shortcode: {SHORTCODE}...")
    try:
        post = instaloader.Post.from_shortcode(L.context, SHORTCODE)
    except Exception as e:
        print(f"❌ Não foi possível encontrar o post: {e}")
        return

    # 4. Exibe as informações do post antes de baixar
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

    # 5. Baixa o post
    pasta_destino = PASTA_DOWNLOADS / post.owner_username
    pasta_destino.mkdir(parents=True, exist_ok=True)

    print(f"\n⬇️  Baixando post para: {pasta_destino}/")
    L.download_post(post, target=pasta_destino)
    print("✅ Download concluído!")

    # 6. Lista os arquivos baixados
    print(f"\n📁 Arquivos em {pasta_destino}/:")
    for arquivo in sorted(pasta_destino.iterdir()):
        tamanho_kb = arquivo.stat().st_size / 1024
        print(f"   {arquivo.name}  ({tamanho_kb:.1f} KB)")

    print("\n✅ Tudo certo!")


if __name__ == "__main__":
    main()