var prescriptionModal = document.getElementById('prescriptionModal')
prescriptionModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var patient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalBodyInput = prescriptionModal.querySelector('.modal-body input')

  modalBodyInput.value = patient
})

var analysisModal = document.getElementById('analysisModal')
analysisModal.addEventListener('show.bs.modal', function (event) {
  // Button that triggered the modal
  var button = event.relatedTarget
  // Extract info from data-bs-* attributes
  var patient = button.getAttribute('data-bs-whatever')
  // If necessary, you could initiate an AJAX request here
  // and then do the updating in a callback.
  //
  // Update the modal's content.
  var modalBodyInput = analysisModal.querySelector('.modal-body input')

  modalBodyInput.value = patient
})

///////////////////////////////////////////////////////////////////////////////////////
// Prescription form

document.getElementById('prescriptForm').addEventListener('submit', onFormSubmit)
var selectedRow = null

function onFormSubmit(e) {
    e.preventDefault();
    var formData = readFormData();
    if (selectedRow == null)
        insertNewRecord(formData);
    else
        updateRecord(formData);
    resetForm();

}

function readFormData() {
    var formData = {};
    formData["DrugNo"] = document.getElementById("DrugNo").value;
    formData["DrugName"] = document.getElementById("DrugName").value;
    formData["NoUnits"] = document.getElementById("NoUnits").value;
    formData["NoTimes"] = document.getElementById("NoTimes").value;
    return formData;
}

function insertNewRecord(data) {
    var table = document.getElementById("prescriptList").getElementsByTagName('tbody')[0];
    var newRow = table.insertRow(table.length);
    cell1 = newRow.insertCell(0);
    cell1.innerHTML = data.DrugNo;
    cell2 = newRow.insertCell(1);
    cell2.innerHTML = data.DrugName;
    cell3 = newRow.insertCell(2);
    cell3.innerHTML = data.NoUnits;
    cell4 = newRow.insertCell(3);
    cell4.innerHTML = data.NoTimes;
    cell4 = newRow.insertCell(4);
    cell4.innerHTML = `<a class="btn btn-secondary fw-bold px-2 text-white  btn-sm rounded-pill" onClick="onEdit(this)">Edit</a>
                      <a class="btn btn-danger fw-bold px-2 text-white btn-sm rounded-pill" onClick="onDelete(this)">Delete</a>`;
}

function resetForm() {
    document.getElementById("DrugNo").value = "";
    document.getElementById("DrugName").value = "";
    document.getElementById("NoUnits").value = "";
    document.getElementById("NoTimes").value = "";
    selectedRow = null;
}

function onEdit(td) {
    selectedRow = td.parentElement.parentElement;
    document.getElementById("DrugNo").value = selectedRow.cells[0].innerHTML;
    document.getElementById("DrugName").value = selectedRow.cells[1].innerHTML;
    document.getElementById("NoUnits").value = selectedRow.cells[2].innerHTML;
    document.getElementById("NoTimes").value = selectedRow.cells[3].innerHTML;
}
function updateRecord(formData) {
    selectedRow.cells[0].innerHTML = formData.DrugNo;
    selectedRow.cells[1].innerHTML = formData.DrugName;
    selectedRow.cells[2].innerHTML = formData.NoUnits;
    selectedRow.cells[3].innerHTML = formData.NoTimes;
}

function onDelete(td) {
    if (confirm('Are you sure to delete this record ?')) {
        row = td.parentElement.parentElement;
        document.getElementById("prescriptList").deleteRow(row.rowIndex);
        resetForm();
    }
}

////////////////////////////////////////////////////////////////////////////////
// Patient database search by name

document.getElementById("myInput").addEventListener('keyup',myFunction);
function myFunction() {
// Declare variables
var input, filter, table, tr, td, i, txtValue;
input = document.getElementById("myInput");
filter = input.value.toLowerCase();
table = document.getElementById("myTable");
tr = table.getElementsByTagName("tr");

// Loop through all table rows, and hide those who don't match the search query
for (i = 0; i < tr.length; i++) {
  td = tr[i].getElementsByClassName("patientDB")[0];
  if (td) {
    txtValue = td.textContent || td.innerText;
    
    if (txtValue.toLowerCase().indexOf(filter) > -1) {
      tr[i].style.display = "";
    } else {
      tr[i].style.display = "none";
    }
  }
}
}