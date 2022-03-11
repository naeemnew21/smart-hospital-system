

function drawJSON(json){
    let htmltext = '';
    for(let app in json){
        htmltext += '<div class="col-lg-6 col-12 pb-3">';
        htmltext += '<div class="container bg-white p-4 shadow-sm  border" style="border-radius: 25px;">';
        
        htmltext += '<div class="col-12  border-bottom  pb-3">';
        htmltext += '<small class="bg-primary text-white rounded-pill  p-2 fw-bold">';
        htmltext += json[app].specialty;
        htmltext += '</small>';
        htmltext += '</div>';

        htmltext += '<div class="col-12 mt-3">';
        htmltext += '<h4 class="display fw-bold " >';
        htmltext += json[app].doctor_name;
        htmltext += '</h4>';
        htmltext += '<h6 class="">';
        htmltext += json[app].week_day + ' ( ' ;
        htmltext += json[app].appointment_date + ' ) from ' ;
        htmltext += json[app].start_time + '  To  ' ;
        htmltext += json[app].end_time ;
        htmltext += '</h6>';
        htmltext += '</div>';

        htmltext += '<div class="col-lg-4 col-12">';
        htmltext += '<button onclick=delete_appoint(this) ';
        htmltext += ' id='+json[app].id +' class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Cancel</button>';
        htmltext += '</div>';

        htmltext += '<small class="bg-primary text-white rounded-pill  p-2 fw-bold">';
        htmltext += json[app].status;
        htmltext += '</small>';
        
        htmltext += '</div>';
        htmltext += '</div>';
        htmltext += '<br>';
    }
    return htmltext;
}


get_appoints()

function get_appoints(element)
{   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        appoints = JSON.parse(this.responseText);
        document.getElementById("appointments").innerHTML = drawJSON(appoints);
      }
    }
    xhttp.open("GET", '/patient/myappoints/', true);
    xhttp.send();   
}  




function delete_appoint(element){
  pk = element.id
  data = {};
  data['pk']   = pk;

  var xhttp = new XMLHttpRequest();
  xhttp.open("DELETE", "/patient/myappoints/", true);

  const csrftoken = getCookie('csrftoken');
  xhttp.setRequestHeader('x-csrftoken', csrftoken)
  xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
  xhttp.setRequestHeader('Accept', 'application/json')

  xhttp.onreadystatechange = function()
  {
      if (this.readyState == 4 && this.status == 200)
      {
          response = JSON.parse(this.responseText);
          var r=confirm("Deleted Successfully");
          if (r==true)
          {
               window.location = response.redirect ;
          }
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