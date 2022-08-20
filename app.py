class student:
    def __init__(self,name,age,mentor):
        self.name=name
        self.age=age
        self.mentor=mentor
class mentor:
    def __init__(self,name,salary):
        self.name=name
        self.salary=salary
ahmad=mentor("ahmad",3000)
s=student("saleh",27,ahmad)

