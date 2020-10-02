# Standard
import os
import sys
import importlib
import flask


# Flask_Startup
sys.path.append(os.path.dirname(os.path.abspath(__file__)))
os.chdir(os.path.dirname(os.path.join("./", __file__)))
app = flask.Flask(
    __name__, template_folder="./templates/", static_folder='./html/static/')
app.config['MAX_CONTENT_LENGTH'] = 10000000


@app.route("/", methods=["GET", "POST"])
def indexpage_show():
    try:
        return flask.render_template_string(
            "<a href='/v1/number2kanji/10000'>/v1/number2kanji/数字</a></br>"+
            "<a href='/v1/kanji2number/壱万'>/v1/kanji2number/漢字</a>")
    except Exception as e:
        return flask.render_template("error.html", STATUS_ERROR_TEXT=str(e)), 500

@app.route("/v1/number2kanji/<path:value>", methods=["GET", "POST"])
def num2kan_show(value):
    try:
        return importlib.import_module("num2kan").show(value)
    except Exception as e:
        return flask.render_template("error.html", STATUS_ERROR_TEXT=str(e)), 500

@app.route("/v1/kanji2number/<path:value>", methods=["GET", "POST"])
def kan2num_show(value):
    try:
        return importlib.import_module("kan2num").show(value)
    except Exception as e:
        return flask.render_template("error.html", STATUS_ERROR_TEXT=str(e)), 500


application = app

if __name__ == "__main__":
    app.run()
