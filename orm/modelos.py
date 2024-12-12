# Importar la clase base de las clases modelos y los tipos de datos
from orm.config import BaseClass
from sqlalchemy import Column, String, Integer, ForeignKey, DateTime

# Modelo para la tabla alumnos
class Alumno(BaseClass):
    __tablename__ = "alumnos"  # Nombre de la tabla
    id = Column(Integer, primary_key=True)
    nombre = Column(String(100))
    edad = Column(Integer)
    domicilio = Column(String(100))
    carrera = Column(String(100))
    trimestre = Column(String(100))
    email = Column(String(100), unique=True)
    password = Column(String(100))
    fecha_registro = Column(DateTime(timezone=True))

# Modelo para la tabla calificaciones
class Calificacion(BaseClass):
    __tablename__ = "calificaciones"  # Nombre de la tabla
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    uea = Column(String(100))
    calificacion = Column(String(100))

# Modelo para la tabla fotos
class Foto(BaseClass):
    __tablename__ = "fotos"  # Nombre de la tabla
    id = Column(Integer, primary_key=True)
    id_alumno = Column(Integer, ForeignKey("alumnos.id"))
    titulo = Column(String(100))
    descripcion = Column(String(100))
    ruta = Column(String(255))
