import os
import persistence.csv_import_neo as csv_import_neo
from common.config import UPLOAD_DIR
from flask_restful import Resource
from flask import abort, request
from werkzeug.utils import secure_filename


class CSVImportAPI(Resource):
    """ CSVImportAPI """

    def post(self):
        if 'file' not in request.files:
            abort(400)
            # TODO: http://flask.pocoo.org/docs/0.12/patterns/apierrors/
        file = request.files['file']
        if file.filename == '':
            abort(400)
        if file and allowed_file(file.filename):
            filename = secure_filename(file.filename)
            file.save(os.path.join(UPLOAD_DIR, filename))
            try:
                csv_import_neo.import_csv(os.path.join(UPLOAD_DIR, filename))
                return {'Result': 'CSV populated BD succesfully.'}, 201
            except Exception as e:
                return {'Error': "Malformed or incorrect CSV format."}, 400


def allowed_file(filename):
    return '.' in filename and filename.rsplit('.', 1)[1].lower() == 'csv'
