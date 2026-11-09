from flask import Flask, render_template

app = Flask(__name__)

PROFILE = {
    "name": "Rex",
    "full_name": "Balogun Al-ameen Olamide",
    "title": "Software Developer & Creative Video Editor",
    "location": "Nigeria",
    "tagline": "Edit. Create. Code.",
    "description": (
        "I build digital experiences, develop web applications "
        "and create visually engaging content."
    ),
    "socials": {
        "youtube": "https://www.youtube.com/@bigrex_11",
        "tiktok": "https://www.tiktok.com/@rex4u_",
        "whatsapp": "https://wa.me/2349034904834",
        "selar": "https://selar.com/m/rex4u",
    }
}

@app.route("/")
def home():
    return render_template("index.html", profile=PROFILE)

@app.route("/about")
def about():
    return render_template("index.html", profile=PROFILE)

@app.route("/projects")
def projects():
    return render_template("index.html", profile=PROFILE)

@app.route("/contact")
def contact():
    return render_template("index.html", profile=PROFILE)

if __name__ == "__main__":
    app.run(debug=True)
