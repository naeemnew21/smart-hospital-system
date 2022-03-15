               
                    
function drawJSON(json)
{
    let htmltext = "";
    for (let appoint in json.results){
        var x  = parseInt(appoint) +1;

        htmltext +='<tr data-bs-toggle="collapse" style="cursor: pointer;" data-bs-target="#EMR'+x+'">';
        htmltext +='<th scope="row">'+ x +'</th>';
        htmltext +='<td class="patientDB">'+ json.results[appoint].patient_name +'</td>';
        htmltext +='<td colspan="2">'+ json.results[appoint].appointment_date +'</td>';
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



get_patients();

function get_patients(element)
{   
    let link = "";
    if (element==undefined){
        link = "/dr/patients/";
    } else {
        link = element.value;
    }
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        patients = JSON.parse(this.responseText);
        document.getElementById("visitshistory").innerHTML = drawJSON(patients);
        document.getElementById("usersPagination").innerHTML = draw_pagination(patients);
      }
    }
    
    xhttp.open("GET", link , true);
    xhttp.send();   
}  




function serach_patients(element)
{   
    let data = document.getElementById("searchpatient").value;
    
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        patients = JSON.parse(this.responseText);
        document.getElementById("visitshistory").innerHTML = drawJSON(patients);
        document.getElementById("usersPagination").innerHTML = draw_pagination(patients);
      }
    }
    
    xhttp.open("GET", "/dr/patients/?search="+data , true);
    xhttp.send();   
}  
 





  



function draw_head(patient)
{
    let htmltext = "";
    
    htmltext +='<h2 class="accordion-header" id="panelsStayOpen-headingOne">';
    htmltext +='<button class="accordion-button" type="button" data-bs-toggle="collapse" data-bs-target="#panelsStayOpen-'+patient.patient+'" aria-expanded="false" aria-controls="panelsStayOpen-collapseOne">';
    htmltext +='<div class="col d-flex align-items-center">';
    htmltext +='<img src="'+patient.avatar+'" alt="" width="30" height="30" class="rounded-circle border me-2 border-white border-2 ">';
    htmltext +='<div class="col d-flex flex-column">';
    htmltext +='<p class=" fw-bold my-auto" >'+patient.patient_name+'</p>';
    htmltext +='</div>';
    htmltext +='</div>';
    htmltext +='</button>';
    htmltext +='</h2>';
   
    return htmltext;
}




function draw_body(patient)
{
    let htmltext = "";

    htmltext +='<div id="panelsStayOpen-'+patient.patient+'" class="accordion-collapse collapse" aria-labelledby="panelsStayOpen-headingOne">';
    htmltext +='<div class="accordion-body">';
    htmltext +='<div class="col d-flex justify-content-end" style="border: 1px solid #e7e7e7; border-radius:25px; padding: 0.4rem;">';
    htmltext +='<a onclick=get_modal_prescription(this) data-name='+patient.patient+' class="btn btn-primary btn-sm rounded-pill fw-bold  px-3 align-items-center d-flex" role="button" data-bs-toggle="modal" data-bs-target="#prescriptionModal'+patient.patient+'" ><i class="fa-solid fa-prescription me-1"></i><span class="d-md-flex d-none">Prescriptions</span> </a>';
   
    htmltext +='<a onclick=get_modal_lab(this) data-name='+patient.patient+' class="btn btn-primary btn-sm rounded-pill fw-bold  px-3 align-items-center mx-2 d-flex" role="button" data-bs-toggle="modal" data-bs-target="#labModal'+patient.patient+'" data-bs-whatever="@First_patient_analyis"><i class="fa-solid fa-vial me-1"></i><span class="d-md-flex d-none">Analyses</span></a>';

    htmltext +='</div>';

    htmltext +='<hr>';
    htmltext +='<table class="table table-striped  table-bordered"> ';
    htmltext +='<tbody>';
    htmltext +='<tr>';
    htmltext +='<th scope="col" rowspan="5" class="align-middle text-center">General history</th>';
    htmltext +='<th scope="col">Name</th>';
    htmltext +='<td scope="col">'+patient.patient_name+'</td>';
    htmltext +='</tr>';
    htmltext +='<tr>';
    htmltext +='<th scope="col">Gender</th>';
    htmltext +='<td scope="col">'+patient.sex+'</td>';
    htmltext +='</tr>';
    htmltext +='<tr>';
    htmltext +='<th scope="col">Marital Status</th>';
    htmltext +='<td scope="col">'+patient.marital_status+'</td>';
    htmltext +='</tr>';
    htmltext +='<tr>';
    htmltext +='<th scope="col">Blood Type</th>';
    htmltext +='<td scope="col">'+patient.blood_type+'</td>';
    htmltext +='</tr>';
    htmltext +='<tr>';
    htmltext +='<th scope="col">Age</th>';
    htmltext +='<td scope="col">'+patient.age+'</td>';
    htmltext +='</tr>';

    htmltext +='</tr>';
    htmltext +='<tr>';
    htmltext +='<th scope="col" class="align-middle text-center">Reports</th>';
    htmltext +='<td scope="col" colspan="2">';
    htmltext +='<ul>';
    htmltext +='<li>reports required</li>';
    htmltext +='</ul>';
    htmltext +='</td>';
    htmltext +='</tr>';
    htmltext +='</tbody>';
    htmltext +='</table>';
    htmltext +='</div>';
    htmltext +='</div>';

    return htmltext;
}


function draw_prescription_modal(patients)
{
    let htmltext = "";

    for (let patient in patients){
        var pk = patients[patient].patient;

        htmltext +='<div class="modal fade " id="prescriptionModal'+patients[patient].patient +'" tabindex="-1" aria-labelledby="prescriptionModalLabel" aria-hidden="true" style="min-width: fit-content;">';
        htmltext +='<div class="modal-dialog modal-xl   " >';
        htmltext +='<div class="modal-content border-0 px-2" style="border-radius:25px">';
        htmltext +='<div class="modal-header" >';
        htmltext +='<h3 class="modal-title fw-bold" id="exampleModalLabel">Prescriptions utility</h3>';
        htmltext +='<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>';
        htmltext +='</div>';
        htmltext +='<div class="modal-body">';
        htmltext +='<div class="container m-3 mx-auto bg-white  " style="border-radius:25px ;">';
        htmltext +='<h4 class="pb-2 border-bottom fw-bold m">Add prescription</h4>';
        
        htmltext +='<div class="employee-form">';
        htmltext +='<form class="row g-3" id="prescriptForm" autocomplete="off">';
        htmltext +='<div>';
        htmltext +='<label for="patient-name" class="col-form-label">patient name:</label>';
        htmltext +='<input type="text" value='+patients[patient].patient_name+' class="form-control" id="patient-name" readonly>';
        htmltext +='</div>';

        htmltext +='<div>';
        htmltext +='<label>Medicine name*</label><label class="validation-error hide" id="fullNameValidationError"></label>';
        htmltext +='<input id="medicine_name'+pk+'" name="medicine_name" class="form-control" type="text"  id="DrugNo">';
        htmltext +='</div>';

        htmltext +='<div class="col-sm-12 col-md-6">';
        htmltext +='<label>Number of units*</label>';
        htmltext +='<input id="number_of_units'+pk+'" name="number_of_units" class="form-control" type="number" value=""></input>';
        htmltext +='</div>';

        htmltext +='<div class="col-sm-12 col-md-6">';
        htmltext +='<label>Unit*</label>';
        htmltext +='<select class="form-control" id="medicine_unit'+pk+'" name="medicine_unit">'+
                      '<option value="" selected="">--------</option>'+
                      '<option value="Tab">Tab</option>'+
                    '<option value="ml">ml</option>'+
                    '</select>';
        htmltext +='</div>';
       

        htmltext +='<div class="col-sm-12 col-md-6">';
        htmltext +='<label>Number of times*</label>';
        htmltext +='<input id="number_of_times'+pk+'" name="number_of_times" class="form-control" type="number" value=""></input>';
        htmltext +='</div>';


        htmltext +='<div class="col-sm-12 col-md-6">';
        htmltext +='<label>Time*</label>';
        htmltext +='<select class="form-control" id="medicine_time'+pk+'" name="medicine_time">'+
                      '<option value="" selected="">--------</option>'+
                      '<option value="After">After</option>'+
                    '<option value="Before">Before</option>'+
                    '</select>';
        htmltext +='</div>';


        htmltext +='<div>';
        htmltext +='<label>Notes</label>';
        htmltext +='<input id="medicine_notes'+pk+'" name="medicine_notes" class="form-control" type="text">';
        htmltext +='</div>';


        htmltext +='<div  class="form-action-buttons">';
        htmltext +='<input type="button" class="btn btn-primary rounded-pill px-3 fw-bold text-white" value="+ Add drug"';
        htmltext +=' id='+pk;
        htmltext +=' name='+patients[patient].appoint_request;
        htmltext +=' onclick=add_medicine(this)';
        htmltext +='>';
        htmltext +='</div>';

        htmltext +='<div  class="form-action-buttons">';
        htmltext +='<input type="button" class="btn btn-primary rounded-pill px-3 fw-bold text-white" value="empty form"';
        htmltext +=' id='+pk;
        htmltext +=' onclick=empty_medicine(this)';
        htmltext +='>';
        htmltext +='</div>';

        htmltext +='</form>';
        htmltext +='</div>';

        htmltext +='</div>';
        htmltext +='<br/>';
     
        htmltext +='<div class = "employees-table container p-3 bg-white border" style="border-radius: 25px;">';
      
        htmltext +='<table class="table table-bordered" id="prescriptList">';
        htmltext +='<thead>';
        htmltext +='<tr>';
        htmltext +='<th>Drug Name</th>';
        htmltext +='<th>Quantity</th>';
        htmltext +='<th>Unit</th>';
        htmltext +='<th>Times</th>';
        htmltext +='<th>Note</th>';
        htmltext +='<th>Delete</th>';
        htmltext +='</tr>';
        htmltext +='</thead>';
        htmltext +='<tbody id="prescription'+pk+'">  </tbody>';
        htmltext +='</table>';

        htmltext +='</div>';

        htmltext +='</div>';
        htmltext +='</div>';
        htmltext +='</div>';
        htmltext +='</div>';
        
    }

    return htmltext;
}


function draw_lab_modal(patients)
{
    let htmltext = "";

    for (let patient in patients){
        var pk = patients[patient].patient;

        htmltext +='<div class="modal fade " id="labModal'+patients[patient].patient +'" tabindex="-1" aria-labelledby="labModalLabel" aria-hidden="true" style="min-width: fit-content;">';
        htmltext +='<div class="modal-dialog modal-xl   " >';
        htmltext +='<div class="modal-content border-0 px-2" style="border-radius:25px">';
        htmltext +='<div class="modal-header" >';
        htmltext +='<h3 class="modal-title fw-bold" id="exampleModalLabel">lab utility</h3>';
        htmltext +='<button type="button" class="btn-close" data-bs-dismiss="modal" aria-label="Close"></button>';
        htmltext +='</div>';
        htmltext +='<div class="modal-body">';
        htmltext +='<div class="container m-3 mx-auto bg-white  " style="border-radius:25px ;">';
        htmltext +='<h4 class="pb-2 border-bottom fw-bold m">Add Analysis</h4>';
        
        htmltext +='<div class="employee-form">';
        htmltext +='<form class="row g-3" id="prescriptForm" autocomplete="off">';
        htmltext +='<div>';
        htmltext +='<label for="patient-name" class="col-form-label">patient name:</label>';
        htmltext +='<input type="text" value='+patients[patient].patient_name+' class="form-control" id="patient-name" readonly>';
        htmltext +='</div>';

        htmltext +='<div>';
        htmltext +='<label>Analysis name*</label><label class="validation-error hide" id="fullNameValidationError"></label>';
        htmltext +='<input id="analysis_name'+pk+'" name="analysis_name" class="form-control" type="text"  id="DrugNo">';
        htmltext +='</div>';


        htmltext +='<div  class="form-action-buttons">';
        htmltext +='<input type="button" class="btn btn-primary rounded-pill px-3 fw-bold text-white" value="+ Add Analysis"';
        htmltext +=' id='+pk;
        htmltext +=' name='+patients[patient].appoint_request;
        htmltext +=' onclick=add_lab(this)';
        htmltext +='>';
        htmltext +='</div>';

        htmltext +='</form>';
        htmltext +='</div>';

        htmltext +='</div>';
        htmltext +='<br/>';
     
        htmltext +='<div class = "employees-table container p-3 bg-white border" style="border-radius: 25px;">';
      
        htmltext +='<table class="table table-bordered" id="prescriptList">';
        htmltext +='<thead>';
        htmltext +='<tr>';
        htmltext +='<th>Analysis Name</th>';
        htmltext +='<th>Delete</th>';
        htmltext +='</tr>';
        htmltext +='</thead>';
        htmltext +='<tbody id="analysis'+pk+'">  </tbody>';
        htmltext +='</table>';

        htmltext +='</div>';

        htmltext +='</div>';
        htmltext +='</div>';
        htmltext +='</div>';
        htmltext +='</div>';
        
    }

    return htmltext;
}
 



function draw_prescription(prescription)
{
    let htmltext = "";

    for (let medicine in prescription.details){
        htmltext +='<tr>';
        htmltext +='<td>'+prescription.details[medicine].medicine_name+'</td>';
        htmltext +='<td>'+prescription.details[medicine].number_of_units+'</td>';
        htmltext +='<td>'+prescription.details[medicine].unit+'</td>';
        htmltext +='<td>'+prescription.details[medicine].number_of_times+'</td>';
        htmltext +='<td>'+prescription.details[medicine].time+'</td>';
        htmltext +='<td><a id='+medicine+'  name='+prescription.patient+' type="button" class="btn btn-danger fw-bold px-2 text-white btn-sm rounded-pill" onClick="del_medicine(this)">Delete</a></td>';
        htmltext +='</tr>';
    }
    return htmltext;
}


function draw_lab(labs)
{
    let htmltext = "";
    for (let lab in labs){
        htmltext +='<tr>';
        htmltext +='<td>'+labs[lab].category+'</td>';
        htmltext +='<td><a id='+labs[lab].id+'  name='+labs[lab].patient+' type="button" class="btn btn-danger fw-bold px-2 text-white btn-sm rounded-pill" onClick="del_lab(this)">Delete</a></td>';
        htmltext +='</tr>';
    }
    return htmltext;
}




function draw_patient(json)
{
    let htmltext = "";
    for (let patient in json){
        htmltext +='<div class="accordion-item">';
        htmltext += draw_head(json[patient]);
        htmltext += draw_body(json[patient]);
        htmltext +='</div>';
    }
    return htmltext;
}

                        


 

get_today_patients();

function get_today_patients(element)
{   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        patients = JSON.parse(this.responseText);
        document.getElementById("today_patient_list").innerHTML = draw_patient(patients);
        document.getElementById("prescription_modals").innerHTML = draw_prescription_modal(patients);
        document.getElementById("lab_modals").innerHTML = draw_lab_modal(patients);
      }
    }
    
    xhttp.open("GET", '/dr/today/' , true);
    xhttp.send();   
}  

 

function get_prescription(patiend_id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        prescription = JSON.parse(this.responseText);
        document.getElementById("prescription"+patiend_id).innerHTML = draw_prescription(prescription);
      }
    }
    
    xhttp.open("GET", '/dr/pre/'+patiend_id , true);
    xhttp.send();   
}



function get_modal_prescription(element){
    var patiend_id = element.dataset.name;
    get_prescription(patiend_id);
}






function add_medicine(element)
{
    let pk = element.id;

    let data = {};
    data['medicine_name']   = document.getElementById("medicine_name"+pk).value;
    data['number_of_units'] = document.getElementById("number_of_units"+pk).value;
    data['unit']            = document.getElementById("medicine_unit"+pk).value;
    data['number_of_times'] = document.getElementById("number_of_times"+pk).value;
    data['time']            = document.getElementById("medicine_time"+pk).value;
    data['notes']           = document.getElementById("medicine_notes"+pk).value;
    data['patient']         = pk;
    data['appoint_request'] = element.name;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/dr/addmed/", true);
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 201)
      {
        medicine = JSON.parse(this.responseText);
        get_prescription(pk);
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}



function del_medicine(element)
{
    let pk      = element.id;
    let patient = element.name
    
    var xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "/dr/delmed/"+pk, true);
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 204)
      {
        get_prescription(patient);
      }
    }
    
    xhttp.send();   
}




function empty_medicine(element)
{
    let pk = element.id;
    document.getElementById("medicine_name"+pk).value   = '';
    document.getElementById("number_of_units"+pk).value = '';
    document.getElementById("medicine_unit"+pk).value   = '';
    document.getElementById("number_of_times"+pk).value = '';
    document.getElementById("medicine_time"+pk).value   = '';
    document.getElementById("medicine_notes"+pk).value  = '';

}





function get_lab(patiend_id){
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        labs = JSON.parse(this.responseText);
        document.getElementById("analysis"+patiend_id).innerHTML = draw_lab(labs);
      }
    }
    
    xhttp.open("GET", '/dr/lab/'+patiend_id , true);
    xhttp.send();   
}



function get_modal_lab(element){
    var patiend_id = element.dataset.name;
    get_lab(patiend_id);
}





function add_lab(element)
{
    let pk = element.id;

    let data = {};
    data['category'] = document.getElementById("analysis_name"+pk).value;
    data['patient']  = pk;
    data['appoint']  = element.name;

    var xhttp = new XMLHttpRequest();
    xhttp.open("POST", "/dr/addlab/", true);
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 201)
      {
        medicine = JSON.parse(this.responseText);
        get_lab(pk);
      }
    }
    
    xhttp.send(JSON.stringify(data));   
}


function del_lab(element)
{
    let pk      = element.id;
    let patient = element.name;

    var xhttp = new XMLHttpRequest();
    xhttp.open("DELETE", "/dr/dellab/"+pk, true);
    const csrftoken = getCookie('csrftoken');
    xhttp.setRequestHeader('x-csrftoken', csrftoken)
    xhttp.setRequestHeader('Content-Type', 'application/json; charset=UTF-8')
    xhttp.setRequestHeader('Accept', 'application/json')

    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 204)
      {
        get_lab(patient);
      }
    }
    
    xhttp.send();   
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