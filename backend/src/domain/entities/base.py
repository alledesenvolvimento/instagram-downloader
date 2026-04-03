from dataclasses import dataclass, field
from datetime import datetime
from uuid import UUID, uuid4


@dataclass
class EntidadeBase:
    """Classe base para todas as entidades de domínio."""

    id: UUID = field(default_factory=uuid4)
    criado_em: datetime = field(default_factory=datetime.utcnow)
    atualizado_em: datetime = field(default_factory=datetime.utcnow)