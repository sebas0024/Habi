async function buscar() {
    const ciudad = document.getElementById('filtro-ciudad').value;
    //const ano = document.getElementById('filtro-ano').value;
    const estado = document.getElementById('filtro-estado').value;

    

    // Construimos la URL con los parámetros
    let url = `http://127.0.0.1:8000/api/properties?`;
    if(ciudad) url += `city=${ciudad}&`;
    //if(ano) url += `year=${ano}&`;
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

        const fotoUrl = ImageService.getPropertyImage(p.id);
        contenedor.innerHTML += `
            <div class="col-12 mb-4">
                <div class="card shadow-sm h-100 overflow-hidden" style="max-height: 220px; min-height: 220px;">
                    <div class="row g-0 h-100">
                        
                        <div class="col-md-4 h-100">
                            <img src="${fotoUrl}" 
                                class="img-fluid h-100 w-100" 
                                style="object-fit: cover;" 
                                alt="Propiedad">
                        </div>
                        
                        <div class="col-md-8 h-100 d-flex flex-column">
                            <div class="card-body flex-grow-1 p-3">
                                <h5 class="card-title text-primary text-truncate" style="text-transform: capitalize;">${p.address}</h5>
                                
                                <div class="card-text mb-2" style="font-size: 0.9rem;">
                                    <strong>Ciudad:</strong> <span style="text-transform: capitalize;">${p.city}</span>
                                    <!-- <strong>Año:</strong> ${p.year}-->
                                </div>

                                <p class="card-text fw-bold text-success mb-1">
                                    Precio: $${(p.price || 0).toLocaleString('es-CO')}
                                </p>

                                <p class="card-text small text-muted text-truncate-custom">
                                    ${p.description || 'Sin descripción adicional.'}
                                </p>
                            </div>

                            <div class="card-footer bg-white border-0 p-3 pt-0 d-flex justify-content-between align-items-center">
                                <span class="badge bg-info text-dark" style="text-transform: capitalize;">${p.status.replace('_', ' ')}</span>
                                <button class="btn btn-outline-primary btn-sm px-3">Ver detalles</button>
                            </div>
                        </div>

                    </div>
                </div>
            </div>
        `;
    });
}

// Carga inicial
buscar();