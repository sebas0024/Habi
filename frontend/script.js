async function buscar() {
    const ciudad = document.getElementById('filtro-ciudad').value;
    const ano = document.getElementById('filtro-ano').value;
    const estado = document.getElementById('filtro-estado').value;

    

    // Construimos la URL con los parámetros
    let url = `http://127.0.0.1:8000/api/properties?`;
    if(ciudad) url += `city=${ciudad}&`;
    if(ano) url += `year=${ano}&`;
    if(estado) url += `status=${estado}&`;

    try {
        const response = await fetch(url);
        const datos = await response.json();
        console.log("DATOS RECIBIDOS DEL BACKEND:", datos);
        render(datos);
    } catch (error) {
        console.error("Error al conectar con la API:", error);
    }
}

function render(propiedades) {
    const contenedor = document.getElementById('contenedor-propiedades');
    contenedor.innerHTML = ""; // Limpiar

    propiedades.forEach(p => {
        contenedor.innerHTML += `
            <div class="col">
                <div class="card h-100 shadow-sm">
                    <div class="card-body">
                        <h5 class="card-title text-primary">${p.address}</h5>
                        <p class="card-text">
                            <strong>Ciudad:</strong> ${p.city}<br>
                            <strong>Año:</strong> ${p.year}<br>
                            <strong>Precio:</strong> $${(p.price || p.precio || 0).toLocaleString('es-CO')}
                        </p>
                    </div>
                    <div class="card-footer bg-white border-0">
                        <span class="badge bg-info text-dark">${p.status}</span>
                    </div>
                </div>
            </div>
        `;
    });
}

// Carga inicial
buscar();