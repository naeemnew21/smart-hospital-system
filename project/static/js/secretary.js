

function draw_waiting(json){
    let htmltext = '';
    for(let app in json){
        if (json[app].status == "pending"){
            htmltext += '<div class="col-lg-6 col-12 pb-3">';
            htmltext += '<div class="container bg-white p-4 shadow-sm  border" style="border-radius: 25px;">';
            
            htmltext += '<div class="col-12 mt-3">';
            htmltext += '<h5 class="display fw-bold " >';
            htmltext += json[app].patient_name;
            htmltext += '</h5>';
            htmltext += '</div>';
    
            htmltext += '<div class="col-lg-4 col-12">';
            htmltext += '<button onclick=appoint_event(this) ';
            htmltext += ' id='+json[app].request_model +' name="confirm" class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Accept</button>';
            htmltext += '</div>';
    
            htmltext += '<br>';
    
            htmltext += '<div class="col-lg-4 col-12">';
            htmltext += '<button onclick=appoint_event(this) ';
            htmltext += ' id='+json[app].request_model +'  name="reject" class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Cancel</button>';
            htmltext += '</div>';
    
            htmltext += '</div>';
            htmltext += '</div>';
            htmltext += '<br>';
        }

    }
    return htmltext;
}


function draw_accepted(json){
    let htmltext = '';
    for(let app in json){
        if (json[app].status == "accepted"){
            htmltext += '<div class="col-lg-6 col-12 pb-3">';
            htmltext += '<div class="container bg-white p-4 shadow-sm  border" style="border-radius: 25px;">';
            
            htmltext += '<div class="col-12 mt-3">';
            htmltext += '<h5 class="display fw-bold " >';
            htmltext += json[app].patient_name;
            htmltext += '</h5>';
            htmltext += '</div>';
    
            htmltext += '<div class="col-lg-4 col-12">';
            htmltext += '<button onclick=appoint_event(this) ';
            htmltext += ' id='+json[app].request_model +' name="discharge" class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Discharge</button>';
            htmltext += '</div>';
    
            htmltext += '<br>';
    
            htmltext += '<div class="col-lg-4 col-12">';
            htmltext += '<button onclick=appoint_event(this) ';
            htmltext += ' id='+json[app].request_model +' name="reject" class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Cancel</button>';
            htmltext += '</div>';
    
            htmltext += '</div>';
            htmltext += '</div>';
            htmltext += '<br>';
        }

    }
    return htmltext;
}

get_patients()

setInterval(function() { get_patients() }, 1000);
  


function get_patients(element)
{   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        appoints = JSON.parse(this.responseText);
        document.getElementById("waiting").innerHTML = draw_waiting(appoints);
        document.getElementById("accepted").innerHTML = draw_accepted(appoints);
      }
    }
    xhttp.open("GET", '/secretary/patients/', true);
    xhttp.send();   
}  




function appoint_event(element)
{   
    let pk = element.id;

    let data = {};
    data['pk']    = pk;
    data['event'] = element.name;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", '/secretary/patients/' , true);

    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        get_patients();
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  
 



function getCookie(name) {
    let cookieValue = null;
    if (document.cookie && document.cookie !== '') {
        const cookies = document.cookie.split(';');
        for (let i = 0; i < cookies.length; i++) {
            const cookie = cookies[i].trim();
            // Does this cookie string begin with the name we want?
            if (cookie.substring(0, name.length + 1) === (name + '=')) {
                cookieValue = decodeURIComponent(cookie.substring(name.length + 1));
                break;
            }
        }
    }
    return cookieValue;
}