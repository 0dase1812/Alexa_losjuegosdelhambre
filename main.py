# backend/main.py
from fastapi import FastAPI, HTTPException
from fastapi.middleware.cors import CORSMiddleware
from pydantic import BaseModel, EmailStr
from typing import List, Optional
from openai import OpenAI
import os
from dotenv import load_dotenv   # Importar dotenv

# --- Cargar variables de entorno ---
dotenv_path = os.path.join(os.path.dirname(__file__), "..", ".env")
load_dotenv(dotenv_path)  # Ahora sí le pasamos la ruta del .env

# --- Configuración ---
app = FastAPI(title="API - Micrositio Derly Sanchez", version="2.0.0")



app.add_middleware(
    CORSMiddleware,
    allow_origins=["*"],  # en producción restringir al dominio
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)

# Configura tu API key de OpenAI
client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))



# --- Models ---
class Contacto(BaseModel):
    nombre: str
    correo: EmailStr
    mensaje: str

class Personaje(BaseModel):
    id: int
    nombre: str
    distrito: str
    rol: Optional[str] = None
    descripcion: str
    imagen: str
    video: Optional[str] = None

class Pelicula(BaseModel):
    id: int
    titulo: str
    ano: int
    director: str
    taquilla_usd: Optional[int] = None
    poster: Optional[str] = None
    descripcion: Optional[str] = None

class Lugar(BaseModel):
    id: int
    nombre: str
    lat: float
    lon: float
    descripcion: Optional[str] = None

class PreguntaIA(BaseModel):
    pregunta: str

# --- Datos Home (presentación Derly) ---
home_data = {
    "nombre": "Derly Sanchez",
    "foto": "https://i.postimg.cc/W15hw3wM/Derly-Sanchez.jpg",
    "descripcion": "Soy estudiante de Ingeniería, emprendedora y fundadora de Fixxgoo, una empresa integral dedicada a la preparación de inmuebles para su entrega en venta o arriendo. Apasionada por la música, el trading y fanática de la saga de Los Juegos del Hambre. Actualmente curso una certificación en Ciberseguridad de Google a través de Coursera.",
    "contacto": {
        "correo": "alexase13246@gmail.com",
        "instagram": "https://www.instagram.com/0dase_1812",
    },
    "proyectos": [
        {"nombre": "Fixxgoo", "descripcion": "Emprendimiento de soluciones integrales para entrega de apartamentos y casas."},
        {"nombre": "Curso de Ciberseguridad – Google Coursera", "descripcion": "Formación práctica en seguridad informática, redes y protección de datos."}
    ],
    "skills": [
        "Python", "FastAPI", "HTML", "CSS", "JavaScript",
        "Excel", "Power BI", "Ciberseguridad", "Trading", "Gestión de proyectos"
    ]
}

# --- Datos de ejemplo (completos, restaurados) ---
personajes_db: List[Personaje] = [
    Personaje(
        id=1,
        nombre="Katniss Everdeen",
        distrito="12",
        rol="Protagonista",
        descripcion="Katniss, la chica en llamas. Heroína que se vuelve símbolo de la rebelión.",
        imagen="https://w0.peakpx.com/wallpaper/15/592/HD-wallpaper-movie-katniss-everdeen-jennifer-lawrence-the-hunger-games-the-hunger-games-mockingjay-part-2.jpg",
        video="https://www.youtube.com/embed/TQBNEF9H0bY?si=K2wwf7XGGtvnM5Ho"
    ),
    Personaje(
        id=2,
        nombre="Peeta Mellark",
        distrito="12",
        rol="Aliado",
        descripcion="Peeta, panadero y aliado, conocido por su bondad y estrategia política/emocional.",
        imagen="https://i.pinimg.com/736x/8b/9a/12/8b9a12ea30629aa17745f88f16161842.jpg",
        video="https://www.youtube.com/embed/l3ENAGeHzLE?si=LL9nnmqwCRxK5jbP"
    ),
    Personaje(
        id=3,
        nombre="President Snow",
        distrito="Capitolio",
        rol="Antagonista",
        descripcion="Presidente Snow, líder autoritario del Capitolio que reprime a los distritos.",
        imagen="https://1.bp.blogspot.com/-KKxk1oZgQPg/VCnZ1FbyvBI/AAAAAAAAO2w/SdVYa4OhiYE/s1600/10693851_1486939548225692_1257649384_n.jpg",
        video="https://www.youtube.com/embed/nvPvYWvHYgc?si=HniIsGKNhU2xVI"
    ),
    Personaje(
        id=4,
        nombre="Gale Hawthorne",
        distrito="12",
        rol="Aliado/Conflicto",
        descripcion="Gale, amigo de Katniss y figura compleja en la rebelión.",
        imagen="https://vignette1.wikia.nocookie.net/igrzyskasmierci/images/f/fb/Gale_kosog%C5%82os_promo.jpg/revision/latest?cb=20150426072638&path-prefix=pl",
        video="//www.youtube.com/embed/nn-uCG2VcXs?si=gy3Dj5GzBxNXFl5p"
    ),
    Personaje(
        id=5,
        nombre="Finnick Odair",
        distrito="4",
        rol="Aliado",
        descripcion="Finnick, saltador carismático y hábil gladiador con un pasado trágico.",
        imagen="https://i.pinimg.com/originals/04/fc/fa/04fcfa3f0d24fe4e172106859f3944f6.jpg",
        video="https://www.youtube.com/embed/t1rQr2bwe0s?si=pzYfhheMJitlp2pz"
    ),
    Personaje(
        id=6,
        nombre="Haymitch Abernathy",
        distrito="12",
        rol="Mentor",
        descripcion="Mentor de Katniss y Peeta, campeón anterior de los Juegos, cínico pero leal.",
        imagen="https://i.pinimg.com/originals/76/7d/90/767d909528ad826674c6e29fe2a5c362.jpg",
        video="https://www.youtube.com/embed/NzxWycaicds?si=nHNsILdfqgoVhliu"
    ),
    Personaje(
        id=7,
        nombre="Effie Trinket",
        distrito="Capitolio",
        rol="Escolta",
        descripcion="Excéntrica y extravagante escolta del Distrito 12.",
        imagen="https://images.fandango.com/ImageRenderer/0/0/redesign/static/img/default_poster.png/0/images/masterrepository/other/INTRO_ButterflyDress.jpg",
        video="https://www.youtube.com/embed/Eae68sBZoC8?si=q6a2HD6KZSxsxMop"
    ),
    Personaje(
        id=8,
        nombre="Primrose Everdeen",
        distrito="12",
        rol="Hermana",
        descripcion="Hermana pequeña de Katniss, dulce y compasiva.",
        imagen="https://vignette.wikia.nocookie.net/thehungergames/images/9/93/PrimroseD13Portrait.jpg/revision/latest?cb=20190306042858",
        video="https://www.youtube.com/embed/0JThHWIoJJw?si=2H_MpIwvNEq61FUY"
    ),
    Personaje(
        id=9,
        nombre="Cinna",
        distrito="Capitolio",
        rol="Estilista",
        descripcion="Diseñador y aliado clave, apoya a Katniss con creatividad y visión política.",
        imagen="https://static3.wikia.nocookie.net/__cb20130622232504/thehungergames/images/b/bd/CinnaCF001.png",
        video="https://www.youtube.com/embed/iw8mX_MisTQ?si=HrhvQgslM2hFvlE-"
    ),
    Personaje(
        id=10,
        nombre="Johanna Mason",
        distrito="7",
        rol="Aliada",
        descripcion="Astuta, sarcástica y valiente; se convierte en una aliada inesperada.",
        imagen="https://i.pinimg.com/originals/e0/56/50/e0565082e22b1dcef8d9e1fc6f3254c3.jpg",
        video="https://www.youtube.com/embed/ETCaUI1KhqM?si=fZthHBIicg-tocdl"
    ),
]

peliculas_db: List[Pelicula] = [
    Pelicula(
        id=1,
        titulo="Los juegos del hambre",
        ano=2012,
        director="Gary Ross",
        taquilla_usd=694394724,
        poster="https://www.miblogdecineytv.com/wp-content/uploads/2016/05/los_juegos_del_hambre-cartel3.jpg",
        descripcion="La historia inicia en Panem, una nación dividida en distritos controlados por el Capitolio. Cada año, como recordatorio del poder y castigo por antiguas rebeliones, se celebran los Juegos del Hambre, un evento televisado en el que un chico y una chica de cada distrito son obligados a luchar hasta la muerte. Cuando la pequeña Prim es elegida como tributo, su hermana Katniss Everdeen se ofrece voluntariamente para ocupar su lugar. Junto a Peeta Mellark, el tributo masculino de su distrito, debe enfrentarse no solo a rivales letales, sino también a un sistema diseñado para mantener sometida a la población. A lo largo de la competencia, Katniss se convierte en un símbolo inesperado de desafío, demostrando que la humanidad y la compasión pueden ser tan poderosas como las armas.."
    ),
    Pelicula(
        id=2,
        titulo="Los juegos del hambre: En Llamas",
        ano=2013,
        director="Francis Lawrence",
        taquilla_usd=865011746,
        poster="https://pics.filmaffinity.com/Los_juegos_del_hambre_En_llamas-123947302-large.jpg",
        descripcion="Después de ganar los Juegos, Katniss y Peeta regresan a su distrito con la vida aparentemente asegurada. Sin embargo, su victoria provoca un efecto inesperado: los distritos empiezan a verla como un símbolo de resistencia contra el Capitolio. Para controlar la situación, el presidente Snow organiza el “Vasallaje de los 25”, una edición especial de los Juegos donde los tributos son elegidos de entre los vencedores anteriores. Esto obliga a Katniss y Peeta a regresar a la arena, enfrentándose a campeones experimentados y a pruebas aún más mortales. A medida que la violencia aumenta, la chispa de la rebelión se extiende por Panem, y Katniss se convierte, sin quererlo, en el rostro de una lucha que apenas comienza."
    ),
    Pelicula(
        id=3,
        titulo="Los juegos del hambre: Sinsajo I",
        ano=2014,
        director="Francis Lawrence",
        taquilla_usd=755356711,
        poster="https://imagenes.gatotv.com/categorias/peliculas/posters/los_juegos_del_hambre_sinsajo_parte_1.jpg",
        descripcion="Tras la destrucción parcial de la arena y el rescate de Katniss por parte de la resistencia, la historia se traslada al Distrito 13, un lugar secreto que encabeza la rebelión contra el Capitolio. Allí, Katniss debe aceptar su papel como “El Sinsajo”, símbolo oficial de la revolución. Aunque al principio se resiste, las injusticias del Capitolio y la manipulación de Peeta como prisionero la convencen de asumir el liderazgo. Entre propagandas, estrategias militares y enfrentamientos, Katniss debe lidiar con la carga emocional de ser un ícono y la presión de tomar decisiones que pueden cambiar el destino de millones de personas. La guerra ya no es solo física, sino también psicológica y mediática."
    ),
    Pelicula(
        id=4,
        titulo="Los juegos del hambre: Sinsajo II",
        ano=2015,
        director="Francis Lawrence",
        taquilla_usd=653428261,
        poster="https://www.lahiguera.net/cinemania/pelicula/7089/los_juegos_del_hambre_sinsajo___parte_2-cartel-6442.jpg",
        descripcion="La batalla final entre los distritos y el Capitolio está en marcha. Katniss, junto con Gale, Finnick y otros aliados, se une a una peligrosa misión para llegar al corazón de Panem y asesinar al presidente Snow. El camino hacia el Capitolio está plagado de trampas y sacrificios, poniendo a prueba la resistencia y la determinación de todos. Sin embargo, a medida que avanza, Katniss se da cuenta de que el verdadero enemigo no es solo Snow, sino también las ambiciones ocultas dentro de la misma rebelión. La película muestra las consecuencias del poder, las traiciones y el costo humano de la guerra, culminando con un desenlace que revela tanto la caída del Capitolio como la complejidad moral de la libertad."
    ),
    Pelicula(
        id=5,
        titulo="Los juegos del hambre: Balada de pájaros cantores y serpientes",
        ano=2023,
        director="Francis Lawrence",
        taquilla_usd=337378738,
        poster="https://imgix.hoyts.com.au/mx/posters/au/the-hunger-games-the-ballad-of-songbirds-and-snakes-fbfd598c.jpg",
        descripcion="Ambientada 64 años antes de los eventos originales, esta precuela narra los inicios del futuro presidente Snow, cuando aún era un joven estudiante ambicioso. Coriolanus Snow vive en un Capitolio debilitado tras la guerra, intentando recuperar la gloria de su familia caída en desgracia. Para demostrar su valía, se convierte en mentor en los décimos Juegos del Hambre y es asignado a Lucy Gray Baird, una tributo del Distrito 12. Lo que empieza como un deber se transforma en una relación ambigua donde Snow descubre tanto la fuerza como el carisma de la joven. A través de esta historia, se revela cómo los ideales de poder, manipulación y control que marcarán su futuro empiezan a desarrollarse. Esta película no solo expande el universo de Panem, sino que también muestra el origen de la crueldad del sistema que dominará las películas principales."
    ),
]


# --- Lugares ---
lugares_db: List[Lugar] = [
    Lugar(id=1, nombre="Forsyth Park (Savannah, GA)", lat=32.0669, lon=-81.0998, descripcion="Usado para escenas del distrito/Capitolio en exteriores."),
    Lugar(id=2, nombre="Cades Cove (Great Smoky Mountains)", lat=35.5578, lon=-83.7176, descripcion="Escenas rurales y boscosas."),
    Lugar(id=3, nombre="Hunger Games Set - Pinewood (Reino Unido)", lat=51.6033, lon=-0.2930, descripcion="Algunas tomas interiores en sets en Reino Unido.")
]

# --- Contactos (se guardan en memoria) ---
contactos_db: List[dict] = []

# --- Endpoints ---
@app.get("/")
def root():
    return {"mensaje": "API de Los Juegos del Hambre / Derly Sanchez - Activa"}

@app.get("/home")
def get_home():
    return home_data

@app.get("/personajes", response_model=List[Personaje])
def get_personajes():
    return personajes_db

@app.get("/personajes/{personaje_id}", response_model=Personaje)
def get_personaje(personaje_id: int):
    personaje = next((p for p in personajes_db if p.id == personaje_id), None)
    if personaje:
        return personaje
    raise HTTPException(status_code=404, detail="Personaje no encontrado")

@app.get("/peliculas", response_model=List[Pelicula])
def get_peliculas():
    return peliculas_db

@app.get("/peliculas/{pelicula_id}", response_model=Pelicula)
def get_pelicula(pelicula_id: int):
    peli = next((p for p in peliculas_db if p.id == pelicula_id), None)
    if peli:
        return peli
    raise HTTPException(status_code=404, detail="Pelicula no encontrada")

@app.get("/lugares", response_model=List[Lugar])
def get_lugares():
    return lugares_db

@app.post("/contacto")
def post_contacto(contacto: Contacto):
    contactos_db.append(contacto.dict())
    return {"ok": True, "mensaje": "Contacto recibido. Gracias."}

@app.get("/contactos")
def listar_contactos():
    return contactos_db

@app.post("/inteligente")
def asistente_ia(p: PreguntaIA):
    try:
        prompt = f"""
        Eres un asistente experto en Los Juegos del Hambre y en el portafolio de Derly Sanchez.
        Usa esta información:
        - Personajes: {[p.nombre for p in personajes_db]}
        - Películas: {[p.titulo for p in peliculas_db]}
        - Lugares: {[l.nombre for l in lugares_db]}
        - Sobre Derly: {home_data['descripcion']}
        - Contacto: {home_data['contacto']}
        Pregunta: {p.pregunta}
        """

        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",  # o gpt-3.5-turbo si no tienes acceso
            messages=[
                {"role": "system", "content": "Eres un asistente útil."},
                {"role": "user", "content": prompt}
            ],
            max_tokens=200
        )

        return {"respuesta": respuesta.choices[0].message.content}

    except Exception as e:
        print("❌ Error con la IA:", str(e))  # 👈 
        raise HTTPException(status_code=500, detail=f"Error con la IA: {str(e)}")


@app.get("/health")
def health():
    return {"status": "ok"}
