import flask
from werkzeug.utils import secure_filename
import json
import importlib
from newsapi import NewsApiClient
import datetime
from datetime import timedelta
def n2k_simo(input_number):
    if input_number==1:
        return "壱"
    if input_number==2:
        return "弐"
    if input_number==3:
        return "参"
    if input_number==4:
        return "四"
    if input_number==5:
        return "五"
    if input_number==6:
        return "六"
    if input_number==7:
        return "七"
    if input_number==8:
        return "八"
    if input_number==9:
        return "九"
    return "零"
def n2k(input_number):
    input_number=int(input_number)
    return_kanzi=""
    if input_number//1000000000000>0:
        return_kanzi+=n2k_simo(input_number//1000000000000)+"兆"
    if input_number//100000000>0:
        return_kanzi+=n2k_simo(input_number//100000000)+"億"
    if input_number//10000>0:
        return_kanzi+=n2k_simo(input_number//10000)+"万"
    return return_kanzi
def show(value):
    try:
        if value.split("/")[0]=="number2kanji":
            return n2k(value.split("/")[1]), 200
        if value.split("/")[0]=="kanji2number":
            return value.split("/")[1], 200
    except:
        return "変換できません", 204
    return "OK", 200

if __name__ == "__main__":
    print("test")