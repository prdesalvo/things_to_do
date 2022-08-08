$("button").click(function(){
  // $("#spinner").removeClass('d-none');
  $("#find_places").addClass('d-none');
  $("#spinner").removeClass("d-none");

  setTimeout(function() {
    $("#first_p").slideDown('slow');
  }, 1000)

  setTimeout(function() {
    $("#second_p").slideDown("slow");
  }, 2000)

  setTimeout(function() {
    $("#third_p").slideDown("slow");
  }, 3000)

  setTimeout(function() {
    $("#fourth_p").slideDown("slow");
  }, 4000)
  
});

$('.nav-link').click(function(){
  $(".active").removeClass('active')
  // $(this).addClass('active')
});