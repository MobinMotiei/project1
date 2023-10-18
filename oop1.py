class human:
    #تابع پایینی یعنی شی ای دارم که اسم و غیره دارم
    def __init__(self,name,lname,age):
        #سلف یعنی اش مثلا سلف دات ایج یعنی سنش
        self.name=name
        self.lname=lname
        self.age=age
    def fun(self):
        return f"{self.name} WELCOME!"
print("888888888888888888888888")


ali=human("ali","mousavi",27)
print(ali.fun())
