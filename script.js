const API_BASE = "http://127.0.0.1:8000"; // ajusta si tu backend está en otra URL

// ====================== PERSONAJES ======================
async function cargarPersonajes() {
  try {
    const response = await fetch(`${API_BASE}/personajes`);
    const personajes = await response.json();
    const container = document.getElementById("personajes-container");
    if (!container) return;
    container.innerHTML = "";

    personajes.forEach(p => {
      const card = document.createElement("div");
      card.classList.add("card-personaje");
      card.innerHTML = `
        <div class="personaje-img" style="background-image: url('${p.imagen}')"></div>
        <div class="personaje-info">
          <h3>${p.nombre}</h3>
          <p>Distrito: ${p.distrito}</p>
          <button onclick="verDetalle(${p.id})">Ver más</button>
        </div>
      `;
      container.appendChild(card);
    });
  } catch (error) {
    console.error("Error cargando personajes:", error);
  }
}

// ====================== DETALLE PERSONAJE ======================
async function verDetalle(id) {
  try {
    const response = await fetch(`${API_BASE}/personajes/${id}`);
    const personaje = await response.json();

    const modalTitle = document.getElementById("modal-titulo") || document.getElementById("modal-title");
    const modalDesc = document.getElementById("modal-descripcion") || document.getElementById("modal-description");
    const modalImg = document.getElementById("modal-imagen") || document.getElementById("modal-img");
    const modalVideo = document.getElementById("modal-video") || document.getElementById("modal-trailer");

    if (modalTitle) modalTitle.innerText = personaje.nombre || "";
    if (modalDesc) modalDesc.innerText = personaje.descripcion || "";
    if (modalImg) modalImg.src = personaje.imagen || "";
    if (modalVideo) modalVideo.src = personaje.video || "";

    const modal = document.getElementById("modal");
    if (modal) modal.style.display = "flex";
  } catch (error) {
    console.error("Error obteniendo detalle:", error);
  }
}

// ====================== PELICULAS ======================
async function cargarPeliculas() {
  try {
    const response = await fetch(`${API_BASE}/peliculas`);
    const peliculas = await response.json();
    const container = document.getElementById("peliculas-container");
    if (!container) return;
    container.innerHTML = "";

    peliculas.forEach(p => {
      const card = document.createElement("div");
      card.classList.add("card");
      card.innerHTML = `
        <img src="${p.poster}" alt="${p.titulo}" style="max-width:150px; border-radius:8px; border:2px solid #ffcc00;">
        <h3>${p.titulo}</h3>
        <p><b>Año:</b> ${p.ano}</p>
        <p><b>Director:</b> ${p.director}</p>
        <button onclick="verDetallePelicula(${p.id})">Ver más</button>
      `;
      container.appendChild(card);
    });
  } catch (error) {
    console.error("Error cargando películas:", error);
  }
}

async function verDetallePelicula(id) {
  try {
    const response = await fetch(`${API_BASE}/peliculas/${id}`);
    const pelicula = await response.json();

    const modalTitle = document.getElementById("modal-titulo") || document.getElementById("modal-title");
    const modalDesc = document.getElementById("modal-descripcion") || document.getElementById("modal-description");
    const modalImg = document.getElementById("modal-imagen") || document.getElementById("modal-img");
    const modalVideo = document.getElementById("modal-video") || document.getElementById("modal-trailer");

    if (modalTitle) modalTitle.innerText = pelicula.titulo || "";
    if (modalDesc) modalDesc.innerText = pelicula.descripcion || "Sin descripción";
    if (modalImg) modalImg.src = pelicula.poster || "";
    if (modalVideo) modalVideo.src = pelicula.video || "";

    const modal = document.getElementById("modal");
    if (modal) modal.style.display = "flex";
  } catch (error) {
    console.error("Error obteniendo detalle de película:", error);
  }
}

// ====================== CERRAR MODAL ======================
function cerrarModal() {
  const modal = document.getElementById("modal");
  if (!modal) return;
  modal.style.display = "none";

  const mv = document.getElementById("modal-video") || document.getElementById("modal-trailer");
  if (mv) mv.src = "";
}
document.addEventListener('click', (e) => {
  if (e.target && (e.target.classList.contains('close-btn') || e.target.classList.contains('close'))) {
    cerrarModal();
  }
});
document.getElementById("modal")?.addEventListener("click", function(e) {
  if (e.target === this) cerrarModal();
});

const setupContacto = () => {
  const form = document.getElementById("form-contacto");
  if (!form) return;

  form.addEventListener("submit", async (e) => {
    e.preventDefault();
    const nombre = form.querySelector("[name='nombre']").value.trim();
    const correo = form.querySelector("[name='correo']").value.trim();
    const mensaje = form.querySelector("[name='mensaje']").value.trim();

    const estado = document.getElementById("estado");
    const correoRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/i;

    if (!correo || !correoRegex.test(correo)) {
      if (estado) { 
        estado.className = "estado error"; 
        estado.innerText = "⚠️ Ingresa un correo válido"; 
        estado.style.display = "block"; 
      }
      return;
    }

    try {
      const resp = await fetch(`${API_BASE}/contacto`, {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ nombre, correo, mensaje })
      });
      if (resp.ok) {
        if (estado) { 
          estado.className = "estado exito"; 
          estado.innerText = "✅ Mensaje enviado"; 
          estado.style.display = "block"; 
        }
        form.reset();
      } else {
        if (estado) { 
          estado.className = "estado error"; 
          estado.innerText = "❌ Error al enviar"; 
          estado.style.display = "block"; 
        }
      }
    } catch (err) {
      console.error("Error enviando contacto:", err);
      if (estado) { 
        estado.className = "estado error"; 
        estado.innerText = "❌ Error de conexión"; 
        estado.style.display = "block"; 
      }
    }
  });
};


// ====================== SECCIÓN INTELIGENTE (CHATBOT IA) ======================
function appendChat(message, from='bot') {
  const c = document.getElementById('ia-respuesta') || document.getElementById('chat-container');
  if (!c) return;
  const wrap = document.createElement('div');
  wrap.style.margin = '8px 0';
  wrap.style.display = 'flex';
  wrap.style.justifyContent = from === 'user' ? 'flex-end' : 'flex-start';
  const bubble = document.createElement('div');
  bubble.textContent = message;
  bubble.style.maxWidth = '75%';
  bubble.style.padding = '10px';
  bubble.style.borderRadius = '10px';
  bubble.style.whiteSpace = 'pre-wrap';
  bubble.style.lineHeight = '1.3';
  if (from === 'user') {
    bubble.style.background = '#0b6cff';
    bubble.style.color = '#fff';
  } else {
    bubble.style.background = '#222';
    bubble.style.color = '#fff';
    bubble.style.border = '1px solid #333';
  }
  wrap.appendChild(bubble);
  c.appendChild(wrap);
  c.scrollTop = c.scrollHeight;
}

async function enviarPreguntaIA(texto) {
  if (!texto) return;
  appendChat(texto, 'user');
  appendChat("⏳ Pensando...", 'bot');

  try {
    const resp = await fetch(`${API_BASE}/inteligente`, {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify({ pregunta: texto })
    });

    const data = await resp.json();

    const c = document.getElementById('ia-respuesta') || document.getElementById('chat-container');
    if (c) {
      for (let i = c.children.length - 1; i >= 0; i--) {
        const last = c.children[i];
        if (last && last.textContent && last.textContent.includes("Pensando")) { last.remove(); break; }
      }
    }

    if (resp.ok && data && data.respuesta) {
      appendChat(data.respuesta, 'bot');
    } else {
      appendChat("❌ Error: " + (data.detail || "No se obtuvo respuesta de la IA."), 'bot');
    }
  } catch (err) {
    console.error("Error en IA:", err);
    appendChat("❌ Error al conectar con la IA.", 'bot');
  }
}

function setupIAUI() {
  const btns = [
    document.getElementById("ia-enviar"),
    document.getElementById("i-enviar")
  ].filter(Boolean);

  btns.forEach(btn => {
    btn.addEventListener("click", () => {
      const input = document.getElementById("ia-pregunta") || document.getElementById("i-texto");
      if (!input) return;
      const texto = input.value.trim();
      if (!texto) return;
      input.value = "";
      enviarPreguntaIA(texto);
    });
  });

  const inputArea = document.getElementById("ia-pregunta") || document.getElementById("i-texto");
  if (inputArea) {
    inputArea.addEventListener("keydown", (e) => {
      if (e.key === "Enter" && !e.shiftKey) {
        e.preventDefault();
        const texto = inputArea.value.trim();
        if (!texto) return;
        inputArea.value = "";
        enviarPreguntaIA(texto);
      }
    });
  }
}

// ====================== MAPA ======================
async function cargarMapa() {
  try {
    const map = L.map("map").setView([34.0, -84.0], 3);
    L.tileLayer("https://{s}.tile.openstreetmap.org/{z}/{x}/{y}.png", {
      attribution: "© OpenStreetMap contributors"
    }).addTo(map);

    const response = await fetch(`${API_BASE}/lugares`);
    const lugares = await response.json();
    lugares.forEach(l => {
      L.marker([l.lat, l.lon]).addTo(map)
        .bindPopup(`<b>${l.nombre}</b><br>${l.descripcion || ""}`);
    });
  } catch (error) {
    console.error("Error cargando lugares:", error);
  }
}

// ====================== INICIO ======================
window.onload = () => {
  cargarPersonajes();
  cargarPeliculas();
  cargarMapa();
  setupContacto();
  setupIAUI();
};
