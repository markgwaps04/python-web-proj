(function(d) {
const forms   = document.getElementsByTagName("form");
const label	  = document.querySelector( '.label-helper' );
const buttonUpload	  = document.querySelector( '.box__button' );
let files = null;

function allowDrop(ev) {
  ev.preventDefault();
}

function fileValidation(file) {
const _validFileExtensions = [".jpg", ".jpeg", ".bmp", ".gif", ".png"];
var file_name = file.name;
var Extension = file_name.substring(file_name.lastIndexOf('.') + 1).toLowerCase();
return Extension === "xls";
}

function uploadFile(file)
{
   const formData = new FormData();
   formData.append('file', file);

   const request = $.ajax({
        url: '/generate/',
        data: formData,
        dataType : "html",
        headers: {"X-CSRFToken": jQuery.cookie("csrftoken")},
        type: 'POST',
        contentType: false, // NEEDED, DON'T OMIT THIS (requires jQuery 1.6+)
        processData: false, // NEEDED, DON'T OMIT THIS
        // ... Other options like success and etc
    });

    request.then(function(res) {
        jQuery("#upload_review")
            .modal("show")
            .find(".modal-body").html(res)
    })

}

function showFiles(files) {
    console.log(label);
    label.textContent = files.length > 1 ? ( input.getAttribute( 'data-multiple-caption' ) || '' ).replace( '{count}', files.length ) : files[ 0 ].name;
}


Array.prototype.forEach.call( forms, function( form ) {
    form.addEventListener("dragover", allowDrop);
    form.addEventListener("drop", function(e) {
        e.preventDefault();
        droppedFiles = e.dataTransfer.files;
        files = droppedFiles;
        showFiles(droppedFiles)
    });
    form.addEventListener("submit",function(e) {

        e.preventDefault();
        if (!files || files.length <= 0)
        {
            alert("No file selected!");
            return;
        }

        file = files[0];
        if (!fileValidation(file))
        {
            return Swal.fire({
                icon: 'error',
                title: 'Cannot open this file.',
                text: 'The file format or file extension is not valid. Verify that the file ' +
                      'has not been corrupted and that the file extension matches the format of the file.',
            });
        }

        uploadFile(file);

    });
});

jQuery("#save_data").click(function() {

    const request = $.ajax({
        url: '/save/',
        dataType : "json",
        headers: {"X-CSRFToken": jQuery.cookie("csrftoken")},
        type: 'POST'
    });

    request.then(function() {
        alert('Successfully save!');
    });

    request.fail(function(e) {
        const error_details = JSON.parse(e.responseText);
        alert(error_details.status)
    })

});




})(jQuery)
