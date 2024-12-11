import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_

# ---------- Peticiones a Alumnos ----------

# SELECT * FROM app.alumnos
# GET '/alumnos'
def lista_alumnos(sesion: Session):
    print("Select * from alumnos") 
    return sesion.query(modelos.Alumno).all()

# SELECT * FROM app.alumnos WHERE id={id_al}
# GET '/alumnos/{id}'
def alumno_por_id(sesion: Session, id_alumno: int):
    print("Select * from alumnos where id = ", id_alumno)
    return sesion.query(modelos.Alumno).filter(modelos.Alumno.id == id_alumno).first()

# DELETE FROM app.alumnos WHERE id_alumnos={id_al}
# DELETE '/alumnos/{id}'
def borra_alumno_por_id(sesion: Session, id_alumno: int):
    print("Delete from alumnos where id = ", id_alumno)
    borra_calificaciones_por_id_alumno(sesion, id_alumno)
    borra_fotos_por_id_alumno(sesion, id_alumno)
    alumno = alumno_por_id(sesion, id_alumno)
    if alumno is not None:
        sesion.delete(alumno)
        sesion.commit()
    respuesta = {
        "mensaje": "Alumno eliminado"
    }
    return respuesta

# ---------- Peticiones a Calificaciones ----------

# SELECT * FROM app.calificaciones
# GET '/calificaciones'
def lista_calificaciones(sesion: Session):
    print("Select * from calificaciones")
    return sesion.query(modelos.Calificacion).all()

# SELECT * FROM app.calificaciones WHERE id={id_ca}
# GET '/calificaciones/{id}'
def calificacion_por_id(sesion: Session, id_calificacion: int):
    print("Select * from calificaciones where id = ", id_calificacion)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id == id_calificacion).first()

# SELECT * FROM app.calificaciones WHERE id_alumnos={id_al}
# GET '/alumnos/{id}/calificaciones'
def calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("Select * from calificaciones where id_alumno = ", id_alumno)
    return sesion.query(modelos.Calificacion).filter(modelos.Calificacion.id_alumno == id_alumno).all()

# DELETE FROM app.calificaciones WHERE id_alumnos={id_al}
# DELETE '/alumnos/{id}/calificaciones'
def borra_calificaciones_por_id_alumno(sesion: Session, id_alumno: int):
    print("Delete from calificaciones where id_alumno = ", id_alumno)
    calificaciones = calificaciones_por_id_alumno(sesion, id_alumno)
    for calificacion in calificaciones:
        sesion.delete(calificacion)
    sesion.commit()
    respuesta = {
        "mensaje": "Calificaciones eliminadas"
    }
    return respuesta


# DELETE FROM app.calificaciones WHERE id = {id_ca}
# DELETE '/calificaciones/{id}'
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

# ---------- Peticiones a Fotos ----------

# SELECT * FROM app.fotos
# GET '/fotos'
def lista_fotos(sesion: Session):
    print("Select * from fotos")
    return sesion.query(modelos.Foto).all()

# SELECT * FROM app.fotos WHERE id={id_fo}
# GET '/fotos/{id}'
def foto_por_id(sesion: Session, id_foto: int):
    print("Select * from fotos where id = ", id_foto)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id == id_foto).first()

# SELECT * FROM app.fotos WHERE id_alumnos={id_al}
# GET '/alumnos/{id}/fotos'
def fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("Select * from fotos where id_alumno = ", id_alumno)
    return sesion.query(modelos.Foto).filter(modelos.Foto.id_alumno == id_alumno).all()

# DELETE FROM app.fotos WHERE id_alumnos={id_al}
# DELETE '/alumnos/{id}/fotos'
def borra_fotos_por_id_alumno(sesion: Session, id_alumno: int):
    print("Delete from fotos where id_alumno = ", id_alumno)
    fotos = fotos_por_id_alumno(sesion, id_alumno)
    for foto in fotos:
        sesion.delete(foto)
    sesion.commit()
    respuesta = {
        "mensaje": "Fotos eliminadas"
    }
    return respuesta
