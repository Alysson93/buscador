from http import HTTPStatus
from sqlite3 import Connection
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from config.db import get_db_conn
from services.geocode import geocode

router = APIRouter(prefix='/revendas', tags=['revendas'])
t_conn = Annotated[Connection, Depends(get_db_conn)]


@router.get('/')
def busca_revendas(conn: t_conn, endereco=None):
    if endereco:    
        geolocal = geocode(endereco)
        return geolocal
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='É necessário fornecer latitude e longitude ou um endereço',
        )
