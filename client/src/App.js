// App.js
import React, { useState } from 'react';
import axios from 'axios';

function App() {
    const [file, setFile] = useState(null);
    const [response, setResponse] = useState(null);
    const [error, setError] = useState(null);

    const handleFileChange = (e) => {
        setFile(e.target.files[0]);
        setResponse(null);
        setError(null);
    };

    const handleSubmit = async (e) => {
        e.preventDefault();
        if (!file) return;

        const formData = new FormData();
        formData.append("file", file);

        try {
            const res = await axios.post("http://127.0.0.1:5000/upload", formData, {
                headers: {
                    "Content-Type": "multipart/form-data"
                }
            });
            setResponse(res.data);
        } catch (err) {
            setError("An error occurred while processing the document.");
        }
    };

    return (
        <div className="App">
            <h1>Document Data Extraction</h1>
            <form onSubmit={handleSubmit}>
                <input type="file" onChange={handleFileChange} />
                <button type="submit">Upload Document</button>
            </form>

            {response && (
                <div>
                    <h3>Extracted Data:</h3>
                    <p><strong>Name:</strong> {response.name}</p>
                    <p><strong>Document Number:</strong> {response.document_number}</p>
                    <p><strong>Expiration Date:</strong> {response.expiration_date}</p>
                    {response.warning && <p><strong>Warning:</strong> {response.warning}</p>}
                </div>
            )}

            {error && <p>{error}</p>}
        </div>
    );
}

export default App;
