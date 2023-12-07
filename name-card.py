from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def root():
    return render_template("index.html")

if __name__ == "__main__":
    #Run the app in debug mode and auto-reload
    app.run(debug=True)
