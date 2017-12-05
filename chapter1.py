'''
# 1.1 python风格的纸牌
import collections
from random import choice   # 内置的随机选元素模块

Card = collections.namedtuple('Card', ['rank', 'suit'])  # 一个元组(点数，花色)

class FrenchDeck:
    ranks = [str(n) for n in range(2,11) ] + list('JQKA')   # list('123')结果就是['1','2','3'],本质上为2个list相加
    suits = 'spades diamonds clubs hearts'.split()   # 若split('s') 结果 ['', 'pade', ' diamond', ' club', ' heart', '']
    # 翻译，红桃，红方，黑方，黑花
    def __init__(self):    # __init__ 用法值得关注,类实例的值就是cardss
        self._cards = [Card(rank,suit) for suit in self.suits
                                for rank in self.ranks ]

    def __len__(self):
        return len(self._cards)

    def __getitem__(self, position):
        return self._cards[position]

suit_values = dict(spades=3, hearts=2,diamonds=1,clubs=0)
def spades_high( card):
    rank_value = FrenchDeck.ranks.index(card.rank)
    return rank_value * len(suit_values) + suit_values[card.suit]


deck = FrenchDeck()
print(  len(deck)  )  # 结果52；上方的self._cards在for in 中选，4*（9+4）=52种组合

print(  deck.__getitem__(0)  )   # 结果：Card(rank='2', suit='spades')
print( deck[0] )    # 结果：同上，红桃2是第一张牌
print(  choice(deck)  )   # 表示随机选牌，如 Card(rank='3', suit='clubs')

# 查看一副牌最上面的3张
print( deck[:3] )
# >>>[Card(rank='2', suit='spades'), Card(rank='3', suit='spades'), Card(rank='4', suit='spades')]
# 从第12张牌开始拿，后面每隔13抽一张,开头有个0，实际就是隔13抽一张,结果抽了4个A
print(  deck[12::13]  )   # <class '__main__.FrenchDeck'>;该类无须外部输入参数，封装好，自己调用自己的参数就可以实现模拟扑克，高手
# >>> [Card(rank='A', suit='spades'), Card(rank='A', suit='diamonds'), Card(rank='A', suit='clubs'), Card(rank='A', suit='hearts')]
print(type(FrenchDeck()))
# 按花色排序，打印出所有的牌
#for card in deck:
#    print(card)
# 对牌进行升序排序
for card in sorted(deck, key = spades_high):
    print(card)
# >>> 结果是2，2，2，2，3，3，3，3...这样排序下去的


#------------------------------------------#
# 一个简单的二维向量 类
from math import hypot
class Vector:
    def __init__(self,x=0,y=0):
        self.x = x
        self.y = y

    def __repr__(self):
        return 'Vecotr(%s,%s)' %(self.x, self.y)

    def __abs__(self):
        return hypot(self.x, self.y)

    def __bool__(self):
        return bool(abs(self))

    def __add__(self, other):
        x = self.x + other.x
        y = self.x + other.y
        return Vector(x, y)

    def __mul__(self, other):
        return Vector(self.x * scalar, self.y * scalar)
#-------------------------------------------#

# 5.5 用户定义的可调用类型
import random
class BingoCage:
    def __init__(self, items):
        self._items = list(items)
        random.shuffle(self._items)   # 随机洗牌
    def pick(self):
        try:  # list = [1,2,3]; list.pop()结果为3，再输入list,结果为[1,2]
            return self._items.pop()
        except ImportError:
            raise LookupError('pick from empty BigoCate')
    def __call__(self):
        return self.pick()  # 实现bingo.pick() 的快捷方式是 bingo()

bingo = BingoCage(range(3))
print( bingo.pick() )   # 结果：0 or 1 or 2
print( bingo() )   # 上方已经定义了随机洗牌
print( callable(bingo) )  # True


# 16-3 定义一个计算移动平均值的协程

def averager():
    total = 0.0
    count = 0
    average = None   # 初始next后，程序停止在 yield average这里
    while 1:
        term = yield average   # 第一次接收10是从 term = yield 开始的，term立即被赋值 10
        total += term
        count += 1
        average = total/count

test = averager()
next(test)

print( test.send(10) )
print( test.send(20) )
print( test.send(30) )

# 结果 10.0;15.0;20.0;

'''




















