import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ---------- Peticiones a Alumnos ----------

def lista_alumnos(sesion: Session):
    print("Select * from alumnos")
    return sesion.query(modelos.Alumno).all()

def alumno_por_id(sesion: Session, id_alumno: int):
    print("Select * from alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

# DELETE '/alumnos/{id}'
# delete from alumnos where id = id_alumno
def borra_alumno_por_id(sesion: Session, id_alumno: int):
    print("# delete from alumnos where id = ", id_alumno)
    alumno = alumno_por_id(sesion, id_alumno)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
    respuesta = {
        "mensaje": "Alumno eliminado"
    }
    return respuesta

# ---------- Peticiones a Calificaciones ----------

def calificacion_por_id(sesion: Session, id_calificacion: int):
    print("Select * from calificaciones where id = ", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

def lista_calificaciones(sesion: Session):
    print("Select * from calificaciones")
    return sesion.query(modelos.Calificacion).all()

# Buscar calificaciones por id de alumno
# GET '/alumnos/{id}/calificaciones'
# select * from calificaciones where id_alumno = id_alumno
def calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("Select * from calificaciones where id_alumno = ", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()

# DELETE '/calificaciones/{id}'
# delete from calificaciones where id = id_calificacion
def borra_calificacion_por_id(sesion: Session, id_calificacion: int):
    print("# delete from calificaciones where id = ", id_calificacion)
    calificacion = calificacion_por_id(sesion, id_calificacion)
    if calificacion is not None:
        sesion.delete(calificacion)
        sesion.commit()
    respuesta = {
        "mensaje": "Calificación eliminada"
    }
    return respuesta

# DELETE '/alumnos/{id}/calificaciones'
# delete from calificaciones where id_alumno = id_alumno
def borra_calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("# delete from calificaciones where id_alumno = ", id_alumno)
    calificaciones = calificaciones_por_id_alumno(sesion, id_alumno)
    for calificacion in calificaciones:
        sesion.delete(calificacion)
    sesion.commit()
    respuesta = {
        "mensaje": "Calificaciones eliminadas"
    }
    return respuesta

# ---------- Peticiones a Fotos ----------

def foto_por_id(sesion: Session, id_foto: int):
    print("Select * from fotos where id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

def lista_fotos(sesion: Session):
    print("Select * from fotos")
    return sesion.query(modelos.Foto).all()

# Buscar fotos por id de alumno
# GET '/alumnos/{id}/fotos'
# select * from fotos where id_alumno = id_alumno
def fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("Select * from fotos where id_alumno = ", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumno).all()

# DELETE '/fotos/{id}'
# delete from fotos where id = id_foto
def borra_foto_por_id(sesion: Session, id_foto: int):
    print("# delete from fotos where id = ", id_foto)
    foto = foto_por_id(sesion, id_foto)
    if foto is not None:
        sesion.delete(foto)
        sesion.commit()
    respuesta = {
        "mensaje": "Foto eliminada"
    }
    return respuesta

# DELETE '/alumnos/{id}/fotos'
# delete from fotos where id_alumno = id_alumno
def borra_fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("# delete from fotos where id_alumno = ", id_alumno)
    fotos = fotos_por_id_alumno(sesion, id_alumno)
    for foto in fotos:
        sesion.delete(foto)
    sesion.commit()
    respuesta = {
        "mensaje": "Fotos eliminadas"
    }
    return respuesta
