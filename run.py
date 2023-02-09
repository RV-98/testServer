from flask import Flask, request
import git

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home_page():
    text= "Dit is versie 2.5!"
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

    app.run(debug=True, host="172.22.38.4", port=5000)