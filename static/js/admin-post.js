// Function to handle HTML file preview
function setupHTMLPreview() {
    const fileInput = document.getElementById('content');
    const previewContainer = document.getElementById('htmlPreview');
    const previewContent = document.getElementById('previewContent');

    if (fileInput && previewContainer && previewContent) {
        fileInput.addEventListener('change', function(event) {
            const file = event.target.files[0];
            if (file) {
                const reader = new FileReader();
                reader.onload = function(e) {
                    const htmlContent = e.target.result;
                    previewContent.innerHTML = htmlContent;
                    previewContainer.style.display = 'block';
                }
                reader.readAsText(file);
            }
        });
    }
}

// Function to handle preview in new window
function setupPreviewButton() {
    const fileInput = document.getElementById('content');
    const previewButton = document.getElementById('previewButton');

    if (previewButton) {
        previewButton.addEventListener('click', function(event) {
            event.preventDefault();
            
            const file = fileInput.files[0];
            if (!file) {
                alert('Please select an HTML file first');
                return;
            }
            
            // Create a FormData object to send the file
            const formData = new FormData();
            formData.append('content', file);

            // Send the file to the server to generate preview
            fetch('/admin/dashboard/generate-preview', {
                method: 'POST',
                body: formData
            })
            .then(response => response.json())
            .then(data => {
                if (data.success) {
                    // Open the preview in a new tab/window
                    window.open(data.preview_url, '_blank');
                } else {
                    alert('Error generating preview: ' + data.error);
                }
            })
            .catch(error => {
                console.error('Error:', error);
                alert('Error generating preview');
            });
        });
    }
}

// Call the function when the page loads
document.addEventListener('DOMContentLoaded', function() {
    setupHTMLPreview();
    setupPreviewButton();
});