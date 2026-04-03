import bcrypt
from jose import jwt

from src.config.settings import configuracoes


ALGORITMO = "HS256"


def criar_hash_senha(senha: str) -> str:
    """Gera o hash bcrypt de uma senha."""
    salt = bcrypt.gensalt()
    return bcrypt.hashpw(senha.encode(), salt).decode()


def verificar_senha(senha: str, hash_senha: str) -> bool:
    """Verifica se uma senha corresponde ao hash armazenado."""
    return bcrypt.checkpw(senha.encode(), hash_senha.encode())


def criar_token_acesso(dados: dict) -> str:
    """Cria um token JWT de acesso."""
    return jwt.encode(dados, configuracoes.secret_key, algorithm=ALGORITMO)