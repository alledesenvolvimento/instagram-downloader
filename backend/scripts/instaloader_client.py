"""
instaloader_client.py
---------------------
Módulo central com funções reutilizáveis do instaloader.

Todas as operações comuns — criar o Instaloader, carregar sessão,
buscar perfil e buscar post — ficam aqui para evitar repetição
nos scripts que usam a biblioteca.

Atualizado na Aula 11 — tratamento de erros robusto.

Módulo 3 — Script Core em Python
Curso: Instagram Downloader
"""

import instaloader


def criar_loader(download_midia: bool = False) -> instaloader.Instaloader:
    """
    Cria e retorna uma instância configurada do Instaloader.

    Parâmetros:
        download_midia: se True, habilita o download de fotos e vídeos.
                        se False, só busca metadados (padrão).
    """
    return instaloader.Instaloader(
        download_pictures=download_midia,
        download_videos=download_midia,
        download_video_thumbnails=False,
        download_geotags=False,
        download_comments=False,
        save_metadata=False,
        post_metadata_txt_pattern="",
        quiet=True,
    )


def carregar_sessao(L: instaloader.Instaloader, conta: str) -> bool:
    """
    Carrega o arquivo de sessão salvo para a conta informada.

    Retorna True se a sessão foi carregada com sucesso, False caso contrário.
    """
    try:
        L.load_session_from_file(conta)
        return True
    except FileNotFoundError:
        print(f"❌ Arquivo de sessão não encontrado para @{conta}.")
        print("   Execute o Passo 4 da Aula 5 para gerar o arquivo de sessão.")
        return False


def buscar_perfil(
    L: instaloader.Instaloader, username: str
) -> instaloader.Profile | None:
    """
    Busca e retorna o objeto Profile para o username informado.

    Retorna None se o perfil não for encontrado.
    Informa se o perfil é privado.
    """
    try:
        perfil = instaloader.Profile.from_username(L.context, username)

        if perfil.is_private:
            print(f"🔒 O perfil @{username} é privado.")
            print("   Só é possível baixar posts de perfis que você segue com a conta de sessão.")
            return None

        return perfil

    except instaloader.exceptions.ProfileNotExistsException:
        print(f"❌ Perfil @{username} não encontrado.")
        return None

    except instaloader.exceptions.ConnectionException as e:
        print(f"❌ Erro de conexão ao buscar @{username}: {e}")
        return None


def buscar_post(
    L: instaloader.Instaloader, shortcode: str
) -> instaloader.Post | None:
    """
    Busca e retorna o objeto Post para o shortcode informado.

    Retorna None se o post não for encontrado.
    """
    try:
        return instaloader.Post.from_shortcode(L.context, shortcode)
    except instaloader.exceptions.ProfileNotExistsException:
        print(f"❌ Post com shortcode '{shortcode}' não encontrado.")
        return None
    except instaloader.exceptions.ConnectionException as e:
        print(f"❌ Erro de conexão ao buscar o post '{shortcode}': {e}")
        return None
    except Exception as e:
        print(f"❌ Erro inesperado ao buscar o post '{shortcode}': {e}")
        return None