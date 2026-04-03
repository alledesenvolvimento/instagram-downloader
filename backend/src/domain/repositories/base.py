from abc import ABC, abstractmethod
from uuid import UUID

from ..entities.base import EntidadeBase


class RepositorioBase(ABC):
    """Interface base para todos os repositórios."""

    @abstractmethod
    async def buscar_por_id(self, id: UUID) -> EntidadeBase | None:
        raise NotImplementedError

    @abstractmethod
    async def salvar(self, entidade: EntidadeBase) -> EntidadeBase:
        raise NotImplementedError