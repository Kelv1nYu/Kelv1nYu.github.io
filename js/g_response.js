$(document).ready(function (){
    $('#response_type').show()
    $('#response_speed').hide()
})

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'response_type')
      {
        $("#response_type").fadeIn(1000);
      }
      else
      {
        $("#response_type").hide();
      }
    });
});

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'response_speed')
      {
        $("#response_speed").fadeIn(1000);
      }
      else
      {
        $("#response_speed").hide();
      }
    });
});