from pydantic_settings import BaseSettings


class Configuracoes(BaseSettings):
    """
    Configurações da aplicação lidas do arquivo .env.
    Todas as variáveis são obrigatórias — a aplicação não sobe sem elas.
    """

    # Servidor
    port: int = 8300
    environment: str = "development"

    # Banco de dados
    postgres_host: str
    postgres_port: int
    postgres_user: str
    postgres_password: str
    postgres_db: str

    # Redis
    redis_url: str

    # Segurança
    secret_key: str = "chave-secreta-local-trocar-em-producao"

    @property
    def database_url(self) -> str:
        """URL de conexão assíncrona com o PostgreSQL."""
        return (
            f"postgresql+asyncpg://{self.postgres_user}:{self.postgres_password}"
            f"@{self.postgres_host}:{self.postgres_port}/{self.postgres_db}"
        )

    class Config:
        env_file = ".env"
        env_file_encoding = "utf-8"


configuracoes = Configuracoes()