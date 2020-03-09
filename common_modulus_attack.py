import csv
import sys
sys.setrecursionlimit(1000000)

class CommonModulusAttack:
    '''
    c1-> ciphertext-1
    c2-> ciphertext-2
    e1-> exponent-1
    e2-> exponent-2
    n-> modulus
    '''
    def __init__(self,c1,c2,e1,e2,n):
        self.c1 = c1
        self.c2 = c2
        self.e1 = e1
        self.e2 = e2
        self.n = n

        #bezout's identity vars.
        self.x = 0 
        self.y = 0

    def modinv(self, a, b):
        """return x such that (x * a) % b == 1"""
        g, x, _ = self.euclideanAlgorithm(a, b)
        if g != 1:
            raise Exception('gcd(a, b) != 1')
        return x % b

    def euclideanAlgorithm(self,e1,e2):
        if (e1 == 0):
            return (e2, 0, 1)
        else:
            gcd, y, x = self.euclideanAlgorithm(e2 % e1, e1)
            return (gcd, x - (e2 // e1) * y, y)
        '''
        Extended Euclidean Algorithm : e1 * x + e2 * y = gcd(e1,e2) 
        since gcd(e1,e2) given as 1 we need to find e1 * x + e2 * y = 1 
        '''

    def attack(self, x,y):
        if(x < 0 and y > 0):
            return (pow(self.modinv(self.c1,self.n),-x,self.n) * pow(self.c2,y, self.n)) % self.n
        elif(x >0 and y <0):
            return (pow(self.c1,x,self.n) * pow(self.modinv(self.c2,self.n),-y, self.n)) % self.n

    def printAll(self):
        print("c1 : " + str(self.c1))
        print("c2 : " + str(self.c2))
        print("e1 : " + str(self.e1))
        print("e2 : " + str(self.e2))
        print("n : " + str(self.n))

if __name__ == "__main__":

    myArgs = dict()
    with open('crackme.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for r in csv_reader:
            myArgs[r[0]]= r[1]

    cma = CommonModulusAttack(int(myArgs["c1"],16),int(myArgs["c2"],16),int(myArgs["e1"],16),int(myArgs["e2"],16),int(myArgs["n"],16))
    gcd,x,y = cma.euclideanAlgorithm(cma.e1,cma.e2)
    hex_str = format(cma.attack(x,y),'x')
    bytes_obj = bytes.fromhex(hex_str)
    ascii_str = bytes_obj.decode("ASCII")

    print(ascii_str)