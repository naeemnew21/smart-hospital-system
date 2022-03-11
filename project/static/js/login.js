



var form = document.forms.namedItem("loginform");

form.addEventListener('submit', function(ev) {

    var jsonform= new FormData(form);
    
    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/login_api", true);

    xhttp.onreadystatechange = function(oEvent)
    {
        if (this.readyState == 4 && this.status == 200)
        {
            response = JSON.parse(this.responseText)
            if (response.error == false){
                window.location = response.url ;
            }
            else 
            {
                document.getElementById("login_error").innerHTML = response.error;
            }
        }
    };
    xhttp.send(jsonform);   
    ev.preventDefault();
}, false);