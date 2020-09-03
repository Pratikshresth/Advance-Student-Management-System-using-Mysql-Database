class Student:
    def __init__(self,fname, lname, city, zipcode, state, gender, email, contact, dob, program,section,clgId):
        self.fname=fname
        self.lname=lname
        self.city=city
        self.zipcode=zipcode
        self.state=state
        self.gender=gender
        self.email=email
        self.contact=contact
        self.dob=dob
        self.program=program
        self.section=section
        self.clgID=clgId

    def get_fname(self):
        return self.fname

    def set_fname(self,fname):
        self.fname=fname
        return self.fname

    def get_lname(self):
        return self.lname

    def set_lname(self, lname):
        self.fname = lname
        return self.lname

    def get_city(self):
        return self.city

    def set_city(self, city):
        self.city = city
        return self.city

    def get_zipcode(self):
        return self.zipcode

    def set_zipcode(self, zipcode):
        self.zipcode = zipcode
        return self.zipcode

    def get_state(self):
        return self.state

    def set_state(self, state):
        self.state = state
        return self.state

    def get_gender(self):
        return self.gender

    def set_gender(self, gender):
        self.gender = gender
        return self.gender

    def get_email(self):
        return self.email

    def set_email(self, email):
        self.email = email
        return self.email

    def get_contact(self):
        return self.contact

    def set_contact(self, contact):
        self.contact = contact
        return self.contact

    def get_dob(self):
        return self.dob

    def set_dob(self, dob):
        self.dob = dob
        return self.dob

    def get_programs(self):
        return self.program

    def set_program(self, program):
        self.program = program
        return self.program

    def get_section(self):
        return self.section

    def set_section(self, section):
        self.section = section
        return self.section

    def get_clgID(self):
        return self.clgID

    def set_clgID(self, clgID):
        self.clgID = clgID
        return self.clgID








