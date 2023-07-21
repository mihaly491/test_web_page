document.getElementById("submit_button").addEventListener("click", function() {
    var name = document.getElementById("name_input").value;
    var greetingMessage = "Привет, " + name + "!";
    document.getElementById("greeting_message").innerText = greetingMessage;
	document.getElementById("greeting_message").style.visibility = "visible";
});