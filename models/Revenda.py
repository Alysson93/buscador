from pydantic import BaseModel


class Revenda(BaseModel):
    id: int
    nome: str
    cnpj: str
    pais: str
    estado: str
    cidade: str
    bairro: str
    rua: str
    numero: str
    cep: str
    latitude: float
    longitude: float
    telefone: str
    email: str
    cnpj_distribuidor: str
