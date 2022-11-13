$(document).ready(function(){
	const my_plot = document.getElementsByClassName("table-data");
	const boxes = document.querySelectorAll('.plot');
	boxes.forEach(box => {
		// box.style.backgroundColor = 'blue';
		y = box.textContent;
		// .slice(0,7);
		box.textContent = y

		// box.style.width = '300px';
	  });

	id_tbody.onmouseover = function(event){
		let target = event.target;
		my_class = target.className.indexOf("class-plot");
		my_class_actors = target.className.indexOf("class-actors");
		// console.log(target);
		// console.log(my_class);
		if (my_class == 11 || my_class_actors == 11){
			// console.log(my_class);
			// console.log(target.id);
			n = target.id;
			// my_plot = target.querySelectorAll("my-plott")
			// console.log(target[my-plott]);
			// document.getElementById(n).style.color = "red";
			document.getElementById(n).style.fontSize = "12px";
			document.getElementById(n).textContent = document.getElementById(n).getAttribute("attr")
		}

		
	};
	
	id_tbody.onmouseout = function(event){
		let target = event.target;
		my_class = target.className.indexOf("class-plot")
		my_class_actors = target.className.indexOf("class-actors");
		// console.log(my_class);
		if (my_class == 11){
			// console.log(target.id);
			n = target.id;
			document.getElementById(n).style.color = "black";
			document.getElementById(n).style.fontSize = "8px";
			textCont = document.getElementById(n).getAttribute("attr");
			document.getElementById(n).textContent = textCont.substring(0,90) + ("...");
			
		}
		if (my_class_actors == 11){
			// console.log(target.id);
			n = target.id;
			// document.getElementById(n).style.color = "red";
			document.getElementById(n).style.fontSize = "8px";
			textCont = document.getElementById(n).getAttribute("attr");
			document.getElementById(n).textContent = textCont.substring(0,70) + ("...");
			
		}
		
	};
	
	myChecked();

	const btn = document.querySelector('#id_all');
		btn.addEventListener('click', (event) => {
			const checkboxes = document.querySelectorAll('input[attr="genree"]')
			if (btn.checked == true){
				console.log("hhhhh")
				checkboxes.forEach((checkbox) => {
					if (checkbox.checked == true) {
						console.log("4")
						// console.log(checkbox.getAttribute("id"));
						// console.log(checkbox.checked)
					} else {
						console.log("no selcted");
					};
					checkbox.checked = true;
					const checked = checkbox.querySelector('input[type="checkbox"]:checked')
				});	
			} else {
				console.log("žžžžžž");
				checkboxes.forEach((checkbox) => {
					if (checkbox.checked == false) {
						console.log("2")
						// console.log(checkbox.getAttribute("id"));
						// console.log(checkbox.checked)
					};
					checkbox.checked = false;
					const checked = checkbox.querySelector('input[type="checkbox"]:checked')
				});

			};
		});  
	
});

// IF ALL IS CHECKED
function myChecked(){

	const cb_checked = document.querySelector("#id_all");
	console.log(cb_checked.checked);
	console.log("rudij");
	// btn.addEventListener('click', (event) => {
	// 	console.log("rudiiiiiiij")            
	//  });  
	// document.querySelector("id_akcija").checked;
}

function check(checked = true) {
	const checkboxes = document.querySelectorAll('#id_all');
	checkboxes.forEach((checkbox) => {
		checkbox.checked = checked;
	});
}

var properties = [
	"id_date",
	"id_channel",
	"id_title",
	"id_original_title",
	"id_genree",
	"id_imdb",
	"id_plot",
	"total",
	"id_director",
	"id_cast",
	"total4",
	"id_time",
	"id_duration"

];

// function myFunction() {
//     alert("Hello from a static file!");
//   }
function myFunction2() {

	let target = event.target;
	console.log(target)

	var e = $(this).attr("ID");
	document.getElementsByClassName(this);
	alert(e);
	var e = this;
	console.log(document.getElementsByClassName(this));
	var lengthText = 30;
	var text = $('#my-truncc').text();
	var shortText = $.trim(text).substring(0, lengthText).split(" ").slice(0, -1).join(" ") + "...";
	
	$('#my-truncc').text(shortText);
	
	$('#my-truncc').hover(function(){
		$(this).text(text);
	}, function(){
		$(this).text(shortText);
	});
  }

$('#cls-len').click(function(){
	// alert("jo")
	$('#cls-len').html("jooooooooooo");
	var example = "I am too long string";
	var result;
	// Slice is JS function
	result = example.slice(0, 10)+'...';
	$('#cls-len').html(result);
	$('#my-trunc').html(result);
});


$.each( properties, function( i, val ) {
	
	var orderClass = '';

	$("#" + val).click(function(e){
		e.preventDefault();
		$('.filter__link.filter__link--active').not(this).removeClass('filter__link--active');
  		$(this).toggleClass('filter__link--active');
   		$('.filter__link').removeClass('asc desc');

   		if(orderClass == 'desc' || orderClass == '') {
    			$(this).addClass('asc');
    			orderClass = 'asc';
       	} else {
       		$(this).addClass('desc');
       		orderClass = 'desc';
       	}

		var parent = $(this).closest('.header__item');
    		var index = $(".header__item").index(parent);
		var $table = $('.table-content');
		var rows = $table.find('.table-row').get();
		var isSelected = $(this).hasClass('filter__link--active');
		var isNumber = $(this).hasClass('filter__link--number');
			
		rows.sort(function(a, b){

			var x = $(a).find('.table-data').eq(index).text();
    			var y = $(b).find('.table-data').eq(index).text();
				
			if(isNumber == true) {
    					
				if(isSelected) {
					return x - y;
				} else {
					return y - x;
				}

			} else {
			
				if(isSelected) {		
					if(x < y) return -1;
					if(x > y) return 1;
					return 0;
				} else {
					if(x > y) return -1;
					if(x < y) return 1;
					return 0;
				}
			}
    		});

		$.each(rows, function(index,row) {
			$table.append(row);
		});

		return false;
	});

});