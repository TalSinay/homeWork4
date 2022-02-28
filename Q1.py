rates ={('dollar','nis'): 3.82,('euro','nis'): 4.07,('nis','dollar'):1/3.82,('nis','euro'):1/4.07,('dollar','euro'):0.88}

class Euro:
    '''
    Representation of the euro currency
    '''
    def __init__(self,x):
        '''

        :param x:The value of the desired currency
        '''
        self.__value=float (x)
        self.shekel=4.07
    def __repr__(self):
        '''

        :return:Representation of the department
        '''
        return f'Euro({self.__value})'

    def __str__(self):
        '''

        :return:Currency representation
        '''
        return f'{str(self.__value)}€'
    def amount(self):
        '''

        :return:The value of the currency in shekels
        '''
        return rates[('euro','nis')] *self.__value

    def __add__(self, other):
        '''

        :param other:the other coin
        :return:Connecting the coins in Shekel
        '''
        return self.amount() + other.amount()

class Dollar:
    '''
    Representation of the dollar currency
    '''
    def __init__(self,x):
        '''

        :param x:The value of the desired currency
        '''
        self.__value=float (x)
        self.shekel = 3.82
    def __repr__(self):
        '''

        :return:Representation of the department
        '''
        return f'Dollar({self.__value})'

    def __str__(self):
        '''

        :return:Currency representation
        '''
        return f'{str(self.__value)}$'
    def amount(self):
        '''

        :return:The value of the currency in shekels
        '''
        return rates[('dollar','nis')] *self.__value
    def __add__(self, other):
        '''

        :param other:the other coin
        :return:Connecting the coins in Shekel
        '''
        return self.amount() + other.amount()


class Shekel:
    '''
    Representation of the shekel currency
    '''
    def __init__(self,x):
        '''

        :param x:The value of the desired currency
        '''
        self.__value=float (x)
        self.shekel = 1
    def __repr__(self):
        '''

        :return:Representation of the department
        '''
        return f'Shekel({self.__value})'

    def __str__(self):
        '''

        :return:Currency representation
        '''
        return f'{str(self.__value)}nis'
    def amount(self):
        '''

        :return:The value of the currency in shekels
        '''
        return self.__value

    def __add__(self, other):
        '''

        :param other:the other coin
        :return:Connecting the coins in Shekel
        '''
        return self.amount() + other.amount()


def add(x,y):
    '''

    :param x:coin a
    :param y:coin b
    :return:Connecting the coins
    '''
    return x+y
def apply(op,coinA,coinB):
    '''
    Receives an action name and a pair of coins and performs the action between them and returns in the representation of the first coin
    :param op:The action
    :param coinA:first coin
    :param coinB:second coin
    :return:the result in the first currency representation
    '''
    if op is 'add':
        if type(coinA) is Shekel:
            a = coinA + coinB
            z=Shekel(a)
            return z
        elif type(coinA) is Euro and type(coinB) is Dollar:
            return Euro((coinA + coinB)*rates[('nis','euro')])

        elif type(coinA) is Dollar and type(coinB) is Euro:
            return Dollar((coinA + coinB)*rates[(('nis','dollar'))])
        elif type(coinA) is Euro:
            return Euro((coinA + coinB)*rates[(('nis','euro'))])
        elif type(coinA) is Dollar:
            return Dollar((coinA+coinB)*rates[(('nis','dollar'))])


    elif op is 'sub':
        if type(coinA) is Shekel:
            a=coinA.amount()-coinB.amount()
            return Shekel(a)
        elif type(coinA) is Euro and type(coinB) is Dollar:
            return Euro((coinA.amount()- coinB.amount()) * rates[('nis', 'euro')])
        elif type(coinA) is Dollar and type(coinB) is Euro:
            return Dollar((coinA.amount()-coinB.amount()) * rates[(('nis', 'dollar'))])
        elif type(coinA) is Euro:
            return Euro((coinA.amount()-coinB.amount()) * rates[(('nis', 'euro'))])
        elif type(coinA) is Dollar:
            return Dollar((coinA.amount()-coinB.amount()) * rates[(('nis', 'dollar'))])

def dollar_to_shekel(x):
    '''

    :param x:Object Dollar
    :return:A currency represented by a Shekel
    '''
    return Shekel(x.amount())
def euro_to_shekel(x):
    '''

    :param x:Object Euro
    :return:A currency represented by a Shekel
    '''
    return Shekel(x.amount())
def euro_to_dollar(x):
    '''

    :param x:Object Euro
    :return:A currency represented by a Dollar
    '''
    return Dollar(x.amount()*rates[('nis','dollar')])
def shekel_to_dollar(x):
    '''

    :param x:Object Shekel
    :return:A currency represented by a Dollar
    '''
    return Dollar(x.amount()*rates[('nis','dollar')])
def shekel_to_euro(x):
    '''

    :param x:Object Shekel
    :return:A currency represented by a Euro
    '''
    return Euro(x.amount() * rates[('nis','euro')])
def dollar_to_euro(x):
    '''

    :param x:Object Dollar
    :return:A currency represented by a Euro
    '''
    return Euro(x.amount() * rates[('nis','euro')])
def shekel(x):
    '''

    :param x:Object Shekel
    :return:A currency represented by a Shekel
    '''
    return Shekel(x.amount())

coercions={('dollar','nis'):dollar_to_shekel,('euro','nis'):euro_to_shekel,('euro','dollar'):euro_to_dollar,('dollar','euro'):dollar_to_euro,('nis','dollar'):shekel_to_dollar,('nis','euro'):shekel_to_euro}
type_tag_tags ={Euro:'euro',Dollar:'dollar',Shekel:'nis'}

def type_tag(x):
    '''

    :param x:a coin
    :return:String of currency representation
    '''
    return type_tag_tags[type(x)]

def  coerce_apply(op,coinA,coinB):
    '''
    Receives an action and a pair of coins converts them to the same type and performs the action between the pair of coins and returns in a shekel representation
    :param op:the action
    :param coinA:first coin
    :param coinB:second coin
    :return: Returns the operation in NIS representation
    '''
    tx,ty=type_tag(coinA),type_tag(coinB)
    if tx is not ty:
        if op is 'add':
            return Shekel(coinA+coercions[tx,ty](coinB))
        elif op is 'sub':
            return Shekel(coinA.amount()-coercions[tx,ty](coinB).amount())



s = Shekel(50)
d = Dollar(20)
e = Euro(20)
p=coercions[('dollar','nis')](Dollar(50))
print(repr(p))
print(d+s)
k=coerce_apply('sub', Dollar(50), Euro(20))
print(repr(k), '2')
h=coerce_apply('add', d,e)
print(repr(h),'3')
j=coerce_apply('add',s,d)
print(repr(j),'4')





