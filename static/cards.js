$(document).ready(function(){

  // jQuery to handle action with #card-resizer button is clicked
  $('#flip-button').click(function() {
    $("#flip-button .flip-card-inner").toggleClass("big-cards-active");
    $("#cards").toggleClass("big-cards");
    $("#cards").toggleClass("little-cards");
    $(".flip-card").toggleClass("big-card");
  });

});
