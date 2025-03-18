class Animal:
    def __init__(self, args):
        self.name = args[0]        
        self.sound = args[1]
    
    def emit_sound(self):
        print(self.sound)