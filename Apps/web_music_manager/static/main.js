document.addEventListener('DOMContentLoaded', function () {
    // Fetch music folders from the server
    fetch('/get_folders').then(response => response.json().then(response_json => {
        const folder_list_dev = document.getElementById('folders_list_dev');
        response_json.folders.forEach(folder => {
            const button = document.createElement('button');
            button.textContent = folder;
            folder_list_dev.append(button);
            button.addEventListener('click', function () {
                const folderName = button.textContent;
                const selected_folder = document.getElementById('selected-folder');
                selected_folder.textContent = folderName;
                fetch(`/select_folder/${folderName}`, {method: 'POST',})
            });
        });
    }));
});

function get_data(key) {
    fetch(`/get_data/` + key, {method: 'GET'})
        .then(response => response.json())
        .then(response_json => {
            const message2 = document.getElementById('message02');
            message2.textContent = response_json[key];
        });
}

function store_data(key, value) {
    const postData = {
        key: key,
        value: value,
    };
    const requestOptions = {
        method: 'POST',
        headers: {
            'Content-Type': 'application/json',
        },
        body: JSON.stringify(postData), // Convert the data to JSON format
    };
    fetch(`/store_data`, requestOptions);
}

document.addEventListener('DOMContentLoaded', function () {
    // Fetch music folders from the server
    fetch('/get_folders');
    const folder_list_dev = document.getElementById('message01');
    message01.textContent = 'message number 1';
});

