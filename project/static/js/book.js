
json = {};
get_doctors();

function drawJSON(json)
{
    let htmltext = "<div>";

    for (let doctor in json){
        htmltext +='<div class="col-12 pb-3">';
        htmltext +='<div class="container p-4 shadow-sm bg-white border" style="border-radius: 25px;" id="doctorCard">';
        htmltext += '<div class="col-12  border-bottom  pb-3">';
        htmltext += '<small class="bg-primary text-white rounded-pill p-2 fw-bold" id="doctor_speciality">'+ json[doctor].specialty +'</small>';
        htmltext += '</div>';
        htmltext += '<div class="col-12 mt-3">';
        
        htmltext += '<div class="row align-items-center">';
        htmltext += '<div class="col-lg-8 col-12 mb-2">';
        htmltext += '<h3 class="display fw-bold " id="doctor_name" >'+ json[doctor].name +'</h3>';
        htmltext += '<small class="fw-bold" id="doctor_experience"><i class="fa-solid fa-circle-check me-2 text-primary"></i>experience : '+ json[doctor].experience +' years</small>';
        
        for (let day in json[doctor].work_days){
            htmltext += '<br>';
            htmltext += '<small class="fw-bold" id="doctor_date"><i class="fa-solid fa-calendar-days me-2 text-primary"></i>';
            htmltext += json[doctor].work_days[day].day +' ( '+json[doctor].work_days[day].start+' - '+json[doctor].work_days[day].end+' )';
            htmltext +='</small>';
        }


        htmltext += '<div class="col-md-6">';
        htmltext += '<label for="book_date" class="form-label fw-bold">Select Date:</label>';
        htmltext += '<select name="book_date" ';
        htmltext += ' id="book_date'+json[doctor].pk+'" class="form-select">';

        for (let day in json[doctor].work_days){
            htmltext += '<option ';
            htmltext += ' value='+json[doctor].work_days[day].date;
            htmltext += '>'+json[doctor].work_days[day].date +' ( '+json[doctor].work_days[day].day+' )';
            htmltext += '</option>';
        }

        htmltext += '</select>';
        htmltext += '</div>';

        htmltext += '</div>';
            
        htmltext += '<div class="col-lg-4 col-12">';
        htmltext += '<button onclick=book_appoint(this) ';
        htmltext += ' id='+json[doctor].pk +' class="btn btn-outline-primary rounded-pill fw-bold d-flex ms-auto align-items-center justify-content-center" style="min-width: fit-content;" role="button"><i class="fa-solid fa-hands-clapping me-2"></i>Book appointment</button>';
        htmltext += '</div>';

        htmltext += '</div>';
        htmltext += '</div>';
        htmltext += '</div>';
        htmltext +='</div>';
    }
    htmltext += "</div>";
    return htmltext;
}


function draw_pagination(json)
{
    let htmltext = "";

    htmltext +='<ul class="pagination justify-content-center align-items-center">';

    if (json.previous == null){
        htmltext +='<li class="page-item disabled">';
        htmltext +='<span class="page-link" style="border-radius: 25px;">Prev.</span>';
    } else {
        htmltext +='<li class="page-item">';
        htmltext +='<button class="page-link bg-outline-info " style="border-radius: 25px;"';
        htmltext +='value='+ json.previous + ' ';
        htmltext +='onclick=get_users(this) >Prev.</button>';
    }

    htmltext +='</li>';
    htmltext +='<li><span class="px-3 py-auto text-muted">Page '+ json.current_page_number +' of '+ json.total_pages +' </span></li>';

    if (json.next == null){
        htmltext +='<li class="page-item disabled">';
        htmltext +='<span class="page-link" style="border-radius: 25px;">Next</span>';
    } else {
        htmltext +='<li class="page-item">';
        htmltext +='<button class="page-link bg-outline-info " style="border-radius: 25px;"';
        htmltext +='value='+ json.next + ' ';
        htmltext +='onclick=get_users(this) >Next</button>';
    }
    
    htmltext +='</li>';
    htmltext +='</ul>';
    
    return htmltext;
}




function get_doctors(element)
{   
    let link = "";
    if (element==undefined){
        link = "/patient/appointments/";
    } else {
        link = element.value;
    }
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        doctors = JSON.parse(this.responseText);
        document.getElementById("selected_doctors").innerHTML = drawJSON(doctors.results);
        document.getElementById("usersPagination").innerHTML = draw_pagination(doctors);
      }
    }
    
    xhttp.open("GET", link , true);
    xhttp.send();   
}  



function serach_doctors(element)
{   
    speciality =  element.id
    var checkbox = document.getElementById(speciality);

    if (checkbox.checked == true){   
        json[speciality] = true;
    } else {
        json[speciality] = false;
    }
    

    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        doctors = JSON.parse(this.responseText);
        document.getElementById("selected_doctors").innerHTML = drawJSON(doctors.results);
        document.getElementById("usersPagination").innerHTML = draw_pagination(doctors);
      }
    }
    
    xhttp.open("GET", "/patient/appointments/?"+jsonToLink(json) , true);
    xhttp.send();   
}  



function book_appoint(element){
    pk = element.id
    var date = document.getElementById('book_date'+pk).value;
    data = {};
    data['date'] = date;
    data['pk']   = pk;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/patient/myappoints/", true);

    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
        if (this.readyState == 4 && this.status == 200)
        {
            response = JSON.parse(this.responseText);
            var r=confirm("Reserved Successfully");
            if (r==true)
            {
                 window.location = response.redirect ;
            }
        }
    }
    
    xhttp.send(JSON.stringify(data));   

}



function jsonToLink(json){
    let link = "";
    for (let special in json){
        if (json[special] == true){
            link += 'search=' + special +'&';
        }
    } 
    return link;
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