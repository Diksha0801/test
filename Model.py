from datetime import datetime
from config import DB
from sqlalchemy.dialects.postgresql import UUID


class Student(DB.Model):
    __tablename__ = "Student"
    student_id = DB.Column(UUID(as_uuid=True), unique=True, nullable=False, primary_key=True)
    student_name = DB.Column(DB.String)
    class_id = DB.Column(DB.ForeignKey('Class.class_id'),nullable=False)
    created_on = DB.Column(DB.DateTime)
    updated_on = DB.Column(DB.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, student_name, class_id, created_on):
            self.student_name = student_name
            self.class_id = class_id
            self.created_on = created_on


class Class(DB.Model):
    __tablename__ = 'Class'
    class_id = DB.Column(DB.Integer, primary_key=True)
    class_name = DB.Column(DB.String)
    class_leader = DB.Column(DB.Integer, DB.ForeignKey('Student.student_id'))
    created_on = DB.Column(DB.DateTime, default=datetime.utcnow)
    updated_on = DB.Column(DB.DateTime, default=datetime.utcnow, onupdate=datetime.utcnow)

    def __int__(self, name, class_leader, created_on):
            self.class_name =  name
            self.class_leader = class_leader
            self.created_on = created_on
