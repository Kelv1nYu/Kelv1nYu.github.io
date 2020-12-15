$(document).ready(function (){
    $('#state_info').show()
    $('#time_info').hide()
    $('#d_type_info').hide()
    $('#i_type_info').hide()
    $('#aid_plan').hide()
})

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'State')
      {
        $("#state_info").fadeIn(1000);
      }
      else
      {
        $("#state_info").hide();
      }
    });
});

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'Time')
      {
        $("#time_info").fadeIn(1000);
      }
      else
      {
        $("#time_info").hide();
      }
    });
});

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'Declaration type')
      {
        $("#d_type_info").fadeIn(1000);
      }
      else
      {
        $("#d_type_info").hide();
      }
    });
});

$(document).ready(function(){
    $('#Dropdown').on('change', function() {
      if ( this.value == 'Incident type')
      {
        $("#i_type_info").fadeIn(1000);
      }
      else
      {
        $("#i_type_info").hide();
      }
    });
});

$(document).ready(function(){
  $('#Dropdown').on('change', function() {
    if ( this.value == 'Aid plan')
    {
      $("#aid_plan").fadeIn(1000);
    }
    else
    {
      $("#aid_plan").hide();
    }
  });
});