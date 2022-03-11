
get_users();


function draw_staff(json, user)
{
    let htmltext = "";
    var job_pk = json.results[user].job_id;
    htmltext +='<form class="row g-3" autocomplete="off" method="post" ';
    htmltext +=' id="jobform'+job_pk+'">';
    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4  d-flex flex-column">';
    htmltext +='<label for="job" class="col-form-label">Job</label>';
    htmltext +='<select class="form-select" name="job" ';
    htmltext +=' id="job'+ job_pk +'"';
    htmltext +='>';
    for (let j in json.joblist){
        htmltext +='<option value='+json.joblist[j]+'>'+json.joblist[j]+'</option>';
    }
    htmltext +='</select>';
    htmltext +='</div>';

    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex flex-column">';
    htmltext +='<label class="col-form-label">Experience</label>';
    htmltext +='<input class="form-control" type="number" name="experience" step="1" ';
    htmltext +=' value='+ json.results[user].experience ;
    htmltext +=' id="experience'+ job_pk +'"';
    htmltext +='>';
    htmltext +='</div>';

    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex  flex-column">';
    htmltext +='<label class="col-form-label">Degree</label>';
    htmltext +='<select class="form-select" name="degree" ';
    htmltext +=' id="degree'+ job_pk +'"';
    htmltext +='>';
    for (let deg in json.degreelist){
        htmltext +='<option value='+json.degreelist[deg]+'>'+json.degreelist[deg]+'</option>';
    }
    htmltext +='</select>';
    htmltext +='</div>';
    htmltext +='<div  class="form-action-buttons">';
    htmltext +='<input type="button" class="btn btn-primary rounded-pill fw-bold text-white w-100 mb-2" value="Save changes"';
    htmltext +=' name="job'+job_pk+'"';
    htmltext +=' id='+job_pk;
    htmltext +=' onclick=update_job(this)';
    htmltext +='>';
    htmltext +='</div>';
    htmltext +='</form>';
    
    return htmltext;
}




function draw_work_days(json, user){
    var job_pk = json.results[user].job_id;

    let htmltext = "";

    htmltext +='<form class="row g-3" autocomplete="off" method="post" ';
    htmltext +=' id="jobdaysform'+job_pk+'">';

    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4  d-flex flex-column">';
    htmltext +='<label for="job" class="col-form-label">Day</label>';
    htmltext +='<select class="form-select" name="day_name" ';
    htmltext +=' id="jobday'+ job_pk +'"';
    htmltext +='>';
    htmltext +='<option value="Sat">Sat</option>';
    htmltext +='<option value="Sun">Sun</option>';
    htmltext +='<option value="Mon">Mon</option>';
    htmltext +='<option value="Tue">Tue</option>';
    htmltext +='<option value="Wed">Wed</option>';
    htmltext +='<option value="Thu">Thu</option>';
    htmltext +='<option value="Fri">Fri</option>';
    htmltext +='</select>';
    htmltext +='</div>';

    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex flex-column">';
    htmltext +='<label class="col-form-label">Start Time</label>';
    htmltext +='<input class="form-control" type="time" name="start_time" ';
    htmltext +=' id="jobstart'+ job_pk +'"';
    htmltext +='>';
    htmltext +='</div>';

    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex  flex-column">';
    htmltext +='<label class="col-form-label">End Time</label>';
    htmltext +='<input class="form-control" type="time" name="end_time" ';
    htmltext +=' id="jobend'+ job_pk +'"';
    htmltext +='>';
    htmltext +='</div>';

    htmltext +='<div  class="form-action-buttons">';
    htmltext +='<input type="button" class="btn btn-primary rounded-pill fw-bold text-white w-100 mb-2" value="Save changes"';
    htmltext +=' name="workdays'+job_pk+'"';
    htmltext +=' id='+job_pk;
    htmltext +=' onclick=update_days(this)';
    htmltext +='>';
    htmltext +='</div>';
    
    htmltext +='</form>';

    htmltext +='<div class = "employees-table container p-3 bg-white border" style="border-radius: 25px;">';
    htmltext +='<table class="table table-bordered"  ';
    htmltext +='id="daystable'+job_pk+'">';
    htmltext +='<thead>';
    htmltext +='<tr>';
    htmltext +='<th>Day</th>';
    htmltext +='<th>Start</th>';
    htmltext +='<th>End</th>';
    htmltext +='<th>Actions</th>';
    htmltext +='</tr>';
    htmltext +='</thead>';
    htmltext +='<tbody id="tbody'+job_pk+'">';

    for (let day in json.results[user].work_days){

        htmltext +='<tr>';
        htmltext +='<td>'+json.results[user].work_days[day].day+'</td>';
        htmltext +='<td>'+json.results[user].work_days[day].start+'</td>';
        htmltext +='<td>'+json.results[user].work_days[day].end+'</td>';
        htmltext +='<td><button class="btn btn-danger fw-bold px-2 text-white btn-sm rounded-pill" onClick="delete_days(this)" ';
        htmltext +=' name='+day;
        htmltext +=' id='+job_pk;
        htmltext +='>Delete</button></td>';
        htmltext +='</tr>';
    }

    htmltext +='</tbody>';
    htmltext +='</table>';
    htmltext +='</div>';
    htmltext +='<hr>';
    return htmltext;
}




function draw_dr(json, user){
    var dr_pk = json.results[user].dr_id;

    let htmltext = "";

    htmltext +='<form class="row g-3" autocomplete="off" method="post">';
    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4  d-flex flex-column">';
    htmltext +='<label for="dr" class="col-form-label">dr</label>';
    htmltext +='<select class="form-select" ';
    htmltext +=' id="dr'+ dr_pk +'"';
    htmltext +='>';
    for (let sp in json.specials){
        htmltext +='<option value='+json.specials[sp]+'>'+json.specials[sp]+'</option>';
    }
    htmltext +='</select>';
    htmltext +='</div>';

    htmltext +='<div  class="form-action-buttons">';
    htmltext +='<input type="button" class="btn btn-primary rounded-pill fw-bold text-white w-100 mb-2" value="Save changes"';
    htmltext +=' name="dr'+dr_pk+'"';
    htmltext +=' id='+dr_pk;
    htmltext +=' onclick=update_dr(this)';
    htmltext +='>';
    htmltext +='</div>';
    htmltext +='</form>';
    return htmltext;
}


function draw_secretary(json, user){
    var sec_pk = json.results[user].sec_id;
    var dr_id  = json.results[user].sec_doc;

    let htmltext = "";
    htmltext +='<form class="row g-3" autocomplete="off" method="post">';
    htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex flex-column">';
    htmltext +='<label class="col-form-label" id="sec_doc'+sec_pk+'">Related Doctor ( '+dr_id+' ) *enter national id</label>';
    htmltext +='<input class="form-control" type="number" name="experience" step="1" ';
    htmltext +=' id="secretary'+ sec_pk +'"';
    htmltext +='>';
    htmltext +='</div>';

    htmltext +='<div  class="form-action-buttons">';
    htmltext +='<input type="button" class="btn btn-primary rounded-pill fw-bold text-white w-100 mb-2" value="Save changes"';
    htmltext +=' id='+sec_pk;
    htmltext +=' onclick=update_secretary(this)';
    htmltext +='>';
    htmltext +='</div>';
    htmltext +='</form>';

    return htmltext;
}





function drawJSON(json)
{
    let htmltext = "";

    for (let user in json.results){
        var x  = parseInt(user) +1;
        var pk = json.results[user].id;

        htmltext += '<tr >';
        htmltext +='<th scope="row" class="text-muted ">'+x+'</th>';
        htmltext +='<td>'+json.results[user].first_name+'</td>';
        htmltext +='<td>'+json.results[user].national_id+'</td>';

        if (json.results[user].is_staff == true){
            htmltext +='<td id="tstaff'+ pk +'"><span class="bg-primary p-1 rounded-pill badge">'+json.results[user].is_staff+'</span></td>';
        } else {
            htmltext +='<td id="tstaff'+ pk +'"><span class="bg-warning p-1 rounded-pill badge text-dark">'+json.results[user].is_staff+'</span></td>';
        }
        
        if (json.results[user].is_active == true){
            htmltext +='<td id="tstatus'+ pk +'"><span class="bg-primary p-1 rounded-pill badge">'+json.results[user].is_active+'</span></td>';
        } else {
            htmltext +='<td id="tstatus'+ pk +'"><span class="bg-warning p-1 rounded-pill badge text-dark">'+json.results[user].is_active+'</span></td>';
        }

        htmltext +='<td ><a href="" data-bs-toggle="collapse" class="link-dark" data-bs-target="#staff'+ user +'"><i class="fa-regular fa-pen-to-square"></i></a></td>';
        htmltext +='</tr>';
        htmltext +='<tr > <!--------Staff Edit form------------------------>';
        htmltext +='<td colspan="12" style="padding:0 !important">';
        htmltext +='<div class=" collapse" id="staff'+ user +'" >';

        htmltext +='<form class="row g-3" autocomplete="off" method="post">';

        htmltext +='<div class="col-sm-12 col-md-6 col-lg-4  d-flex flex-column">';
        htmltext +='<label for="status" class="col-form-label">Status</label>';
        htmltext +='<input type="checkbox" name="status"';
        htmltext +=' id="status'+ pk +'"';
        if (json.results[user].is_active == true){
            htmltext +=' checked';
        }
        htmltext +='>';
        htmltext +='</div>';


        htmltext +='<div class="col-sm-12 col-md-6 col-lg-4 d-flex flex-column">';
        htmltext +='<label for="staff" class="col-form-label"> Staff</label>';
        htmltext +='<input type="checkbox" name="staff"';
        htmltext +=' id="staff'+ pk +'"';
        if (json.results[user].is_staff == true){
            htmltext +=' checked';
        }
        htmltext +='>';
        htmltext +='</div>';

        htmltext +='<div  class="form-action-buttons">';
        htmltext +='<input type="button" class="btn btn-primary rounded-pill fw-bold text-white w-100 mb-2" value="Save changes"';
        htmltext +=' name="user'+pk+'"';
        htmltext +=' id='+pk;
        htmltext +=' onclick=update_user(this)';
        htmltext +='>';
        htmltext +='</div>';
        htmltext +='</form>';
        
        if (json.results[user].is_staff == true){
            htmltext += draw_staff(json, user);
            htmltext += draw_work_days(json, user);
            if (json.results[user].job == 'Dr'){
                htmltext += draw_dr(json, user);
            } 
            if (json.results[user].job == 'Secretary'){
                htmltext += draw_secretary(json, user);
            } 
        }

        htmltext +='</div>';
        htmltext +='</td>';
        htmltext +='</tr>';
    }
    
    return htmltext;
}

function draw_table(json, job_pk)
{
    let htmltext = "";
    for (let day in json){

        htmltext +='<tr>';
        htmltext +='<td>'+json[day].day_name+'</td>';
        htmltext +='<td>'+json[day].start_time+'</td>';
        htmltext +='<td>'+json[day].end_time+'</td>';
        htmltext +='<td><button class="btn btn-danger fw-bold px-2 text-white btn-sm rounded-pill" onClick="delete_days(this)" ';
        htmltext +=' name='+day;
        htmltext +=' id='+job_pk;
        htmltext +='>Delete</button></td>';
        htmltext +='</tr>';
    }
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

function draw_head(bool)
{
    let htmltext = "";
    if (bool == true){
        htmltext +='<span class="bg-primary p-1 rounded-pill badge">'+bool+'</span>';
    } else {
        htmltext +='<span class="bg-warning p-1 rounded-pill badge text-dark">'+bool+'</span>';
    }
    return htmltext;
}




function get_users(element)
{   
    let link = "";
    if (element==undefined){
        link = "/hr/users/";
    } else {
        link = element.value;
    }
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        all_users = JSON.parse(this.responseText);
        document.getElementById("tbody").innerHTML = drawJSON(all_users);
        document.getElementById("usersPagination").innerHTML = draw_pagination(all_users);
        set_degree(all_users);
      }
    }
    
    xhttp.open("GET", link , true);
    xhttp.send();   
}  
 




function serach_users(element)
{   
    let data = document.getElementById("search").value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        all_users = JSON.parse(this.responseText);
        document.getElementById("tbody").innerHTML = drawJSON(all_users);
        document.getElementById("usersPagination").innerHTML = draw_pagination(all_users);
        set_degree(all_users);
      }
    }
    
    xhttp.open("GET", "/hr/users/?search="+data , true);
    xhttp.send();   
}  
 



function update_user(element)
{   
    let pk = element.id;

    let data = {};
    data['is_staff']  = document.getElementById("staff"+pk).checked;
    data['is_active'] = document.getElementById("status"+pk).checked;


    const csrftoken = getCookie('csrftoken');

    var xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "/hr/users/" + pk, true);

    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        user = JSON.parse(this.responseText);
        document.getElementById("tstatus"+pk).innerHTML = draw_head(user.is_active);
        document.getElementById("tstaff"+pk).innerHTML = draw_head(user.is_staff);

      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  
 

function update_job(element)
{   
    let pk = element.id;
    
    let data = formToJSON('jobform'+pk);
    
    var xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "/hr/jobs/" + pk, true);

    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        job = JSON.parse(this.responseText);
        document.getElementById("job"+pk).value        = job.job;
        document.getElementById("experience"+pk).value = job.experience;
        document.getElementById("degree"+pk).value     = job.degree;
      }
    }
    xhttp.send(JSON.stringify(data));   
}  
 


function update_days(element)
{   
    let pk = element.id;

    let data = formToJSON('jobdaysform'+pk);

    //alert(JSON.stringify(data));

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/hr/day/" + pk, true);

    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        days = JSON.parse(this.responseText);
        document.getElementById('tbody'+pk).innerHTML = draw_table(days, pk);
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  



function delete_days(element)
{   
    let pk = element.id;
    let index = element.name;
    let data = rowToJSON('daystable'+pk, index);

    var xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "/hr/day/"+pk, true);

    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        days = JSON.parse(this.responseText);
        document.getElementById('tbody'+pk).innerHTML = draw_table(days, pk);
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  


function update_dr(element)
{   
    let pk = element.id;

    let data = {};
    data['specialty'] = document.getElementById("dr"+pk).value;

    const csrftoken = getCookie('csrftoken');

    var xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "/hr/drs/" + pk, true);

    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        dr = JSON.parse(this.responseText);
        document.getElementById("dr"+pk).value = dr.specialty;
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  
 


function update_secretary(element)
{   
    let pk = element.id;

    let data = {};
    data['doctor'] = document.getElementById("secretary"+pk).value;

    const csrftoken = getCookie('csrftoken');

    var xhttp = new XMLHttpRequest();
    xhttp.open("PUT", "/hr/sec/" + pk, true);

    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        dr = JSON.parse(this.responseText);
        document.getElementById("sec_doc"+pk).innerHTML = 'Related Doctor ( '+dr.doctor+' ) *enter national id';
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}  
 


function formToJSON(formID){
    let myForm = document.getElementById(formID);
    const formData = new FormData(myForm);
    var object = {};
    formData.forEach((value, key) => object[key] = value);
    //var json = JSON.stringify(object);
    return object;
}

function rowToJSON(tableID, row_index){
    var table  = document.getElementById(tableID);
    var tBody  = table.getElementsByTagName('tbody')[0];
    var rows   = tBody.getElementsByTagName('tr');
    var tableRow = rows[row_index].getElementsByTagName('td');

    var object = {};
    keys = ['day_name', 'start_time', 'end_time'];
    for (var t = 0; t < tableRow.length-1; t++){
        object[keys[t]] = tableRow[t].innerHTML;
    }
    return object;
}


function set_degree(json){
    for (let user in json.results){
        if (json.results[user].is_staff == true){
            var job_pk = json.results[user].job_id;
            document.getElementById("degree"+ job_pk ).value = json.results[user].degree ;
            document.getElementById("job"+ job_pk ).value = json.results[user].job ;
            if (json.results[user].job == 'Dr'){
                document.getElementById("dr"+ json.results[user].dr_id).value = json.results[user].dr ;
            }
        }
    }
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