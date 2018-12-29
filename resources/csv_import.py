import os
from flask_restful import Resource
from flask import abort, request, redirect, url_for
from werkzeug.utils import secure_filename
from common.config import UPLOAD_DIR


class CSVImportAPI(Resource):
    """ CSVImportAPI skeleton """

    def post(self):
        if 'file' not in request.files:
            abort(400)
        file = request.files['file']
        if file.filename == '':
            abort(410)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            return redirect(url_for('uploaded_file', filename=filename))


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'
