from flask import Flask, render_template

# testing a Blueprint
from routes.routes import routes

app = Flask(__name__)

app.register_blueprint(routes, url_prefix="/")


# Create Custom error pages

# invalid URl
@app.errorhandler(404)
def page_not_found(e):
    return render_template("404.html",), 404

# Internal Server Error
@app.errorhandler(500)
def page_not_found(e):
    return render_template("500.html",), 500


if __name__ == '__main__':
    app.run(debug=True)
