from http import HTTPStatus
from sqlite3 import Connection
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from config.db import get_db_conn
from services.geocode import geocode

router = APIRouter(prefix='/distribuidores', tags=['distribuidores'])
t_conn = Annotated[Connection, Depends(get_db_conn)]


@router.get('/')
def busca_distribuidores(conn: t_conn, endereco=None, latitude=None, longitude=None):
    if endereco:
        latitude, longitude = geocode(endereco)

    if latitude is None or longitude is None:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='É necessário fornecer latitude e longitude ou um endereço',
        )

    cursor = conn.cursor()
    distribuidores = cursor.execute('SELECT * FROM distribuidores;').fetchall()
    return distribuidores
