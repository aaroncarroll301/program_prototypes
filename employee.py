class Employee:
    def __init__(self, name, id, department, title):
        self.name = name
        self.id = id
        self.department = department
        self.title = title

    def get_name(self):
        return self.name
    
    def get_id(self):
        return self.id
    
    def get_department(self):
        return self.department
    
    def get_title(self):
        return self.title
    
def main():

    print("Name           ID Number   Department       Job Title")
    print('----------------------------------------------------------------')

    objSusan = Employee('Susan Meyers', '47899', 'Accounting', 'Vice President')
    name1 = objSusan.get_name()
    id1 = objSusan.get_id()
    dep1 = objSusan.get_department()
    title1 = objSusan.get_title()
    print(f"{name1}   {id1}       {dep1}       {title1}")

    objMark = Employee('Mark Jones', '39119', 'IT', 'Programmer')
    name2 = objMark.get_name()
    id2 = objMark.get_id()
    dep2 = objMark.get_department()
    title2 = objMark.get_title()
    print(f"{name2}     {id2}       {dep2}               {title2}")

    objJoy = Employee('Joy Rogers', '81774', 'Manufacturing', 'Engineer')
    name3 = objJoy.get_name()
    id3 = objJoy.get_id()
    dep3 = objJoy.get_department()
    title3 = objJoy.get_title()
    print(f"{name3}     {id3}       {dep3}    {title3}")
    print('----------------------------------------------------------------')

if __name__ == '__main__':
    main()

        