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
  