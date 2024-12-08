from fastapi import FastAPI, UploadFile, File, Form, Depends
from typing import Optional
from pydantic import BaseModel
import shutil
import os
import uuid
import orm.repo as repo  # Para hacer consultas a la BD
from sqlalchemy.orm import Session
from orm.config import generador_session  # Generador de sesiones

# Creación del servidor
app = FastAPI()

# Clase base para alumno
class AlumnoBase(BaseModel):
    nombre: Optional[str] = None
    edad: int
    domicilio: str
    carrera: str
    trimestre: str
    email: str

# Ruta base
@app.get("/")
def hola_mundo():
    print("Invocando a ruta /")
    respuesta = {
        "mensaje": "¡Hola mundo!"
    }
    return respuesta

# ---------- Consultas a Alumnos ----------

@app.get("/alumnos")
def lista_alumnos(sesion: Session = Depends(generador_session)):
    print("API consultando todos los alumnos")
    return repo.lista_alumnos(sesion)

@app.get("/alumnos/{id}")
def alumno_por_id(id: int, sesion: Session = Depends(generador_session)):
    print(f"API consultando alumno con id: {id}")
    return repo.alumno_por_id(sesion, id)

@app.delete("/alumnos/{id}")
def borrar_alumno(id: int, sesion: Session = Depends(generador_session)):
    print(f"API eliminando alumno con id: {id}")
    return repo.borra_alumno_por_id(sesion, id)

# ---------- Consultas a Calificaciones ----------

@app.get("/calificaciones/{id}")
def calificacion_por_id(id: int, sesion: Session = Depends(generador_session)):
    print(f"API consultando calificación con id: {id}")
    return repo.calificacion_por_id(sesion, id)

@app.get("/alumnos/{id}/calificaciones")
def calificaciones_por_alumno(id: int, sesion: Session = Depends(generador_session)):
    print(f"API consultando calificaciones del alumno con id: {id}")
    return repo.calificaciones_por_id_alumno(sesion, id)

@app.delete("/calificaciones/{id}")
def borrar_calificacion(id: int, sesion: Session = Depends(generador_session)):
    print(f"API eliminando calificación con id: {id}")
    return repo.borra_calificacion_por_id(sesion, id)

@app.delete("/alumnos/{id}/calificaciones")
def borrar_calificaciones_por_alumno(id: int, sesion: Session = Depends(generador_session)):
    print(f"API eliminando calificaciones del alumno con id: {id}")
    return repo.borra_calificaciones_por_id_alumno(sesion, id)

# ---------- Consultas a Fotos ----------

@app.get("/fotos/{id}")
def foto_por_id(id: int, sesion: Session = Depends(generador_session)):
    print(f"API consultando foto con id: {id}")
    return repo.foto_por_id(sesion, id)

@app.get("/alumnos/{id}/fotos")
def fotos_por_alumno(id: int, sesion: Session = Depends(generador_session)):
    print(f"API consultando fotos del alumno con id: {id}")
    return repo.fotos_por_id_alumno(sesion, id)

@app.delete("/fotos/{id}")
def borrar_foto(id: int, sesion: Session = Depends(generador_session)):
    print(f"API eliminando foto con id: {id}")
    return repo.borra_foto_por_id(sesion, id)

@app.delete("/alumnos/{id}/fotos")
def borrar_fotos_por_alumno(id: int, sesion: Session = Depends(generador_session)):
    print(f"API eliminando fotos del alumno con id: {id}")
    return repo.borra_fotos_por_id_alumno(sesion, id)

