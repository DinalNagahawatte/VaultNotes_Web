function deleteMyNote(noteId) {
    // Show a confirmation dialog box to the user.
    // The confirm() method returns true if the user clicks "OK", and false if they click "Cancel".
    if (confirm("Are you sure you want to delete this note? This action cannot be undone.")) {
        
        // If the user confirms, proceed with the deletion request
        fetch('/delete-note', {
            method: 'POST',
            body: JSON.stringify({ noteId: noteId }),
            headers: {
                'Content-Type': 'application/json' // Important: specify the content type
            }
        })
        .then(response => {
            // Check if the response is successful (status 200)
            if (response.ok) {
                // Assuming successful deletion, reload the page or remove the note element from the DOM
                window.location.reload(); 
            } else {
                // Handle errors, e.g., show an alert
                alert("An error occurred while trying to delete the note. Please try again.");
            }
        })
        .catch(error => {
            console.error('Fetch error:', error);
            alert("Network error. Could not connect to the server.");
        });

    } else {
        // If the user cancels the confirmation, do nothing.
        console.log("Note deletion cancelled by user.");
    }
}
