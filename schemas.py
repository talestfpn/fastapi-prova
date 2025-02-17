from pydantic import BaseModel

class EmpresaBase(BaseModel):
    nome: str
    cnpj: str
    endereco: str | None = None
    email: str | None = None
    telefone: str | None = None

class EmpresaCreate(EmpresaBase):
    pass

class Empresa(EmpresaBase):
    id: int

    class ConfigDict:
        from_attributes = True

class ObrigacaoAcessoriaBase(BaseModel):
    nome: str
    periodicidade: str
    empresa_id: int

class ObrigacaoAcessoriaCreate(ObrigacaoAcessoriaBase):
    pass

class ObrigacaoAcessoria(ObrigacaoAcessoriaBase):
    id: int

    class ConfigDict:
        from_attributes = True