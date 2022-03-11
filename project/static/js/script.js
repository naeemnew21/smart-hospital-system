var sections = document.querySelectorAll("section");

	onscroll = function () {
		var scrollPosition = document.documentElement.scrollTop;

		sections.forEach((section) => {
		if (
			scrollPosition >= section.offsetTop - section.offsetHeight * 0.2 &&
			scrollPosition <
			section.offsetTop + section.offsetHeight - section.offsetHeight * 0.2
		) {
			var currentId = section.attributes.id.value;
			removeAllActiveClasses();
			addActiveClass(currentId);
		}
		});
	};

	var removeAllActiveClasses = function () {
		document.querySelectorAll("nav ul li a").forEach((el) => {
		el.classList.remove("active");
		});
	};

	var addActiveClass = function (id) {
		// console.log(id);
		var selector = `nav a[href="#${id}"]`;
		document.querySelector(selector).classList.add("active");
	};
			  
	var prevScrollpos = window.pageYOffset;
	window.onscroll = function() {
	  var currentScrollPos = window.pageYOffset;
	  if (prevScrollpos > currentScrollPos) {
		document.getElementById("mynav").style.top = "0";
		
	  } else {
		document.getElementById("mynav").style.top = "-80px";
	  }
	  prevScrollpos = currentScrollPos;
	  
	};		  

	var popoverTriggerList = [].slice.call(document.querySelectorAll('[data-bs-toggle="popover"]'))
	var popoverList = popoverTriggerList.map(function (popoverTriggerEl) {
	return new bootstrap.Popover(popoverTriggerEl)
	})

	document.getElementById("floatingInput").addEventListener("keyup", pass);

	document.getElementById("floatingPassword").addEventListener("keyup", pass);
	function pass(){
	const email = document.getElementById("floatingInput").value;
	const pass = document.getElementById("floatingPassword").value;
	if(email.length >= 4 && pass.length >= 4) {
		document.getElementById("signbtn").removeAttribute("disabled");
	}
	else {
		document.getElementById("signbtn").setAttribute("disabled",true);
	}	
	}