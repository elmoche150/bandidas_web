document.getElementById('form-menu').addEventListener('submit', async (e) => {
        e.preventDefault();

    const servidorIP = window.location.hostname;
    const API_URL = `http://${servidorIP}:5006/menu_agregar`;
        
        const data = {
            nombre: document.getElementById('menu-nombre').value,
            precio: document.getElementById('menu-precio').value,
            estado: document.getElementById('menu-estado').value
        };

        try {
            const res = await fetch(API_URL, {
                method: "POST",
                headers: {"Content-Type": "application/json"},
                body: JSON.stringify(data)
            });

            if (res.ok) {
                alert("Producto agregado correctamente");
                e.target.reset();
            }
        } catch (err) {
            alert("Error al conectar con el servidor");
        }
    });