class Insect:
    def __init__(self):
        print("This insect can: ")

class Bumblebee(Insect):
    def __init__(self):
        super().__init__()
        print("Bumblebee can:")

    def sting(self):
        print("sting.")

class Grasshopper(Insect):
    def __init__(self):
        super().__init__()
        print("Grasshopper can:")
    
    def jump(self):
        print("jump.")

