from flask import Flask, request, send_file, render_template_string
from flask_socketio import SocketIO, emit
import os
from main import process_pdf, process_multiple_pdfs
import config

app = Flask(__name__, template_folder='src/templates')
socketio = SocketIO(app)

print("Template folder path:", app.template_folder)
print("Current working directory:", os.getcwd())
print("Files in template directory:", os.listdir(app.template_folder))

@app.route('/')
def index():
    template = """
    <!DOCTYPE html>
    <html lang="en">
    <head>
        <meta charset="UTF-8">
        <meta name="viewport" content="width=device-width, initial-scale=1.0">
        <title>PDF Data Masking</title>
        <style>
            body {
                font-family: Arial, sans-serif;
                margin: 0;
                padding: 0;
                background-color: #f4f4f4;
            }

            h1 {
                background-color: #333;
                color: #fff;
                padding: 10px 0;
                text-align: center;
                margin: 0;
            }

            h2 {
                color: #333;
                margin: 20px 0 10px 0;
                padding: 0 10px;
            }

            form {
                margin: 0 auto;
                padding: 20px;
                max-width: 500px;
                background: #fff;
                border-radius: 8px;
                box-shadow: 0 2px 4px rgba(0, 0, 0, 0.1);
            }

            input[type="file"],
            input[type="submit"],
            select,
            textarea {
                display: block;
                width: 100%;
                padding: 10px;
                margin-bottom: 10px;
                border: 1px solid #ccc;
                border-radius: 4px;
            }

            input[type="submit"] {
                background-color: #333;
                color: #fff;
                border: none;
                cursor: pointer;
            }

            input[type="submit"]:hover {
                background-color: #555;
            }
        </style>
        </head>
        <body>
            <h1>PDF Data Masking</h1>
            <h2>Single File Upload</h2>
            <form action="/upload" method="post" enctype="multipart/form-data">
                <input type="file" name="file">
                <select name="language">
                    <option value="eng">English</option>
                    <option value="chi_sim">Simplified Chinese</option>
                    <option value="chi_tra">Traditional Chinese</option>
                    <option value="kor">Korean</option>
                </select>
                <textarea name="custom_sensitive_words" placeholder="Enter custom sensitive words/patterns, separated by commas..."></textarea>
                <input type="submit" value="Upload">
            </form>
            <h2>Multiple Files Upload</h2>
            <form action="/upload_multiple" method="post" enctype="multipart/form-data">
                <input type="file" name="files" multiple>
                <select name="language">
                    <option value="eng">English</option>
                    <option value="chi_sim">Simplified Chinese</option>
                    <option value="chi_tra">Traditional Chinese</option>
                    <option value="kor">Korean</option>
                </select>
                <textarea name="custom_sensitive_words" placeholder="Enter custom sensitive words/patterns, separated by commas..."></textarea>
                <input type="submit" value="Upload Multiple">
            </form>
            <h2>Progress</h2>
            <div id="progress"></div>
            <script src="https://cdnjs.cloudflare.com/ajax/libs/socket.io/4.1.3/socket.io.js"></script>
            <script>
                var socket = io();
                socket.on('progress', function(msg) {
                    document.getElementById('progress').innerHTML = msg.data;
                });
            </script>
        </body>
        </html>
        """
    return render_template_string(template)

@app.route('/upload', methods=['POST'])
def upload_file():
    if 'file' not in request.files:
        return "No file part"
    file = request.files['file']
    lang = request.form.get('language', 'eng')
    custom_sensitive_words = request.form.get('custom_sensitive_words', '')
    custom_sensitive_words = custom_sensitive_words.split(',') if custom_sensitive_words else None
    if file.filename == '':
        return "No selected file"
    if file:
        input_path = config.INPUT_PDF_PATH
        output_path = config.OUTPUT_PDF_PATH
        report_path = os.path.splitext(output_path)[0] + '_report.txt'

        # Ensure the input and output directories exist
        os.makedirs(os.path.dirname(input_path), exist_ok=True)
        os.makedirs(os.path.dirname(output_path), exist_ok=True)

        file.save(input_path)
        process_pdf(input_path, output_path, lang, custom_sensitive_words, report_path)

        if os.path.exists(output_path):
            return send_file(output_path, as_attachment=True)
        else:
            return "File not found", 404

@app.route('/upload_multiple', methods=['POST'])
def upload_multiple_files():
    if 'files' not in request.files:
        return "No file part"
    files = request.files.getlist('files')
    lang = request.form.get('language', 'eng')
    custom_sensitive_words = request.form.get('custom_sensitive_words', '')
    custom_sensitive_words = custom_sensitive_words.split(',') if custom_sensitive_words else None
    input_dir = 'data/input'
    output_dir = 'data/output'
    os.makedirs(input_dir, exist_ok=True)
    os.makedirs(output_dir, exist_ok=True)
    report_dir = 'reports'
    os.makedirs(report_dir, exist_ok=True)

    total_files = len(files)
    for idx, file in enumerate(files):
        if file.filename == '':
            return "No selected file"
        if file:
            file_path = os.path.join(input_dir, file.filename)
            file.save(file_path)
            if os.path.getsize(file_path) == 0:
                return f"Uploaded file {file.filename} is empty", 400
            socketio.emit('progress', {'data': f'Processing {idx + 1}/{total_files} files...'})

    process_multiple_pdfs(input_dir, output_dir, lang, custom_sensitive_words, report_dir)

    first_output_file = os.path.join(output_dir, files[0].filename)
    if os.path.exists(first_output_file):
        return send_file(first_output_file, as_attachment=True)
    else:
        return "File not found", 404

if __name__ == '__main__':
    socketio.run(app, debug=True)
