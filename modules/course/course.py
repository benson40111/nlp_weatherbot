from modules.db.mongo import Course

class Search_Course():
    def __init__(self, department, category, grade, week, time):
        self.department = department
        self.category = category
        self.grade = grade
        self.week = week
        self.time = time

    def get_data(self):
        time_dict = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L']
        time_list = []
        search_dict = {}
        for x in self.time:
            if (x in time_dict):
                time_list.append(x)
        if (self.department):
            search_dict['classes'] = self.department
        if (self.category):
            search_dict['course_category'] = self.category
        if (self.grade):
            search_dict['grade'] = self.grade
        if (self.week):
            search_dict['week'] = self.week
        if (time_list):
            search_dict['time'] = {
                '$elemMatch': {
                    '$elemMatch': { '$in': time_list }
                }
            }
        search_result = Course.objects(__raw__=search_dict).all()
        return search_result
