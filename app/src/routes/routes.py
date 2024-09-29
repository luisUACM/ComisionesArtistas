from flask import current_app as app
from flask import render_template
from flask import session
import random

from ..modelo.model import Usuario
from ..modelo.model import Arte
from ..modelo.model import Usuario
from ..modelo.model import Dinero
from ..modelo.model import Concepto
from ..modelo.model import Servicio


def generar_conceptos(cantidad: int) -> list[Concepto]:
    conceptos = []
    descripciones = [
        "Concepto A", "Concepto B", "Concepto C", "Concepto D", "Concepto E",
        "Concepto F", "Concepto G", "Concepto H", "Concepto I", "Concepto J",
        "Concepto K", "Concepto L", "Concepto M", "Concepto N", "Concepto O"
    ]
    
    for i in range(cantidad):
            # Crear una instancia de Dinero con una cantidad aleatoria entre 100 y 500
            dinero_concepto = Dinero(cantidad=random.uniform(100, 500), moneda=Dinero.TipoMoneda.MXN)

            # Asegurarse de que cada concepto tenga una descripción única
            descripcion = descripciones[i % len(descripciones)]  # Asegúrate de que la longitud sea suficiente
            
            # Condición para determinar si es un concepto extra
            es_extra = (i != 0)  # El primer concepto (índice 0) será False, el resto será True

            # Crear instancia de Concepto
            concepto = Concepto(
                descripcion=descripcion,
                precio=dinero_concepto,  # Asignar la instancia de dinero que vale 100 pesos
                es_extra=es_extra,
                id=i
            )
            conceptos.append(concepto)

    return conceptos



def generar_arte_aleatoria(cantidad=3) -> list[Arte]:
    artes = []
    for i in range(cantidad):
        arte = Arte(
            artista=i,
            ruta='img/broly.jpg',
            nombre_archivo=f"obra_{i}.jpg",
            id=i,
            etiquetas=["etiqueta1", "etiqueta2"],
            titulo=f"Título de la obra {i} - {random.randint(1, 1000)}"
        )
        artes.append(arte)
    return artes

# Listas de adjetivos y sustantivos para crear títulos únicos
adjetivos = [
    "Personalizado", "Innovador", "Interactivo", "Colaborativo", "Conceptual", 
    "Animado", "Vectorial", "Minimalista", "Dinámico", "Realista", 
    "Futurista", "Surrealista", "Abstracto", "Visual", "Profesional"
]
sustantivos = [
    "Ilustración", "Animación", "Modelado 3D", "Renderización", "Diseño UX/UI", 
    "Logotipo", "Banner", "Concept Art", "Motion Graphics", "Pieza Publicitaria", 
    "Diseño Web", "Arte Multimedia", "Edición de Video", "Fotomanipulación", 
    "Desarrollo de Marca", "Diseño de Producto", "Escultura Digital", "Cartel"
]



def generar_servicios(cantidad=15) -> list[Servicio]:
    servicios = []
    for i in range(cantidad):
        # Generar un título único combinando un adjetivo y un sustantivo
        adjetivo = random.choice(adjetivos)
        sustantivo = random.choice(sustantivos)
        titulo = f"{adjetivo} {sustantivo} {i + 1}"  # Agregamos el número para garantizar unicidad

        # Generar una lista de conceptos y piezas de arte por cada servicio
        conceptos = generar_conceptos(random.randint(1, 5))  # Entre 2 y 5 conceptos
        piezas_arte = generar_arte_aleatoria()  # Entre 1 y 3 piezas de arte
        contrato = ["Término 1", "Término 2", "Término 3"]  # Un contrato simulado
        
        servicio = Servicio(
            titulo=titulo,
            conceptos=conceptos,
            piezas_arte=piezas_arte,
            contrato=contrato,
            id=i
        )
        servicios.append(servicio)
    
    return servicios

#Se pueden declarar una o mas rutas para la funcion que responde a dicha ruta
@app.route('/')
@app.route('/inicio')
def home():
    #Aqui se hace procesamiento y se devuelve una template renderizada, tambien se pueden agregar variables
    session['id_cuenta'] = 1   #Simulacion de login
    # Crear 15 instancias de la clase Arte

    # Crear 15 instancias de la clase Usuario con rol de ARTISTA
    usuarios = []
    for i in range(15):
        usuario = Usuario(
            correo=f"user{i}@ejemplo.com",
            contrasena=f"contrasena{i}",
            nombre=f"Usuario {i}",
            roles=[Usuario.Rol.ARTISTA],  # Todos tienen rol de ARTISTA
            id=i,
            biografia=f"Biografía del usuario {i}",
            foto_perfil='/fotos_perfil/generic.webp',
            moneda=Dinero.TipoMoneda.MXN,
            portafolio=[],  # Asignar la lista de arte generada anteriormente
            comisiones=[],
            servicios=generar_servicios(15),
            contactos=[]
        )
        usuarios.append(usuario)
    
    for usuario in usuarios:
        print(usuario._nombre)   
        for servicio in usuario.servicios:
            print(servicio._titulo)
            print(servicio.obtener_ruta_primera_arte())
            for concepto in servicio._conceptos:
                print(f"Es extra: {concepto.es_extra}, Precio: {concepto.precio._cantidad} {concepto.precio._moneda.name}")
                etiquetas = servicio.dame_etiquetas()
                print(etiquetas)
            
    return render_template('index.html', usuarios=usuarios)
#Para poder mostrar esta debo de crear Usuarios,Arte,Comisiones,Servicios,Conceptos,Dinero
