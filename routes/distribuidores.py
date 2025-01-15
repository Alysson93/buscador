from http import HTTPStatus
from sqlite3 import Connection
from typing import Annotated

from fastapi import APIRouter, Depends, HTTPException

from config.db import get_db_conn
from services.geocode import geocode
from services.valida_input import is_valid_lat_lon

router = APIRouter(prefix='/distribuidores', tags=['distribuidores'])
t_conn = Annotated[Connection, Depends(get_db_conn)]


@router.get('/')
def busca_distribuidores(conn: t_conn, endereco=None):  
    if endereco:
        coordenadas = is_valid_lat_lon(endereco)
        if coordenadas:
            latitude, longitude = coordenadas
        else:
            latitude, longitude = geocode(endereco)
        cursor = conn.cursor()
        distribuidores = cursor.execute(
            'SELECT *, sqrt(pow(latitude - :x, 2) + pow(longitude - :y, 2)) AS distance FROM distribuidores ORDER BY distance LIMIT 5;'
        , {'x': latitude, 'y': longitude}).fetchall()
        return distribuidores
    else:
        raise HTTPException(
            status_code=HTTPStatus.NOT_FOUND,
            detail='É necessário fornecer latitude e longitude ou um endereço',
        )
