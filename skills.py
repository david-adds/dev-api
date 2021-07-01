from flask_restful import Resource


skills_list = ['Python', 
               'C#', 
               'PHP', 
               'Django',
               'Java', 
               'Flask', 
               'C++',
               'PostgreSQL'
               ]

class Skills(Resource):
    def get(self):
        return skills_list
        
        