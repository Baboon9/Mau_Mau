import View.view 

class Controller:
    def __init__(self):
        pass

    def update(self, device):
        if type(device) == View.view.Console:
            return str(input())
