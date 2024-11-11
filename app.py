from flask import Flask, render_template, request

app = Flask(__name__)

@app.route("/", methods=["GET", "POST"])
def index():
    result = None
    if request.method == "POST":
        # Obtener los valores de la forma
        celsius = request.form.get("celsius")
        fahrenheit = request.form.get("fahrenheit")

        # Convertir según el campo proporcionado
        if celsius:
            result = (float(celsius) * 9/5) + 32  # Celsius a Fahrenheit
        elif fahrenheit:
            result = (float(fahrenheit) - 32) * 5/9  # Fahrenheit a Celsius

    return render_template("index.html", result=result)

if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=80)
