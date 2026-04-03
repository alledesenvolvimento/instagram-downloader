class ErroDeNegocio(Exception):
    """Classe base para todos os erros de domínio."""

    def __init__(self, mensagem: str) -> None:
        self.mensagem = mensagem
        super().__init__(mensagem)


class RecursoNaoEncontrado(ErroDeNegocio):
    """Recurso solicitado não existe."""
    pass


class RequisicaoInvalida(ErroDeNegocio):
    """Dados fornecidos são inválidos para a operação."""
    pass