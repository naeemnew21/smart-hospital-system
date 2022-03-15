

function draw_labs(labs){
    let htmltext = '';
    for(let lab in labs){ 
        htmltext += '<div class="p-4 m-4 mx-auto container  border bg-white shadow-sm" id="Analysis'+ labs[lab].id +'" style="border-radius:25px; min-width:330px">';
        htmltext += '<div class="row">';
        htmltext += '<div class="col-10">';
        htmltext += '<h2 class="fw-bold">Dr. '+labs[lab].doctor_name +'</h2>';
        htmltext += '</div>';
        htmltext += '<div class="col-2">';
        htmltext += '<button class="btn btn-outline-dark fw-bold rounded-pill btn-sm d-flex align-items-center ms-auto" id='+ labs[lab].id +'  onclick="generateLabPDF(this);"><i class="fa-solid fa-print p-1"></i><span class="d-none d-md-flex p-1">Print</span></button>';
        htmltext += '</div>';
        htmltext += '</div>';
        htmltext += '<hr>';

        htmltext += '<table class="table table-striped table-bordered ">';
        htmltext += '<thead>';
        htmltext += ' <tr>';
        htmltext += '<th scope="col">Analysis</th>';
        htmltext += '<th scope="col">Date</th>';
        htmltext += '</tr>';
        htmltext += '</thead>';
        htmltext += '<tbody>';
        htmltext += '<tr>';
        htmltext += '<td>';
        htmltext += labs[lab].category;
        htmltext += '</td>';
        htmltext += '<td>';
        htmltext += labs[lab].date;
        htmltext += '</td>';
        htmltext += '</tr>';
        htmltext += '</tbody>';
        htmltext += '</table>';
        htmltext += '</div>';

    }
    return htmltext;
}




get_labs()

function get_labs(element)
{   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        labs = JSON.parse(this.responseText);
        document.getElementById("All_Labs").innerHTML = draw_labs(labs);
      }
    }
    xhttp.open("GET", '/patient/labs/', true);
    xhttp.send();   
}  

