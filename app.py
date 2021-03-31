from flask import Flask, request, render_template, redirect


app = Flask(__name__)


@app.route('/', methods=["GET", "POST"])
def hello_world():
    if request.method == "POST":
        print("FORM DATA RECEIVED")
        if "file" not in request.files:
            return redirect(request.url)
        file = request.files["file"]
        if file.filename == "":
            return redirect(request.url)
        # if file: code for audio to text
        #

    return render_template("input.html")


if __name__ == '__main__':
    app.run(debug=True, threaded=True)
