(function() {
	'use strict';

	var tinyslider = function() {
		var el = document.querySelectorAll('.testimonial-slider');

		if (el.length > 0) {
			var slider = tns({
				container: '.testimonial-slider',
				items: 1,
				axis: "horizontal",
				controlsContainer: "#testimonial-nav",
				swipeAngle: false,
				speed: 700,
				nav: true,
				controls: true,
				autoplay: true,
				autoplayHoverPause: true,
				autoplayTimeout: 3500,
				autoplayButtonOutput: false
			});
		}
	};
	tinyslider();

	


	var sitePlusMinus = function() {

		var value,
    		quantity = document.getElementsByClassName('quantity-container');

		function createBindings(quantityContainer) {
	      var quantityAmount = quantityContainer.getElementsByClassName('quantity-amount')[0];
	      var increase = quantityContainer.getElementsByClassName('increase')[0];
	      var decrease = quantityContainer.getElementsByClassName('decrease')[0];
	      increase.addEventListener('click', function (e) { increaseValue(e, quantityAmount); });
	      decrease.addEventListener('click', function (e) { decreaseValue(e, quantityAmount); });
	    }

	    function init() {
	        for (var i = 0; i < quantity.length; i++ ) {
						createBindings(quantity[i]);
	        }
	    };

	    function increaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        console.log(quantityAmount, quantityAmount.value);

	        value = isNaN(value) ? 0 : value;
	        value++;
	        quantityAmount.value = value;
	    }

	    function decreaseValue(event, quantityAmount) {
	        value = parseInt(quantityAmount.value, 10);

	        value = isNaN(value) ? 0 : value;
	        if (value > 0) value--;

	        quantityAmount.value = value;
	    }
	    
	    init();
		
	};
	sitePlusMinus();


})()

document.addEventListener('DOMContentLoaded', function() {
	const inputFecha = document.getElementById('fecha');
	const hoy = new Date();
  
	const yyyy = hoy.getFullYear();
	const mm = String(hoy.getMonth() + 1).padStart(2, '0');
	const dd = String(hoy.getDate()).padStart(2, '0');
  
	const fechaMin = `${yyyy}-${mm}-${dd}`;
	if (inputFecha) {
	  inputFecha.min = fechaMin;
	}
  
	const form = document.getElementById('form-reserva');  // <--- Falta esto
  
	const errorMsg = document.getElementById('error-msg');
	const errorText = document.getElementById('error-text');
  
	form.addEventListener('submit', function(e) {
	  errorMsg.classList.add('d-none');  // Ocultamos alerta al empezar
	  errorText.textContent = '';         // Limpiamos texto
  
	  const fecha = inputFecha.value;
	  const nombre = document.getElementById('nombre').value;
	  const hora = document.getElementById('hora').value;
	  const tamanio = document.getElementById('tamanio').value;
	  
  
	  if (!fecha || !hora || !tamanio || !nombre) {
		e.preventDefault();
  
		errorText.textContent = 'Por favor, completá todos los campos.';
		errorMsg.classList.remove('d-none');  // Mostramos alerta
	  }
	});
  });