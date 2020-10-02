import flask
from werkzeug.utils import secure_filename
import json
import importlib
import datetime
from datetime import timedelta
def n2k_simo(input_number=0):
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
def n2k_naka(input_number=0):
    return_kanzi=""
    if input_number//1000>0:
        return_kanzi+=n2k_simo(input_number//1000)+"千"
        input_number%=1000
    if input_number//100>0:
        return_kanzi+=n2k_simo(input_number//100)+"百"
        input_number%=100
    if input_number//10>0:
        return_kanzi+=n2k_simo(input_number//10)+"捨"
        input_number%=10
    if input_number//1>0:
        return_kanzi+=n2k_simo(input_number//1)
    return return_kanzi
def n2k(input_number=0):
    return_kanzi=""
    if input_number==0:
        return "零"
    if input_number//1000000000000>0:
        return_kanzi+=n2k_naka(input_number//1000000000000)+"兆"
        input_number%=1000000000000
    if input_number//100000000>0:
        return_kanzi+=n2k_naka(input_number//100000000)+"億"
        input_number%=100000000
    if input_number//10000>0:
        return_kanzi+=n2k_naka(input_number//10000)+"万"
        input_number%=10000
    if input_number//1>0:
        return_kanzi+=n2k_naka(input_number//1)
    return return_kanzi
def show(value):
    try:
        return n2k(int(value)), 200
    except:
        return "変換できません", 204
    return "OK", 200

if __name__ == "__main__":
    print("test")