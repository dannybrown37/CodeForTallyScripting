$(document).ready(function(){

  // jQuery to handle action when #card-resizer button is clicked
  $('#flip-button').click(function() {
    $("#flip-button .flip-card-inner").toggleClass("big-cards-active");
    $("#cards").toggleClass("big-cards").toggleClass("little-cards");
    $(".flip-card").toggleClass("big-card");
  });

  // jQuery to make grid sortable - https://jqueryui.com/sortable/#display-grid
  $(function () {
    $("#cards").sortable().disableSelection();
  });

});
