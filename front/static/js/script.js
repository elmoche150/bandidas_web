// ELEMENTOS DEL DOM
const grupoComidas = document.getElementById("grupo-comidas");
const grupoBebidas = document.getElementById("grupo-bebidas");
const listaResumen = document.getElementById("lista");
const selectProducto = document.getElementById("producto");
const inputCantidad = document.getElementById("cantidad");
const notasArea = document.getElementById("notas");
const btnAgregar = document.getElementById("agregar");
const btnEnviar = document.getElementById("enviar");

let itemsPedido = [];

// CARGAR MENU
fetch("http://localhost:5006/menu")
    .then(res => res.json())
    .then(menu => {
        menu.forEach(p => {
            const opt = document.createElement("option");
            opt.value = p.id;
            opt.textContent = p.nombre;
            if (p.estado === "bebida") grupoBebidas.appendChild(opt);
            else grupoComidas.appendChild(opt);
        });
    });

// AGREGAR ITEM AL RESUMEN
btnAgregar.addEventListener("click", () => {
    const productoId = selectProducto.value;
    const cantidad = parseInt(inputCantidad.value);
    const textoNota = notasArea.value;

    if (!productoId || productoId === "Elegí un producto" || cantidad < 1) return;

    const nombre = selectProducto.options[selectProducto.selectedIndex].text;

    itemsPedido.push({
        producto_id: productoId,
        nombre: nombre,
        cantidad: cantidad,
        detalles: textoNota
    });

    // Limpiar campos
    notasArea.value = ""; 
    inputCantidad.value = 1;
    selectProducto.selectedIndex = 0;

    renderResumen();
});

function renderResumen() {
    listaResumen.innerHTML = "";
    itemsPedido.forEach((item, index) => {
        const div = document.createElement("div");
        div.classList.add("order-item");
        div.innerHTML = `
            <span><strong>${item.cantidad}x</strong> ${item.nombre} ${item.detalles ? `<small>(${item.detalles})</small>` : ''}</span>
            <span style="cursor:pointer; color:red" onclick="eliminarDelResumen(${index})">✕</span>
        `;
        listaResumen.appendChild(div);
    });
}

window.eliminarDelResumen = (index) => {
    itemsPedido.splice(index, 1);
    renderResumen();
};

// ENVIAR A COCINA
btnEnviar.addEventListener("click", () => {
    if (itemsPedido.length === 0) return alert("Pedido vacío");

    fetch("http://localhost:5006/comandas", {
        method: "POST",
        headers: { "Content-Type": "application/json" },
        body: JSON.stringify({ items: itemsPedido })
    })
    .then(res => {
        if (res.ok) {
            alert("Enviado a cocina");
            itemsPedido = [];
            renderResumen();
        }
    });
});