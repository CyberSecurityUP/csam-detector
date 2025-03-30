from flask import Blueprint, render_template, request, redirect, url_for, flash
import os
from werkzeug.utils import secure_filename
from app.hashing import generate_hash, compare_with_database
from app.ai_model import classify_image
from app.database import init_db, save_log
from flask import send_from_directory



main_routes = Blueprint('main', __name__)
UPLOAD_FOLDER = 'uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)
ALLOWED_EXTENSIONS = {'png', 'jpg', 'jpeg'}

# cria pasta se não existir
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() in ALLOWED_EXTENSIONS

@main_routes.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        if 'image' not in request.files:
            flash('No file part')
            return redirect(request.url)
        file = request.files['image']
        if file.filename == '':
            flash('No selected file')
            return redirect(request.url)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            filepath = os.path.join(UPLOAD_FOLDER, filename)
            file.save(filepath)
            return redirect(url_for('main.result', filename=filename))
        else:
            flash('Invalid file type')
    return render_template('index.html')
init_db()

@main_routes.route('/uploads/<filename>')
def uploaded_file(filename):
    return send_from_directory('uploads', filename)

@main_routes.route('/result/<filename>')
def result(filename):
    filepath = os.path.join(UPLOAD_FOLDER, filename)
    label, confidence = classify_image(filepath)
    hash_val = generate_hash(filepath)
    is_match, match_id = compare_with_database(hash_val)
    save_log(filename, label, confidence, hash_val, is_match)
    
    return render_template('result.html', 
                           filename=filename,
                           label=label,
                           confidence=confidence,
                           hash_val=hash_val,
                           is_match=is_match,
                           match_id=match_id)