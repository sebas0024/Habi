
const ImageService = {
    // Esta función devuelve la URL de la imagen basada en el ID de la propiedad
    getPropertyImage: function(propertyId) {
        // Servicio de fotos aleatorias pero "bloqueado" por ID
        // Para que la casa #2 siempre tenga la misma foto
        return `https://loremflickr.com/400/400/house,home/all?lock=${propertyId}`;
    },

    // Imagen de respaldo por si algo falla
    getPlaceholder: function() {
        return 'https://via.placeholder.com/400x400?text=Casa+Habi';
    }
};