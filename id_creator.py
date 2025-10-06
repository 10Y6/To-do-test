class Hash():
    def __init__(self,string):
        self.string = string
        self.MOD = 1000000007
    
    def string_to_hash(self):
        prime_2 = 10**9+9
        string_to_int = [ord(i) for i in self.string]
        acumulator = 0
        for ascii in string_to_int:
            acumulator += ascii*prime_2
            pow(acumulator,1,self.MOD)
        
        return '#' + str(acumulator)
