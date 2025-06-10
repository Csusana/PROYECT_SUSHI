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

	// 购物车功能
	var setupAddToCart = function() {
		// 存储购物车中的商品
		let cart = JSON.parse(localStorage.getItem('cart')) || [];
		
		// 获取所有添加到购物车的按钮（"+"图标）
		const addButtons = document.querySelectorAll('.icon-cross');
		
		// 修改所有加号按钮的位置
		addButtons.forEach(function(button) {
			button.style.bottom = '50px';
			
			// 为每个按钮添加点击事件监听器
			button.addEventListener('click', function(e) {
				e.preventDefault();
				e.stopPropagation(); // 防止触发父元素的点击事件
				
				// 获取商品信息
				const productItem = this.closest('.product-item');
				const productName = productItem.querySelector('.product-title').textContent;
				const productPrice = productItem.querySelector('.product-price').textContent.replace('$', '');
				const productImage = productItem.querySelector('img.product-thumbnail').getAttribute('src');
				const productId = productItem.querySelector('img.product-thumbnail').getAttribute('data-bs-target').replace('#modal', '');
				
				// 检查购物车中是否已存在该商品
				const existingItemIndex = cart.findIndex(item => item.id === productId);
				
				if (existingItemIndex > -1) {
					// 如果商品已存在，增加数量
					cart[existingItemIndex].quantity += 1;
				} else {
					// 否则，添加新商品到购物车
					cart.push({
						id: productId,
						name: productName,
						price: productPrice,
						image: productImage,
						quantity: 1
					});
				}
				
				// 将购物车数据保存到localStorage
				localStorage.setItem('cart', JSON.stringify(cart));
				
				// 显示成功消息（可选）
				alert('商品已添加到购物车！');
			});
		});
	};
	

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

	// 在DOM完全加载后初始化购物车功能
	document.addEventListener('DOMContentLoaded', function() {
		setupAddToCart();
	});
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
  
	if (form) {
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
	}
  });