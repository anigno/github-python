document.addEventListener('DOMContentLoaded', function () {
    // Fetch music folders from the server
    fetch('/get_folders')
        .then(response => response.json())
        .then(data => {
            const folderListDiv = document.getElementById('folder-list');
            // iterate folders to create buttons
            data.folders.forEach(folder => {
                const button = document.createElement('button');
                button.textContent = folder;
                button.addEventListener('click', function () {
                    const folderName = button.textContent;

                    // Send an AJAX request to your Flask route
                    fetch(`/select_folder/${folderName}`, {
                        method: 'POST',  // or 'GET' depending on your use case
                    })
                        .then(response => response.text())  // Parse the response as text
                        .then(selectedFolder => {
                            // Update the content of the selected-folder div
                            const selectedFolderDiv = document.getElementById('selected-folder');
                            selectedFolderDiv.textContent = `Selected Folder: ${selectedFolder}`;
                        })
                        .catch(error => {
                            console.error('Error:', error);
                        });
                });
                folderListDiv.appendChild(button);
            });
        })
        .catch(error => {
            console.error('Error fetching music folders:', error);
        });

    const volumeSlider = document.getElementById('volume-slider');
    const durationSlider = document.getElementById('duration-slider');

    // Function to handle volume change
    volumeSlider.addEventListener('input', function () {
        const volumeValue = volumeSlider.value;
        fetch('/update_volume', {
            method: 'POST',
            body: new URLSearchParams({'volume': volumeValue}),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
            .then(response => {
                // Handle the response from the server if needed
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });

    // Function to handle duration change
    durationSlider.addEventListener('input', function () {
        const durationValue = durationSlider.value;
        fetch('/update_duration', {
            method: 'POST',
            body: new URLSearchParams({'duration': durationValue}),
            headers: {
                'Content-Type': 'application/x-www-form-urlencoded',
            },
        })
            .then(response => {
                // Handle the response from the server if needed
            })
            .catch(error => {
                console.error('Error:', error);
            });
    });


    const volumeDisplay = document.getElementById('volume-display');
    const durationDisplay = document.getElementById('duration-display');

    // Function to update volume display
    volumeSlider.addEventListener('input', function () {
        const volumeValue = volumeSlider.value;
        volumeDisplay.textContent = `Volume: ${volumeValue}`;
        localStorage.setItem('volume', volumeValue); // Store volume value
        // Send volumeValue to Flask backend if needed
    });

    // Function to update duration display
    durationSlider.addEventListener('input', function () {
        const durationValue = durationSlider.value;
        durationDisplay.textContent = `Duration: ${durationValue}`;
        localStorage.setItem('duration', durationValue); // Store duration value
        // Send durationValue to Flask backend if needed
    });

    // Retrieve and set slider values on page load
    const storedVolume = localStorage.getItem('volume');
    if (storedVolume) {
        volumeSlider.value = storedVolume;
        volumeDisplay.textContent = `Volume: ${storedVolume}`;
    }

    const storedDuration = localStorage.getItem('duration');
    if (storedDuration) {
        durationSlider.value = storedDuration;
        durationDisplay.textContent = `Duration: ${storedDuration}`;
    }

});


