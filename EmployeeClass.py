class employeeclass:
    def __init__(self, name, idnumber, department, jobtitle, monthlysalary):
        self._name=name
        self._idnumber=idnumber
        self._department=department
        self._jobtitle=jobtitle
        self._monthlysalary=monthlysalary

    def set_name(self, name):
        self._name = name
    
    def get_name(self):
        return self._name

    def set_idnumber(self,idnumber):
        self._idnumber = idnumber

    def get_idnumber(self):
        return self._idnumber

    def set_department(self, department):
        self._department=department

    def get_department(self):
        return self._department

    def set_jobtitle(self, jobtitle):
        self._jobtitle=jobtitle

    def get_jobtitle(self):
        return self._jobtitle

    def set_monthlysalary(self, monthlysalary):
        self._monthlysalary=monthlysalary

    def get_monthlysalary(self):
        return self._monthlysalary

#def set_manufact(self, manufact):
   #     self.__manufact = manufact
  # def get_manufact(self):
    #    return self.__manufact