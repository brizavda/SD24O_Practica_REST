# El engine permite configurar la conexión a la base de datos
from sqlalchemy import create_engine
# El sessionmaker permite crear sesiones para hacer consultas
# Por cada consulta se abre y cierra
from sqlalchemy.orm import sessionmaker
# declarative_base permite definir la clase base para mapear las tablas de la base de datos
from sqlalchemy.ext.declarative import declarative_base

# 1. Configurar la conexión a la base de datos
# servidorBD://usuario:password@url:puerto/nombreBD
URL_BASE_DATOS = "postgresql://SistemasD:Nomelos3@localhost:5432/PracticaREST"

# Crear el motor de conexión
engine = create_engine(URL_BASE_DATOS)

# 2. Obtener la clase que nos permite crear objetos tipo sesión
SessionClass = sessionmaker(engine)

# Crear una función que nos permite obtener objetos de tipo sesión
def generador_session():
    sesion = SessionClass()
    try:
        # Equivalente a return sesion pero de manera segura
        yield sesion
    finally:
        sesion.close()

# 3. Obtener la clase base para mapear tablas
BaseClass = declarative_base()
