# -*- coding: utf-8 -*-

import os
import pexpect
from base64 import b64encode
from uuid import uuid4
from flask import Flask, request, jsonify


app = Flask(__name__)
app.config['JSONIFY_PRETTYPRINT_REGULAR'] = False


idat_path = '/home/idauser/idapro-7.5/idat64'
script_path = '/share/data/script.py'


@app.errorhandler(Exception)
def on_error(exception):
    response = jsonify(error=exception)
    response.status_code = 500
    return response


@app.route('/execute_script', methods=['POST'])
def execute_script():
    data = request.form
    if 'filename' not in data or 'file' not in request.files:
        return jsonify(error="Missing parameter 'filename' or 'file'"), 422
    filename = data['filename']

    binary = request.files.get('file')
    saved_path = "/tmp/ida_" + uuid4().hex
    os.system("mkdir -p {0}".format(saved_path))

    fp = os.path.join(saved_path, filename)
    binary.save(fp)

    command = [idat_path, "-B", '-S{0}'.format(script_path), fp]
    result = b""
    try:
        timeout = None if 'timeout' not in data else int(data['timeout'])
        _, exit_code = pexpect.run(" ".join(command), timeout=timeout, withexitstatus=True)
        if exit_code == 0:
            with open(os.path.join(saved_path, 'result.json'), "rb") as f:
                result = f.read()
    except pexpect.TIMEOUT:
        return jsonify(error='request to IDA timed out'), 408
    finally:
        os.system("rm -rf {0}".format(saved_path))

    if exit_code != 0:
        return jsonify(error='IDA finish with status code %s' % exit_code), 500
    else:
        return jsonify(message='OK', data=b64encode(result).decode()), 200


if __name__ == '__main__':
    app.run(debug=False)
