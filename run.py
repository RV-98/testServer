from flask import Flask

app = Flask(__name__)


@app.route("/", methods=['GET', 'POST'])
@app.route('/home', methods=['GET', 'POST'])

def home_page():
    text= "Dit is versie 1!"
    return (text)



if __name__ == '__main__':
    # app.run(debug=True)

    app.run(debug=True, host="0.0.0.0", port=5000)