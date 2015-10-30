function correct(){
	var elem = document.getElementById("success");
	var buttons = document.getElementById("buttons");
	buttons.style.display = "none";
	elem.style.display = "block";
}

function wrong(){
	var elem = document.getElementById("failure");
	var buttons = document.getElementById("buttons");
	buttons.style.display = "none";
	elem.style.display = "block";
}