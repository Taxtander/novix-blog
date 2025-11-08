import React, { useState, useEffect } from 'react';

const ShowHTMLContent = ({ htmlContent, filePath }) => {
  const [content, setContent] = useState(htmlContent || '');
  const [loading, setLoading] = useState(false);

  // Function to load HTML content from a file
  const loadHTMLFromFile = async (file) => {
    setLoading(true);
    try {
      const text = await file.text();
      setContent(text);
    } catch (error) {
      console.error('Error reading file:', error);
      setContent('<p>Error loading HTML content</p>');
    } finally {
      setLoading(false);
    }
  };

  // Handle file input change
  const handleFileChange = (event) => {
    const file = event.target.files[0];
    if (file && file.type === 'text/html') {
      loadHTMLFromFile(file);
    } else {
      alert('Please select a valid HTML file');
    }
  };

  // If a file path is provided and content is empty, we might fetch from that path
  useEffect(() => {
    if (filePath && !htmlContent) {
      const fetchHTML = async () => {
        try {
          const response = await fetch(filePath);
          if (response.ok) {
            const htmlText = await response.text();
            setContent(htmlText);
          } else {
            console.error('Failed to fetch HTML content');
          }
        } catch (error) {
          console.error('Error fetching HTML content:', error);
        }
      };
      fetchHTML();
    }
  }, [filePath, htmlContent]);

  return (
    <div className="html-content-display">
      <div className="file-upload-section">
        <label htmlFor="htmlFileInput">Upload HTML File:</label>
        <input
          type="file"
          id="htmlFileInput"
          accept=".html,.htm"
          onChange={handleFileChange}
        />
      </div>

      {loading ? (
        <div className="loading">Loading HTML content...</div>
      ) : (
        <div className="html-display-area">
          <h3>HTML Content Preview:</h3>
          <div 
            className="html-content"
            dangerouslySetInnerHTML={{ __html: content }}
          />
        </div>
      )}
    </div>
  );
};

export default ShowHTMLContent;