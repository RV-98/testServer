from flask import Flask, request
import git
from logging.handlers import RotatingFileHandler
import logging
import time
import os

app = Flask(__name__)

handler = RotatingFileHandler(os.path.join(app.root_path, 'logs', 'error_log.log'), maxBytes=102400, backupCount=10)
logging_format = logging.Formatter(
    '%(asctime)s - %(levelname)s - %(filename)s - %(funcName)s - %(lineno)s - %(message)s')

handler.setFormatter(logging_format)
app.logger.addHandler(handler)



@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home_page():
    text= "Halloe Ralewrwerwerewph! Dit is versie 35!"
    return (text)

@app.route('/update_server', methods=['get'])
def webhook():
    if request.method == 'GET':
        repo = git.Repo('C:/Pythonscripts_Test/testServer')
        origin = repo.remotes.origin
        origin.pull()
        return 'Updated PythonAnywhere successfully', 200
    else:
        return 'Wrong event type', 400


if __name__ == '__main__':
    # app.run(debug=True)

    app.run(debug=True, host="172.22.38.4", port=5003)