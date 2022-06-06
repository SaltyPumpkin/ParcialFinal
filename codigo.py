from select import select
from typing import Optional
from sqlmodel import Field, Session, SQLModel, create_engine

#variables 
a = "antes de interactuar con la base de datos " 
b = "Medida 1:"
c = "Medida 2:"
d = "Medida 3:"

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

def seleccion_medidas():
    with Session(engine) as session:
        estado = select(Medidas) .where(Medidas.Sistema_SI == "1.60")
        resultado = session.exec(estado)
        for medida in resultado:
            print(medida)



def main():
    create_db_and_tables()
    create_medidas()
    seleccion_medidas()

if __name__ == "__main__":
    create_db_and_tables()
    create_medidas()

