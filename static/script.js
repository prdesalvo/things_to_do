$("form").submit(function(){
  
  $("#find_places").addClass('d-none');
  $("#spinner").removeClass("d-none");

  $("#first_p").delay(1000).slideDown('slow');
  $("#second_p").delay(2000).slideDown("slow");
  $("#third_p").delay(3000).slideDown("slow");
  $("#fourth_p").delay(4000).slideDown("slow");
  
});