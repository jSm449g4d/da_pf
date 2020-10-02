import flask
from werkzeug.utils import secure_filename
import json
import importlib
import datetime
from datetime import timedelta
def show(value):
    try:
        return value,200
    except:
        return "変換できません", 204
    return "OK", 200

if __name__ == "__main__":
    print("test")