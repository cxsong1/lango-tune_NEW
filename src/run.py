from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('layout.html')

@app.route("/", methods=['POST'])
def post_song_name():
    song_name = request.form['song_name']
    return song_name

def post_language_select():
    language = request.forn['language']
    return language

if __name__ == '__main__':
    app.run(debug=True)