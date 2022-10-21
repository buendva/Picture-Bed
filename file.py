from flask import Blueprint, request, render_template, send_from_directory
from werkzeug.utils import secure_filename
import uuid
import os
import stats_update
import json

bp = Blueprint('file', __name__)
UPLOAD_IMGS_FOLDER = 'static/upload/imgs'
UPLOAD_FILES_FOLDER = 'static/upload/files'
images_allowed = ['jpg', 'png', 'webp', 'gif']


@bp.route('/upload', methods=['GET', 'POST'])
def upload():
    if request.method == 'GET':
        return render_template('upload.html')
    else:
        f = request.files['file']
        secure_name = secure_filename(f.filename)
        ext = secure_name.split('.')[-1]
        if ext in images_allowed:
            filename = 'P' + str(uuid.uuid4()) + '.' + ext
            filepath = os.path.join(UPLOAD_IMGS_FOLDER, filename)
        else:
            filename = 'F' + str(uuid.uuid4()) + '.' + ext
            filepath = os.path.join(UPLOAD_FILES_FOLDER, filename)
        f.save(filepath)
        stats_update.update_stats()
        return '保存成功'


@bp.route('/download/<filename>')
def download(filename):
    if filename[0] == 'P':
        path = os.path.isfile(os.path.join(UPLOAD_IMGS_FOLDER, filename))
        dir_path = UPLOAD_IMGS_FOLDER
    else:
        path = os.path.isfile(os.path.join(UPLOAD_FILES_FOLDER, filename))
        dir_path = UPLOAD_FILES_FOLDER
    if path:
        return send_from_directory(dir_path, filename, as_attachment=True)
    else:
        return '下载错误'


@bp.route('/stats')
def stats():
    f = open('static/stats.txt', 'r', encoding='UTF-8')
    r = f.read()
    f.close()
    r = json.loads(r)
    return render_template('stats.html', r=r)
