class student:
    def _init_(self,name,rollno,branch):
        self.name = name
        self.rollno = rollno
        self.branch = branch

    def display(self):
        print(f"name: {self.name}, roll_no: {self.rollno}, branch: {self.branch}")

s1=student("Ram",101,"CS")
s2=student("Sarthak",102,"CS")
s3=student("Ram",103,"IT")

s1.display()
s2.display()
s3.display()