from flask import Blueprint, render_template

routes = Blueprint("routes", __name__, static_folder="static",
                   template_folder="templates")


@routes.route('/')
def home():
    return "<h1> Hii!! my name is ali, i am trying to build my website kjshdqlkksdljwasl </h1>"
