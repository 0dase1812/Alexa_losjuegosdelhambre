Micrositio Web - Los Juegos del Hambre 🎬🔥
📌 Objetivo del Proyecto

El objetivo de este proyecto fue diseñar y desarrollar un micrositio web completo que combina tanto un backend basado en servicios API REST como un frontend funcional y bien estructurado.

Yo creé mi propia API para gestionar datos y la consumí desde el frontend con JavaScript, siguiendo buenas prácticas de desarrollo web moderno.
Este proyecto me permitió entender la conexión real entre frontend y backend, además de fortalecer mi habilidad para construir interfaces dinámicas, integradas y con un diseño profesional.

🧩 Caso de Uso

El micrositio está dividido en 6 secciones principales:

Home – Presentación personal tipo hoja de vida: incluye foto, descripción, contacto, proyectos realizados y mis skills técnicos.

Catálogo – Catálogo de películas de Los Juegos del Hambre, alimentado desde mi propia API.

Detalle de entidad – Cada película del catálogo se puede consultar en detalle: con imagen, descripción extendida y un video embebido.

Formulario de contacto – Permite que los visitantes escriban un mensaje; el frontend valida los datos y luego se envían a un endpoint de la API.

Sección con mapa – Muestra tres lugares de rodaje reales de la saga, utilizando LeafletJS, con mensajes explicativos de cada sitio.

Sección Inteligente (IA) – Funcionalidad de recomendación que usa un modelo de IA para generar descripciones o comentarios relacionados con la saga.

⚙️ Tecnologías Utilizadas

Backend: Python con FastAPI.

Frontend: HTML5, CSS3, JavaScript.

Mapas: LeafletJS.

IA: OpenAI API.

Servidor local: Uvicorn.

🏗️ Estructura del Proyecto
📂 micrositio
 ┣ 📂 backend
 ┃ ┗ 📜 main.py
 ┣ 📂 frontend
 ┃ ┣ 📜 index.html
 ┃ ┣ 📜 contacto.html
 ┃ ┣ 📜 scrpt.js
 ┃ ┗ 📜 styles.css
 ┗ 📜 README.md

🔌 Explicación Técnica
1. API REST (Backend con FastAPI)

Creé la API usando FastAPI en Python. Esta API expone endpoints que devuelven la información de las películas en formato JSON.

Ejemplo de endpoint:

@app.get("/peliculas")
def get_peliculas():
    return peliculas


El API se ejecuta con Uvicorn en un servidor local y es consumida desde el frontend.

2. Conexión API - Frontend

En el frontend utilicé fetch() para consumir la API desde JavaScript:

fetch("http://127.0.0.1:8000/peliculas")
  .then(response => response.json())
  .then(data => mostrarPeliculas(data));


De esta forma logré que el catálogo muestre los datos que vienen directamente de la API.

3. Home

Página principal donde presento mi perfil, mis habilidades y mis proyectos. Sirve como carta de presentación para cualquier persona que visite el micrositio.

Archivo: index.html

4. Catálogo

Aquí muestro un catálogo con las películas de Los Juegos del Hambre. Toda la información (nombre, imagen, descripción) viene de la API.

Archivo: catalogo.html

5. Detalle de entidad

Cada película tiene su propia página de detalle, con una descripción más larga, imagen destacada y un video embebido desde YouTube.

Archivo: detalle.html

6. Formulario de contacto

El formulario valida los campos en el frontend y envía los datos a un endpoint del backend. No se usa base de datos; los mensajes se almacenan temporalmente en la API.

Archivo: contacto.html

Ejemplo de endpoint para guardar mensajes:

@app.post("/contacto")
def guardar_contacto(mensaje: dict):
    mensajes.append(mensaje)
    return {"mensaje": "Contacto guardado exitosamente"}

7. Mapas

Integré LeafletJS para mostrar tres lugares de rodaje de la saga. Al hacer clic en cada marcador, aparece un mensaje que explica qué se grabó en ese lugar.

Archivo: mapa.html

Ejemplo en JS:

L.marker([48.8566, 2.3522]).addTo(map)
  .bindPopup("Escenas grabadas en París para la película.")

8. Sección Inteligente (IA)

Usé la API de OpenAI para generar descripciones o recomendaciones relacionadas con las películas. Esto permite enriquecer el micrositio con contenido dinámico.

Archivo: inteligente.html

📖 Definiciones breves

API REST: Conjunto de reglas que permite que una aplicación se comunique con otra usando HTTP.

Endpoint: Dirección URL donde se puede acceder a un recurso de la API.

Frontend: Parte visible de la aplicación, con la que interactúa el usuario.

Backend: Parte lógica que maneja los datos, reglas y conexiones.

Fetch(): Función de JavaScript para solicitar datos de un servidor.

✅ Conclusiones

Este proyecto fue una experiencia muy valiosa porque me permitió poner en práctica los conocimientos adquiridos en el curso de una forma real y significativa.
Al trabajar en el micrositio, pude integrar el frontend y el backend de manera coherente, logrando que ambos se comunicaran a través de una API REST que yo misma construí.

Elegí la saga de Los Juegos del Hambre porque es mi favorita, y eso hizo que el desarrollo fuera más motivador y personal.

Aprendí a:

Crear y consumir endpoints de una API REST.

Validar formularios y manejar datos desde el frontend y backend.

Integrar mapas interactivos con LeafletJS.

Usar un modelo de IA para mejorar la experiencia del usuario.

Siento que este micrositio refleja mis habilidades actuales como desarrolladora y me abre la puerta a seguir mejorando en proyectos más complejos.

🔗 Entregables

Repositorio en GitHub:
https://github.com/0dase1812/Alexa_losjuegosdelhambre

Página HTML publicada:
https://0dase1812.github.io/Alexa_losjuegosdelhambre/