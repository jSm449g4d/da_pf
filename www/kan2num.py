import flask
from werkzeug.utils import secure_filename
def n2k_simo(input_kanzi=""):
    if input_kanzi=="壱":
        return 1
    if input_kanzi=="弐":
        return 2
    if input_kanzi=="参":
        return 3
    if input_kanzi=="四":
        return 4
    if input_kanzi=="五":
        return 5
    if input_kanzi=="六":
        return 6
    if input_kanzi=="七":
        return 7
    if input_kanzi=="八":
        return 8
    if input_kanzi=="九":
        return 9
    return 0
def k2n_naka(input_kanzi=""):
    return_number=0
    if len(input_kanzi.split("千"))==2:
        return_number+=1000*n2k_simo(input_kanzi.split("千")[0])
        input_kanzi=input_kanzi.split("千")[1]
    if len(input_kanzi.split("百"))==2:
        return_number+=100*n2k_simo(input_kanzi.split("百")[0])
        input_kanzi=input_kanzi.split("百")[1]
    if len(input_kanzi.split("拾"))==2:
        return_number+=10*n2k_simo(input_kanzi.split("拾")[0])
        input_kanzi=input_kanzi.split("拾")[1]
    return_number+=n2k_simo(input_kanzi)
    return return_number
def k2n(input_kanzi=""):
    return_number=0
    if input_kanzi=="零":
        return 0
    if len(input_kanzi.split("兆"))==2:
        return_number+=1000000000000
        input_kanzi=input_kanzi.split("兆")[1]
    if len(input_kanzi.split("億"))==2:
        return_number+=100000000
        input_kanzi=input_kanzi.split("億")[1]
    if len(input_kanzi.split("万"))==2:
        return_number+=10000*k2n_naka(input_kanzi.split("万")[0])
        input_kanzi=input_kanzi.split("万")[1]
    return_number+=k2n_naka(input_kanzi)
    return str(return_number)
def show(value):
    try:
        return k2n(value),200
    except:
        return "変換できません", 204
    return "OK", 200

if __name__ == "__main__":
    print("test")