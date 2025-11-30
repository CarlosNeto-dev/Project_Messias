from flask import Flask, render_template

app = Flask(__name__)

@app.route("/")
def index():
    return render_template("index.html")

@app.route("/gemini")
def gemini():
    return render_template("gemini.html")

@app.route("/certifications/aws")
def aws():
    return render_template("certifications/aws_cloud.html")

@app.route("/certifications/google_analytics")
def google():
    return render_template("certifications/google_analytics.html")

@app.route("/certifications/pcep")
def pcep():
    return render_template("certifications/pcep.html")

if __name__ == "__main__":
    app.run(debug=True)
