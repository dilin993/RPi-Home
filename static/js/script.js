function updateTemperature() {
    $.ajax({
      url: '/temperature',
      success: function(data) {
        console.log(data);
        document.getElementById("temperature_value").innerHTML = data.temperature;
      },
      complete: function() {
        // schedule the next request *only* when the current one is complete:
        setTimeout(updateTemperature, 300000);
      }
    });
  }

  updateTemperature();
  
  function switchx(sw_id)  {
    console.log('clicked');
    $.ajax({
      url: '/switch/' + sw_id,
      type: 'PUT',
      success: function(data) {
        console.log(data);
        if(data==0) {
        document.getElementById("switch" + sw_id + "_text").innerHTML = "Turn on";
        } else {
        document.getElementById("switch" + sw_id + "_text").innerHTML = "Turn off";
        }
      }});
  }
  
  function updatePresence() {
    $.ajax({
      url: '/presence',
      success: function(data) {
        console.log(data);
        if(data.presence==0) {
        document.getElementById("presence_value").innerHTML = "off";
        } else {
        document.getElementById("presence_value").innerHTML = "on";
        }
      },
      complete: function() {
        // schedule the next request *only* when the current one is complete:
        setTimeout(updatePresence, 3000);
      }
    });
  }
  
  updatePresence();
  
