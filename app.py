from flask import Flask, render_template, request
from diet_classifiers import classify_recipe

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        raw_ingredients = request.form["ingredients"]
        ingredients = [i.strip() for i in raw_ingredients.split(",")]
        result = classify_recipe(ingredients)
    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True)
