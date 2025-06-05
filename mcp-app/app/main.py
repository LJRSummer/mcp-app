from flask import Flask, render_template, request, send_from_directory
import os
from werkzeug.utils import secure_filename
from utils.image_utils import group_similarity_score, allowed_file

app = Flask(__name__)
BASE_DIR = os.path.dirname(os.path.abspath(__file__))
UPLOAD_FOLDER = os.path.join(BASE_DIR, 'uploads')
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/', methods=['GET', 'POST'])
def index():
    avg_score = max_score = min_score = None
    img_files = []
    max_pair = (None, None)
    if request.method == 'POST':
        for f in os.listdir(UPLOAD_FOLDER):
            file_path = os.path.join(UPLOAD_FOLDER, f)
            if os.path.isfile(file_path) and allowed_file(f):
                os.remove(file_path)
        files = request.files.getlist('images')
        for file in files:
            if file and allowed_file(file.filename):
                filename = secure_filename(file.filename)
                file.save(os.path.join(app.config['UPLOAD_FOLDER'], filename))
        avg_score, max_score, min_score, max_pair = group_similarity_score(UPLOAD_FOLDER)
        img_files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
    else:
        img_files = [f for f in os.listdir(UPLOAD_FOLDER) if allowed_file(f)]
    return render_template('index.html',
                           avg_score=avg_score,
                           max_score=max_score,
                           min_score=min_score,
                           img_files=img_files,
                           max_pair=max_pair)

@app.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory(app.config['UPLOAD_FOLDER'], filename)

if __name__ == '__main__':
    # 平台一般要求监听 0.0.0.0 和 8080 端口
    app.run(host='0.0.0.0', port=8080)