class Father:

    def __init__(self):
        print("Father Constructor")


class Mother:

    def __init__(self):
        print("Mother Constructor")


class Child(Father, Mother):

    def __init__(self):
        Father.__init__(self)
        Mother.__init__(self)
        print("Child Constructor")


c = Child()