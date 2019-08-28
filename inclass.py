class MyClass:

    # class variable
    listlength = 5

    # instance method
    def __init__(self, number):

        # instance attribute
        self.data = number

    # class method
    @classmethod
    def list_of_objects(cls):
        result = []
        for i in range(cls.listlength):
            newobj = cls(i)
            result.append(newobj)
        return result

result = MyClass.list_of_objects()
print(result)
print([r.data for r in result])