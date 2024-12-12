import orm.modelos as modelos
from sqlalchemy.orm import Session
from sqlalchemy import and_
import orm.esquemas as esquemas
from fastapi import UploadFile
import os
import uuid

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

# UPDATE app.alumnos SET columna = AlumnoBase WHERE id={id_al}
# PUT '/alumnos/{id}'
def actualiza_alumno(session: Session, id_alumno: int, alm_esquema:esquemas.AlumnoBase):
    print("UPDATE app.alumnos SET columna = valor WHERE id= ", id_alumno)
    alm_bd = alumno_por_id(session, id_alumno)
    if alm_bd is not None:
        alm_bd.nombre = alm_esquema.nombre
        alm_bd.edad = alm_esquema.edad
        alm_bd.domicilio = alm_esquema.domicilio
        alm_bd.carrera = alm_esquema.carrera
        alm_bd.trimestre = alm_esquema.trimestre
        alm_bd.email = alm_esquema.email
        alm_bd.password = alm_esquema.password

        session.commit()
        session.refresh(alm_bd)
        print(alm_esquema)
        return alm_esquema
    else:
        respuesta = {"mensaje":"No existe el usuario"}
        return respuesta

# INSERT INTO app.alumnos VALUES AlumnoBase
# POST '/alumnos'
def guardar_alumno(sesion:Session, alm_esquema:esquemas.AlumnoBase):
    alm_bd = modelos.Alumno()

    alm_bd.nombre = alm_esquema.nombre
    alm_bd.edad = alm_esquema.edad
    alm_bd.domicilio = alm_esquema.domicilio
    alm_bd.carrera = alm_esquema.carrera
    alm_bd.trimestre = alm_esquema.trimestre
    alm_bd.email = alm_esquema.email
    alm_bd.password = alm_esquema.password    
    
    sesion.add(alm_bd)
    sesion.commit()
    sesion.refresh(alm_bd)

    return alm_bd

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

# UPDATE app.calificaciones SET columna = CalificacionBase WHERE id={id_ca}
# PUT '/calificaciones/{id}'
def actualiza_calificacion(session: Session, id_calificacion: int, cal_esquema:esquemas.CalificacionBase):
    print("UPDATE app.calificaciones SET columna = valor WHERE id= ", id_calificacion)
    cal_bd = calificacion_por_id(session, id_calificacion)
    if cal_bd is not None:
        cal_bd.uea = cal_esquema.uea
        cal_bd.calificacion = cal_esquema.calificacion

        session.commit()
        session.refresh(cal_bd)
        print(cal_esquema)
        return cal_esquema
    else:
        respuesta = {"mensaje":"No existe la calificación"}
        return respuesta
    
# INSERT INTO app.calificaiones VALUES CalificacionBase
# POST '/alumnos/{id}/calificaciones'
def guardar_calificacion(sesion:Session, cal_esquema:esquemas.CalificacionBase, id_usuario:int):
    alm = alumno_por_id(sesion,id_usuario)
    if alm is not None:
        cal_bd = modelos.Calificacion()

        cal_bd.id_alumno = id_usuario
        cal_bd.uea = cal_esquema.uea
        cal_bd.calificacion = cal_esquema.calificacion 
        
        sesion.add(cal_bd)
        sesion.commit()
        sesion.refresh(cal_bd)

        return cal_bd
    else:
        respuesta = {"mensaje":"No se encuentra al alumno"}
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

# DELETE FROM fotos WHERE id = id_foto
# DELETE '/fotos/{id}'
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

# UPDATE app.fotos SET columna = FotoBase WHERE id={id_ft}
# PUT '/fotos/{id}'
async def actualizar_foto(sesion: Session, id_foto: int, fto_esquema: esquemas.FotoBase, foto: UploadFile = None):
    print(f"UPDATE app.fotos SET columna = valor WHERE id = {id_foto}")

    # Buscar la foto en la base de datos
    fto_bd = foto_por_id(sesion, id_foto)
    if fto_bd is None:
        return {"mensaje": "No existe la foto"}

    # Actualizar los campos
    fto_bd.titulo = fto_esquema.titulo
    fto_bd.descripcion = fto_esquema.descripcion

    if foto is not None:
        # Configuración de directorio y nombre de archivo
        home_usuario = os.path.expanduser("~")
        ruta_base = os.path.join(home_usuario, "fotos-alumnos")
        os.makedirs(ruta_base, exist_ok=True)  # Crear directorio si no existe

        # Generar un nombre único para el archivo
        nombre_archivo = f"{uuid.uuid4()}{os.path.splitext(foto.filename)[1]}"
        nueva_ruta = os.path.join(ruta_base, nombre_archivo)

        # Guardar el nuevo archivo físicamente
        with open(nueva_ruta, "wb") as archivo:
            contenido = await foto.read()
            archivo.write(contenido)

        # Eliminar el archivo anterior si existe
        if os.path.exists(fto_bd.ruta):
            os.remove(fto_bd.ruta)

        # Actualizar la ruta en la base de datos
        fto_bd.ruta = nueva_ruta

    # Confirmar los cambios en la base de datos
    sesion.commit()
    sesion.refresh(fto_bd)

    return fto_bd
    
# INSERT INTO app.fotos VALUES FotoBase
# POST '/alumnos/{id}/fotos'
async def guardar_foto(sesion: Session, fto_esquema: esquemas.FotoBase, id_usuario: int, foto: UploadFile):
    print("INSERT INTO app.fotos VALUES FotoBase")

    # Verificar si el alumno existe
    alm = alumno_por_id(sesion, id_usuario)
    if alm is None:
        return {"mensaje": "No se encuentra al alumno"}

    # Configuración de directorio y nombre de archivo
    home_usuario = os.path.expanduser("~")
    ruta_base = os.path.join(home_usuario, "fotos-alumnos")
    os.makedirs(ruta_base, exist_ok=True)  # Crear directorio si no existe

    # Generar un nombre único para el archivo
    nombre_archivo = f"{uuid.uuid4()}{os.path.splitext(foto.filename)[1]}"
    ruta_completa = os.path.join(ruta_base, nombre_archivo)

    # Guardar el archivo físicamente
    with open(ruta_completa, "wb") as archivo:
        contenido = await foto.read()
        archivo.write(contenido)

    # Guardar los detalles en la base de datos
    fto_bd = modelos.Foto()
    fto_bd.id_alumno = id_usuario
    fto_bd.titulo = fto_esquema.titulo
    fto_bd.descripcion = fto_esquema.descripcion
    fto_bd.ruta = ruta_completa

    sesion.add(fto_bd)
    sesion.commit()
    sesion.refresh(fto_bd)

    return fto_bd
