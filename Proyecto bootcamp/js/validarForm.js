document.addEventListener('DOMContentLoaded', function() {
    const form = document.getElementById('registroForm');
    form.addEventListener('submit', function(e) {
        if (!form.checkValidity()) {
            e.preventDefault();
            if (window.M && M.toast) {
                M.toast({html: 'Por favor, completa todos los campos correctamente.'});
            } else {
                alert('Por favor, completa todos los campos correctamente.');
            }
        }
        
    });
});