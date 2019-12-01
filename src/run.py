from flask import Flask, render_template, request
app = Flask(__name__)


@app.route("/")
def template_test():
    return render_template('layout.html', my_string="Wheeeee!", my_list=[0,1,2,3,4,5])

@app.route("/", methods=['POST'])
def post_song_name():
    song_name = request.form['song_name']
    return song_name

if __name__ == '__main__':
    app.run(debug=True)