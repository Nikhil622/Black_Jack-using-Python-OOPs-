
suits=('DIAMOND','SPADE','CLUBS','HEARTS')
ranks=('TWO','THREE','FOUR','FIVE','SIX','SEVEN','EIGHT','NINE','TEN','JACK','QUEEN','KING','ACE')
values={'TWO':2,'THREE':3,'FOUR':4,'FIVE':5,'SIX':6,'SEVEN':7,'EIGHT':8,'NINE':9,'TEN':10,'JACK':10,'QUEEN':10,'KING':10,'ACE':(1,11)}



class card():
    def __init__(self,suit,rank):
        self.suit=suit
        self.rank=rank
        self.value=values[rank]
    def __str__(self):
        return f'{self.rank} of {self.suit}'


class deck():
    def __init__(self):
        self.card=[]
        for x in suits:
            for y in ranks:
                self.card.append(card(x,y))
    def shuffle(self):
        import random
        random.shuffle(self.card)
    def remove(self):
        return self.card.pop(0)
    def __len__(self):
        return len(self.card)

class player():
    def __init__(self):
        self.name=input('Name of player:-')
        self.balance=int(input('Enter Total Amount You Have:-'))
    def playingAmt(self,x):
        if self.balance<x:
            while self.balance<x:
                print('BALANCE IS INSUFFICIENT!')
                x=int(input('PLEASE CHOOSE ANOTHER AMOUNT:-'))
        return x
    def amount(self):
        return self.balance
    def winAmount(self,winAmt):
        self.balance=self.balance+winAmt
    def lost(self,x):
        self.balance=self.balance-x

X=deck()
class Black_Jack():
    def __init__(self):
        self.PlayerOne=player()
        self.DECK=X
        self.sumCard=0
        
    def Computer(self):
        sumX=0
        while sumX<=17:
            card=self.DECK.remove()
            print(card.__str__())
            if card.rank!='ACE':
                sumX=sumX+card.value
            else:
                if sumX+11>21:
                    sumX=sumX+1
                else:
                    sumX=sumX+11
            print(sumX)
        if sumX<=21:
            return sumX
        else:
            return -1
    
    def play(self):
        y=input('To play press Y else press any key:-')
        return y=='Y'
    def Hit(self):
        return 'Y'==input('To Open New Card Press Y!\n Else Press Any Key!')

    def fun(self):
        M=self.DECK
        self.DECK.shuffle()
        while self.play():
            x=int(input('Enter amount to play:-'))
            while True:
                PlayingAmount=self.PlayerOne.playingAmt(x)
                break
            self.DECK.shuffle()
            while self.Hit():
                Val=self.DECK.remove()
                print(Val)
                if Val.rank!='ACE':
                    self.sumCard=self.sumCard+Val.value
                else:
                    self.sumCard=self.sumCard+int(input('ACE-CARD:-Choose between 1 or 11 :-'))
                print(self.sumCard)
                if self.sumCard>21:
                    print('BUSTED!\nYOU LOST!')
                    self.PlayerOne.lost(PlayingAmount)
                    break
            if self.sumCard>21:
                self.DECK=deck()
                print(self.DECK.__len__())
                self.sumCard=0
                continue
                    
            if self.sumCard<=21:
                print("Computers Turn!")
                sumOFcomputer=self.Computer()
                if self.sumCard > sumOFcomputer:
                    print('YOU WON!')
                    self.PlayerOne.winAmount(PlayingAmount)
                elif self.sumCard==sumOFcomputer:
                    print('Match Draw!')
                else:
                    print('YOU LOST!')
                    self.PlayerOne.lost(PlayingAmount)
                self.DECK=deck()
                print(self.DECK.__len__())
                self.sumCard=0

            


B=Black_Jack()

B.fun()

len(B.DECK)

B.PlayerOne.balance
