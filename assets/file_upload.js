(function(d) {
const forms   = document.getElementsByTagName("form");
const label	  = document.querySelector( '.label-helper' );

function allowDrop(ev) {
  ev.preventDefault();
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
        showFiles(droppedFiles)
    });
})

})(jQuery)
