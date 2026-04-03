"""
baixar_perfil.py
----------------
Baixa os posts mais recentes de um perfil público do Instagram
e os organiza em pastas separadas por post, nomeadas com o shortcode.

Aula 9 — Módulo 3: Script Core em Python
Curso: Instagram Downloader
"""

from itertools import islice
from pathlib import Path

from instaloader_client import buscar_perfil, carregar_sessao, criar_loader

# ─── Configurações ────────────────────────────────────────────────────────────

MINHA_CONTA = "seu_usuario"   # substitua pelo seu username
PERFIL_ALVO     = "nasa"
LIMITE_POSTS    = 3               # quantos posts baixar
PASTA_DOWNLOADS = Path("downloads")


# ─── Funções ──────────────────────────────────────────────────────────────────


def renomear_arquivos(pasta_post: Path) -> None:
    """Renomeia os arquivos baixados para nomes simples e previsíveis."""
    contador_foto = 1
    contador_video = 1

    for arquivo in sorted(pasta_post.iterdir()):
        sufixo = arquivo.suffix.lower()

        if sufixo == ".jpg":
            novo_nome = pasta_post / f"foto_{contador_foto}.jpg"
            if not novo_nome.exists():
                arquivo.rename(novo_nome)
            contador_foto += 1

        elif sufixo == ".mp4":
            novo_nome = pasta_post / f"video_{contador_video}.mp4"
            if not novo_nome.exists():
                arquivo.rename(novo_nome)
            contador_video += 1


def baixar_post(L, post, pasta_perfil: Path) -> Path:
    """
    Baixa um post e o salva em uma subpasta nomeada com o shortcode.
    Se a pasta já existe e já tem arquivos, pula o download.
    Retorna o caminho da pasta criada.
    """
    pasta_post = pasta_perfil / post.shortcode

    # Se a pasta já existe e já tem arquivos, pula o download
    if pasta_post.exists() and any(pasta_post.iterdir()):
        return pasta_post

    pasta_post.mkdir(parents=True, exist_ok=True)
    L.download_post(post, target=pasta_post)
    renomear_arquivos(pasta_post)

    return pasta_post


# ─── Ponto de entrada ──────────────────────────────────────────────────────────


def main():
    print("🏭 Criando o Instaloader...")
    L = criar_loader(download_midia=True)

    print(f"🔐 Carregando sessão de @{MINHA_CONTA}...")
    if not carregar_sessao(L, MINHA_CONTA):
        return
    print("✅ Sessão carregada com sucesso!")

    print(f"\n🔍 Buscando perfil @{PERFIL_ALVO}...")
    perfil = buscar_perfil(L, PERFIL_ALVO)
    if perfil is None:
        return

    print(f"✅ Perfil encontrado: {perfil.full_name} ({perfil.mediacount:,} posts)")

    pasta_perfil = PASTA_DOWNLOADS / perfil.username
    pasta_perfil.mkdir(parents=True, exist_ok=True)

    print(f"\n⬇️  Baixando os últimos {LIMITE_POSTS} posts de @{PERFIL_ALVO}...\n")

    for i, post in enumerate(islice(perfil.get_posts(), LIMITE_POSTS), start=1):
        print(f"  [{i}/{LIMITE_POSTS}] {post.shortcode} — {post.typename} ({post.date.strftime('%d/%m/%Y')})")

        pasta_post = baixar_post(L, post, pasta_perfil)

        arquivos = sorted(pasta_post.iterdir())
        for arquivo in arquivos:
            tamanho_kb = arquivo.stat().st_size / 1024
            print(f"         💾 {arquivo.name}  ({tamanho_kb:.1f} KB)")

    print(f"\n✅ Download concluído! Arquivos em: {pasta_perfil}/")
    print("\n📁 Estrutura final:")
    for pasta_post in sorted(pasta_perfil.iterdir()):
        if pasta_post.is_dir():
            print(f"   {pasta_post.name}/")
            for arquivo in sorted(pasta_post.iterdir()):
                print(f"      {arquivo.name}")


if __name__ == "__main__":
    main()