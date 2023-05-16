from flask import Blueprint, render_template, redirect, url_for

views = Blueprint(__name__,"views")

@views.route("/")
def home():
    return render_template("index.html")

@views.route("/aboutus")
def aboutus():
    return render_template("aboutus.html")

@views.route("/contactus")
def contactus():
    return render_template("contactus.html")

@views.route("/breakfast")
def breakfast():
    return render_template("breakfast.html")
@views.route("/rice")
def rice():
    return render_template("rice.html")
@views.route("/vegrecipes")
def veg():
    return render_template("vegrecipes.html")
@views.route("/nonvegrecipes")
def nonveg():
    return render_template("nonvegrecipes.html")

#redirections
@views.route("/go-to-bf")
def go_to_bf():
    return redirect(url_for("views.breakfast"))
@views.route("/go-to-rice")
def go_to_rice():
    return redirect(url_for("views.rice"))
@views.route("/go-to-veg")
def go_to_veg():
    return redirect(url_for("views.vegrecipes"))
@views.route("/go-to-nonveg")
def go_to_nonveg():
    return redirect(url_for("views.nonvegrecipes"))

@views.route("/go-to-aboutus")
def go_to_aboutus():
    return redirect(url_for("views.aboutus"))

@views.route("/go-to-contactus")
def go_to_contactus():
    return redirect(url_for("views.contactus"))

@views.route("/go-to-home")
def go_to_home():
    return redirect(url_for("views.home"))