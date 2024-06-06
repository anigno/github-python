    console.log('Script loaded');
    $(document).ready(function() {
        // Button click handler
        $('#actionButton').click(function() {
            // Send a POST request to the Flask route '/button_click'
            $.post('/button_click', function(response) {
                // Handle the response if needed
                console.log('Button click response:', response);
            });
        });

        // Function to periodically update the scroll value
        function updateScrollValue() {
            $.get('/get_scroll_value', function(data) {
                $('#scrollBar').val(data);
                $('#scrollValue').text(data);
            });
        }

        // Function to periodically update the status text
        function updateStatusText() {
            $.get('/get_status_text', function(data) {
                $('#statusText').text(data);
            });
        }

        // Initial update of the scroll value and status text
        updateScrollValue();
        updateStatusText();

        // Scroll bar handler
        $('#scrollBar').on('input', function() {
            let scrollValue = $(this).val();
            $('#scrollValue').text(scrollValue); // Update displayed value
            $.post('/set_scroll_value', {scroll_val: scrollValue});
        });

        // Periodically update the scroll value (every 1 second)
        setInterval(updateScrollValue, 1000);

        // Periodically update the status text (every 1 second)
        setInterval(updateStatusText, 1000);
    });
