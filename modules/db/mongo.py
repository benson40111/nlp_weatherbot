from mongoengine import Document, IntField,ListField,StringField, connect
connect('course')

class Course(Document):
    course_id = StringField()
    name = StringField()
    course_category = StringField()
    teacher = ListField(StringField())
    classes = StringField()
    grade = StringField()
    week = ListField(StringField())
    time = ListField(ListField())
    classroom = ListField(StringField())
