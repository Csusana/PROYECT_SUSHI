(function () {
	'use strict';

	var tinyslider = function () {
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




	var sitePlusMinus = function () {

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
			for (var i = 0; i < quantity.length; i++) {
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

document.addEventListener('DOMContentLoaded', function () {
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

	form.addEventListener('submit', function (e) {
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

document.addEventListener('DOMContentLoaded', function () {
	// Obtener datos locales de los pedidos
	const deliveryDate = localStorage.getItem('deliveryDate');
	const deliveryTime = localStorage.getItem('deliveryTime');
	const customerInfo = JSON.parse(localStorage.getItem('customerInfo') || '{}');

	// Mostrar código de pedido
	if (customerInfo.orderNumber) {
		document.getElementById('order-number').textContent = customerInfo.orderNumber;
	}

	// Mostrar fecha y hora de entraga
	if (deliveryDate) {
		const formattedDate = new Date(deliveryDate).toLocaleDateString('es-ES');
		document.getElementById('delivery-date-display').textContent = formattedDate;
	}

	if (deliveryTime) {
		document.getElementById('delivery-time-display').textContent = deliveryTime;
	}

	// Mostrar datos del cliente 
	if (customerInfo.firstName) {
		document.getElementById('customer-name').textContent = customerInfo.firstName + ' ' + customerInfo.lastName;
		document.getElementById('customer-address').textContent = customerInfo.address;
	}

	// Borrar datos cliente y pedido
	localStorage.removeItem('cart');

	// Muestra los datos pero los borra luego de 1 minuto
	setTimeout(function () {
		localStorage.removeItem('customerInfo');
		localStorage.removeItem('deliveryDate');
		localStorage.removeItem('deliveryTime');
	}, 60000);
});

localStorage.setItem('cart', JSON.stringify(carrito)); 

  document.addEventListener('DOMContentLoaded', function () {
	const deliveryDate = localStorage.getItem('deliveryDate');
	const deliveryTime = localStorage.getItem('deliveryTime');
	const customerInfo = JSON.parse(localStorage.getItem('customerInfo') || '{}');
  
	const orderNumberElem = document.getElementById('order-number');
	if (customerInfo.orderNumber && orderNumberElem) {
	  orderNumberElem.textContent = customerInfo.orderNumber;
	}
  
	const deliveryDateElem = document.getElementById('delivery-date-display');
	if (deliveryDate && deliveryDateElem) {
	  const formattedDate = new Date(deliveryDate).toLocaleDateString('es-ES');
	  deliveryDateElem.textContent = formattedDate;
	}
  
	const deliveryTimeElem = document.getElementById('delivery-time-display');
	if (deliveryTime && deliveryTimeElem) {
	  deliveryTimeElem.textContent = deliveryTime;
	}
  
	const customerNameElem = document.getElementById('customer-name');
	const customerAddressElem = document.getElementById('customer-address');
	if (customerInfo.firstName && customerNameElem && customerAddressElem) {
	  customerNameElem.textContent = customerInfo.firstName + ' ' + customerInfo.lastName;
	  customerAddressElem.textContent = customerInfo.address;
	}
  
	// Limpiar carrito inmediatamente
	localStorage.removeItem('cart');
  
	// Borrar datos cliente y pedido luego de 1 minuto (opcional)
	setTimeout(function () {
	  localStorage.removeItem('customerInfo');
	  localStorage.removeItem('deliveryDate');
	  localStorage.removeItem('deliveryTime');
	}, 60000);
  });

