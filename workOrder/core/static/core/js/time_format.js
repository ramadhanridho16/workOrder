// time_format.js
document.addEventListener('DOMContentLoaded', function() {
    var timeInputs = document.querySelectorAll('input[type="time"]');
    timeInputs.forEach(function(input) {
        input.addEventListener('input', function() {
            // Get the value entered by the user
            var enteredValue = this.value;

            // Convert the entered value to 24-hour format
            var timeArray = enteredValue.split(':');
            var hour = parseInt(timeArray[0], 10);
            var minute = parseInt(timeArray[1], 10);

            // Ensure the hour is in 24-hour format
            if (hour < 0 || hour > 23) {
                hour = 0;
            }

            // Ensure the minute is within the valid range
            if (minute < 0 || minute > 59) {
                minute = 0;
            }

            // Format the time with leading zeros if necessary
            var formattedTime = (hour < 10 ? '0' + hour : hour) + ':' + (minute < 10 ? '0' + minute : minute);

            // Update the input value with the formatted time
            this.value = formattedTime;
        });
    });
});
