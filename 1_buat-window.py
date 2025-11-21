from core.base import Base

class Test(Base):
    def initialize(self):
        print("Inisialisasi window")

    
    def update(self):
        pass

Test().run()