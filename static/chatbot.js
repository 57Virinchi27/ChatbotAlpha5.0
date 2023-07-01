$(document).ready(function() {
    $("#send-btn").click(function() {
        var userInput = $("#user-input").val();
        if (userInput !== "") {
            displayMessage("You: " + userInput);
            $("#user-input").val("");

            $.ajax({
                type: "POST",
                url: "/get_response",
                data: { user_input: userInput },
                success: function(response) {
                    displayMessage("Bot: " + response);
                }
            });
        }
    });

    function displayMessage(message) {
        $("#messages").append("<p>" + message + "</p>");
    }
});

