let filtroActual = 'pendiente';

async function cargarComandas() {
    const contenedor = document.getElementById("comandas-container");
    if (!contenedor) return;

    try {
        // Usamos la URL que confirmaste: http://localhost:5006/historial_comandas
        const response = await fetch("http://localhost:5006/historial_comandas");
        
        if (!response.ok) throw new Error("No se pudo obtener datos del servidor");
        
        const comandas = await response.json();
        
        contenedor.innerHTML = "";
        // Filtramos por estado según la base de datos
        const filtradas = comandas.filter(c => c.estado === filtroActual);

        if (filtradas.length === 0) {
            contenedor.innerHTML = `<p style="text-align:center; grid-column:1/-1;">No hay comandas ${filtroActual}es.</p>`;
            return;
        }

        filtradas.forEach(comanda => {
            const card = document.createElement("div");
            card.className = `comanda-card ${comanda.estado}`;
            
            // Generamos la lista de productos basada en la tabla comanda_items
            let itemsHtml = comanda.items.map(item => `
                <div class="item-line">
                    <strong>${item.cantidad}x</strong> ${item.nombre}
                    ${item.detalles ? `<br><small style="color:red">↳ ${item.detalles}</small>` : ""}
                </div>
            `).join("");

            card.innerHTML = `
                <div class="card-header"><span>Ticket #${comanda.id}</span></div>
                <div class="card-body">${itemsHtml}</div>
                ${comanda.estado === 'pendiente' ? 
                    `<button class="btn-ready" onclick="finalizarComanda(${comanda.id})">TERMINAR</button>` : ''}
            `;
            contenedor.appendChild(card);
        });
    } catch (e) { 
        console.error("Error en el historial:", e); 
    }
}

// Funciones globales
window.cambiarFiltro = (estado) => {
    filtroActual = estado;
    document.querySelectorAll('.filter-btn').forEach(b => b.classList.remove('active'));
    if (event) event.target.classList.add('active');
    cargarComandas();
};

window.finalizarComanda = async (id) => {
    try {
        // Llamada al puerto 5006 con la ruta nueva
        const res = await fetch(`http://localhost:5006/comandas/${id}/finalizar`, { 
            method: 'PATCH' 
        });
        
        if (res.ok) {
            // Recargamos la lista para que el ticket desaparezca de "Pendientes"
            cargarComandas(); 
        } else {
            alert("No se pudo finalizar la comanda");
        }
    } catch (e) { 
        console.error("Error al finalizar:", e); 
    }
};

// Refresco cada 5 segundos para tiempo real
setInterval(cargarComandas, 5000);
cargarComandas();

