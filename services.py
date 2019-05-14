import uuid
from datetime import datetime
from Model import Student, Class
import config

"""This script prompts a to preform crud operation on student 
and class"""

###########defining method for class table#################

db = config.DbSession


def get_class_record():
    session = db.session()
    column_list = ['class_name', 'class_leader', 'created_on', 'update_on']
    res = session.query(Class).all()
    out_dikt = {}

    for db_col in res:
        class_id = db_col.class_id
        class_name = str(db_col.class_name)
        class_leader = str(db_col.class_leader)
        created_on = str(db_col.created_on)
        update_on = str(db_col.updated_on)

        out_dikt[str(class_id)] = dict(zip(column_list, [class_name, class_leader, created_on, update_on]))
    return (out_dikt)


def add_class_record(params):
    session = db.session()
    name = params.get('name', '')
    class_id = uuid.uuid1()
    class_table = Class(class_id=class_id, class_name=name, created_on=datetime.now())
    session.add(class_table)
    session.commit()

    return 'update successful', 201


def update_class_by_id(param):
    session = db.session()

    class_id = param.get('class_id', '')
    name = param.get('class_name', '')
    leader = param.get('class_leader', '')

    updat_dict = {}

    class_table = session.query(Class).filter(Class.class_id == class_id)

    if name != '':
        updat_dict[Class.class_name] = name
    elif leader != '':
        updat_dict[Class.class_leader] = leader
    class_table.update(updat_dict)
    session.commit()
    return 'update successful', 201


def delete_class(param):
    session = db.session()
    class_id = param.get('class_id', '')
    print(param)
    session.query(Class).filter(Class.class_id == class_id).delete()
    session.commit()
    return {'result': True}, 201


def update_classleader(param):
    session = db.session()
    student_id = param['s_id']
    class_id = param['c_id']

    class_data = session.query(Class.class_leader).filter(Class.class_id == class_id)
    update_dict = {}
    for data in class_data:
        if data.class_leader is None:
            update_dict[Class.class_leader] = student_id

    class_data.update(update_dict)
    session.commit()

    return 'update completed !!'


###########defining method for student table#################


def add_student_record(params):
    session = db.session()
    student_id = uuid.uuid1()

    name = params.get('name', '')
    class_id = params.get('class_id', '')

    student = Student(student_id=student_id, student_name=name, class_id=class_id, created_on=datetime.now())

    session.add(student)
    session.commit()

    return 'update successful', 201, {'c_id':class_id, 's_id':student_id}


def get_student():
    session = db.session()
    column_list = ['student_name', 'class_id', 'created_on', 'update_on']
    res = session.query(Student).all()
    out_dikt = {}
    for db_col in res:
        student_id = db_col.student_id
        student_name = str(db_col.student_name)
        class_id = str(db_col.class_id)
        created_on = str(db_col.created_on)
        update_on = str(db_col.updated_on)
        out_dikt[str(student_id)] = dict(zip(column_list, [student_name, class_id, created_on, update_on]))

    return out_dikt


def update_student_by_id(param):
    session = db.session()
    student_id = param.get('student_id', '')
    name = param.get('student_name', '')
    class_id = param.get('class_id', '')

    update_dict = {}

    student = session.query(Student).filter(Student.student_id == student_id)

    if name != '':

        update_dict[Student.student_name] = name
    elif class_id != '':
        update_dict[Student.class_id] = class_id

    student.update(update_dict)
    student.student_name = name
    session.commit()

    return 'update successful', 201


def delete_student(param):
    session = db.session()
    student_id = param.get('student_id')
    session.query(Student).filter(Student.student_id == student_id).delete()
    session.commit()

    return {'result': True}, 201


