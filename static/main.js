function correct(){
	var result = document.getElementById("result");
	var buttons = document.getElementById("buttons");
	var result_text = document.getElementById("result_text");
	result_text.innerHTML = "Correct!";
	buttons.style.display = "none";
	result.style.display = "block";
	result.className+= " alert-success";
}

function wrong(){
	var elem = document.getElementById("result");
	var buttons = document.getElementById("buttons");
	var result_text = document.getElementById("result_text");
	result_text.innerHTML = "Wrong!";
	buttons.style.display = "none";
	result.style.display = "block";
	result.className+= " alert-danger";

}