from flask import render_template, request, jsonify, abort
import services
import config

app = config.APP


@app.route('/', methods=["GET", "POST"])
def home():
   return render_template("<html><h1>Students</h1></html>")


@app.route('/addnewclass', methods=['POST'])
def add_class_record():
    param = request.get_json()
    if not param:
        abort(400, "failed to insert")
    else:
        res = services.add_class_record(param)
    return jsonify({'result': res})


@app.route('/getclassdata', methods=["GET"])
def get_class_record():
    res = services.get_class_record()
    return jsonify({'result':res})


@app.route('/updateclassdetails', methods=["PUT"])
def update_class():
    param = request.get_json()

    if not request.json:
        abort(400)
    if 'id' in param and not isinstance(param['id'], str):
        abort(400)
    if len(param) == 0:
        abort(404, "missing parameter")
    else:
        res = services.update_class_by_id(param)
    return jsonify({'result': res})


@app.route('/deleteclassrecord', methods=["DELETE"])
def delete_class():
    param = request.get_json()
    if len(param) == 0:
        abort(404, "Error, Not found")
    if 'id' in param and not isinstance(param['id'],str):
        abort(400)
    else:
        res = services.delete_class(param)
    return jsonify({'result': res})


@app.route('/getstudent', methods=["GET"])
def get_student():
    res = services.get_student()
    return jsonify({'result': res})


@app.route('/addstudent', methods=['POST'])
def add_student():
    param = request.get_json()
    if not param:
        abort(400, "failed to insert")
    else:

        res = services.add_student_record(param)
        if not res:
            abort(400, "failed to insert")
        else:
            services.update_classleader(res[2])
    return jsonify({'result':res})


@app.route('/updatestudent', methods=["PUT"])
def update_student():
    param = request.get_json()

    if not request.json:
        abort(400)
    if 'id' in param and not isinstance(param['id'], str):
        abort(400)
    if len(param) == 0:
        abort(404, "missing parameter")
    else:
        res = services.update_student_by_id(param)
    return jsonify({'result': res})


@app.route('/deletestudent', methods=["DELETE"])
def delete_student():
    param = request.get_json()
    if len(param) == 0:
        abort(404, "Error, Not found")
    if 'id' in param and not isinstance(param['id'], str):
        abort(400)
    else:
        res = services.delete_student(param)
    return jsonify({'result': res})


if __name__ == "__main__":
    app.run(debug=True)
