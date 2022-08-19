$("form").submit(function(){
  $("#find_places").prop("disabled",true).text('Loading...')
  // $("#find_places").prepend("<span class="spinner-border spinner-border-sm d-none" role="status" aria-hidden="true"></span>");

  $("#first_p").delay(1000).slideDown('slow');
  $("#second_p").delay(2000).slideDown("slow");
  $("#third_p").delay(3000).slideDown("slow");
  $("#fourth_p").delay(4000).slideDown("slow");
  
});