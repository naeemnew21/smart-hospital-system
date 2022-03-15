
function generatePDF(btn) {
    var pk = btn.id;
    var element = document.getElementById('Prescription'+pk);
    var opt = {
        margin:       1,
        filename:     'myPrescription.pdf',
        image:        { type: 'jpeg', quality: 0.99 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }

    };
        
    // New Promise-based usage:
    html2pdf().set(opt).from(element).save();

    }


function generateLabPDF(btn) {
    var pk = btn.id;
    var element = document.getElementById('Analysis'+pk);
    var opt = {
        margin:       1,
        filename:     'myAnalysis.pdf',
        image:        { type: 'jpeg', quality: 0.99 },
        html2canvas:  { scale: 2 },
        jsPDF:        { unit: 'in', format: 'letter', orientation: 'portrait' }

    };
        
    // New Promise-based usage:
    html2pdf().set(opt).from(element).save();

    }