import csv

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

    def euclideanAlgorithm(self,e1,e2):
        '''
        Extended Euclidean Algorithm : e1 * x + e2 * y = gcd(e1,e2) 
        since gcd(e1,e2) given as 1 we need to find e1 * x + e2 * y = 1 
        '''


if __name__ == "__main__":

    myArgs = dict()
    with open('crackme.csv') as csv_file:
        csv_reader = csv.reader(csv_file,delimiter=',')
        for r in csv_reader:
            myArgs[r[0]]= r[1]

    cma = CommonModulusAttack(myArgs["c1"],myArgs["c2"],myArgs["e1"],myArgs["e2"],myArgs["n"])
    #!!!!!!!!!!!!! convert c1,c2,e1,e2,n to HEX !!! currrently these are string
