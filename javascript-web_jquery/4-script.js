// JavaScript script that toggles the class of the <header> element
// when the user clicks on the tag DIV#toggle_header:

$('DIV#toggle_header').on('click', function () {
  $('HEADER').toggleClass('red green');
});
