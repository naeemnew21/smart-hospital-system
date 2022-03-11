

                
                  

                


function draw_pres(pres){
    let htmltext = '';
    for(let prescription in pres){ 
        htmltext += '<div class="p-4 m-4 mx-auto container  border bg-white shadow-sm" id="Prescription'+pres[prescription].prescription_id +'" style="border-radius:25px; min-width:330px">';
        htmltext += '<div class="row">';
        htmltext += '<div class="col-10">';
        htmltext += '<h2 class="fw-bold">Dr. '+pres[prescription].doctor_name +'</h2>';
        htmltext += '</div>';
        htmltext += '<div class="col-2">';
        htmltext += '<button class="btn btn-outline-dark fw-bold rounded-pill btn-sm d-flex align-items-center ms-auto" id='+pres[prescription].prescription_id +'  onclick="generatePDF(this);"><i class="fa-solid fa-print p-1"></i><span class="d-none d-md-flex p-1">Print</span></button>';
        htmltext += '</div>';
        htmltext += '</div>';
        htmltext += '<hr>';

        htmltext += '<table class="table table-striped table-bordered ">';
        htmltext += '<thead>';
        htmltext += ' <tr>';
        htmltext += '<th scope="col">Drug name</th>';
        htmltext += '<th scope="col">No. units</th>';
        htmltext += '<th scope="col">Unit</th>';
        htmltext += '<th scope="col">No. times</th>';
        htmltext += '<th scope="col">Time</th>';
        htmltext += '<th scope="col">Note</th>';
        htmltext += '</tr>';
        htmltext += '</thead>';
        htmltext += '<tbody>';
        for(let medicine in pres[prescription].details){
            htmltext += '<tr>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].medicine_name;
            htmltext += '</td>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].number_of_units;
            htmltext += '</td>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].unit;
            htmltext += '</td>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].number_of_times;
            htmltext += '</td>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].time;
            htmltext += '</td>';
            htmltext += '<td>';
            htmltext += pres[prescription].details[medicine].notes;
            htmltext += '</td>';
            htmltext += '</tr>';
        }
        htmltext += '</tbody>';
        htmltext += '</table>';
        htmltext += '</div>';

    }
    return htmltext;
}




get_pres()

function get_pres(element)
{   
    var xhttp = new XMLHttpRequest();
    xhttp.onreadystatechange = function()
    {
      if (this.readyState == 4 && this.status == 200)
      {
        pres = JSON.parse(this.responseText);
        document.getElementById("All_Prescriptions").innerHTML = draw_pres(pres);
      }
    }
    xhttp.open("GET", '/patient/pres/', true);
    xhttp.send();   
}  

