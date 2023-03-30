class Andy:

    def AndysDing (self):
        andy1 = 1
        print (andy1)
        return self
    def AndysDing2 (self):
        andy2 = 2
        print (andy2)
        return self
    
andy = Andy()
#andy.AndysDing()
#andy.AndysDing2()

andy.AndysDing().AndysDing2()

andy.AndysDing()\
    .AndysDing2() #Line continueation
