from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

#variables 
a = "antes de interactuar con la base de datos " 
b = "Medida 1:"
c = "Medida 2:"
d = "Medida 3:"
e = "antes de comentar la sesion mostrar ID "
f = "antes de comentar la sesion "
g = "Medida 1 ID:"
h = "Medida 2 ID:"
i = "Medida 3 ID:"
k = "Despues de comentar la sesion mostar los valores"
l = "Valor de Medida 1:"
m = "Valor de Medida 2:"
n = "Valor de Medida 3:"
ñ = "Despues actualizar medidas"
o = "Despues de que la sesion se cierre"

class Medidas(SQLModel, table=True):
    id: Optional[int] = Field(default=None, primary_key=True)
    Sistema_SI: float
    Sistema_Ingles: float

sqlite_file_name = "base_de_datos.db"
sqlite_url = f"sqlite:///{sqlite_file_name}"

engine = create_engine(sqlite_url, echo = True)

SQLModel.metadata.create_all(engine)

def create_db_and_tables():
    SQLModel.metadata.create_all(engine)


def create_medidas():
    Kilometros = Medidas(Sistema_SI="1.60", Sistema_Ingles="1") #por si solos no dan salida
    Gramos  = Medidas(Sistema_SI="0.453", Sistema_Ingles="1")
    Litros = Medidas(Sistema_SI="3.785", Sistema_Ingles="1")

    print(a) #se imprime dado a la función
    print(b,Kilometros)
    print(c,Gramos)
    print(d,Litros)

    with Session(engine) as session: #aun no estan guardados en la base de datos
        session.add(Kilometros)
        session.add(Gramos)
        session.add(Litros)

        session.commit()

        print(f)
        print(b, Kilometros) #Ahora esta caducado hasta que se actualize 
        print(c, Gramos)
        print(d, Litros)

        print(e)
        print(g, Kilometros.id) # puede detectar que estamos tratando de acceder a los datos, luego está actualmente asociado con una sesión y se marca como caducado.
        print(h, Gramos.id)
        print(i, Litros.id)

        print(k)
        print(l, Kilometros.Sistema_SI) #no obtiene datos adicionales y no ejecuta SQL adicional 
        print(m, Gramos.Sistema_SI)
        print(n, Litros.Sistema_SI)

        session.refresh(Kilometros) #session usará el motor para ejecuar el SQL 
        session.refresh(Gramos)
        session.refresh(Litros)

        print(ñ)
        print(b, Kilometros)
        print(c, Gramos)
        print(d, Litros)

    print(o)
    print(b, Kilometros)
    print(c, Gramos)
    print(d, Litros)



def main():
    create_db_and_tables()
    create_medidas()

if __name__ == "__main__":
    create_db_and_tables()
    create_medidas()

