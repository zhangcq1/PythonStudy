import random
import copy

class Poker(object):
    def __init__(self):
        self.cards=[]
        self.Init_Poker()
        self.Player_cards=[]
        self.PlayerA_cards=[]
        self.PlayerB_cards=[]
        self.FinalCares=[]
        self.Cares={}
        self.Deal()
    def Init_Poker(self):
        pattern=['Hearts','Spades','DiamOnds','Clubs']
        point=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        for pat in pattern:
            for poi in point:
               self.cards.append((pat,poi))
        self.cards.append(('red','king'))
        self.cards.append(('black','king'))
    def Deal(self):
        cards=copy.deepcopy(self.cards)
        num=53
        while num>2:
            self.Player_cards.append(cards.pop(random.randint(0,num)))
            num=num-1
            self.PlayerA_cards.append(cards.pop(random.randint(0,num)))
            num=num-1
            self.PlayerB_cards.append(cards.pop(random.randint(0,num)))
            num=num-1
    def Arrange(self,cards):
        NewCards=[]
        order=['king','2','A','K','Q','J','10','9','8','7','6','5','4','3']
        for ele in order:
            for card in cards:
                if card[1] == ele:
                    NewCards.append(card)
        return NewCards
    
    def Order(self,cards):
        num=len(cards)+1
        Newcards={}
        for i in range(1,num):
            Newcards[str(i)]=cards[i-1]
        return Newcards

    def Playcards(self,cards):
        while 1:
            Pcards=[]
            playcards=input('Please Play cards:').split(' ')
            for card in playcards:
                Pcards.append(cards[card])
            if self.Rules(Pcards):
                for card in playcards:
                    cards.pop(card)
                
                print('\n','Play cards for you:',Pcards,'\n')
                print('\n','your cards:',cards,'\n')
                break
            else:
                print('error')
    def APlaycards(self):


    def CompareRules(self,cards1,cards2):
        order=['king','2','A','K','Q','J','10','9','8','7','6','5','4','3']
        cardsA=[]
        cardsB=[]
        for card in cards1:
            cardsA.append(card[1])
        for card in cards2:
            cardsB.append(card[1])
            
        if len(cardsB)==2:
            if cardsB[0]=='king' and cardsA[1]=='king':
                return False
            
        if len(cardsA)==2:
            if cardsA[0]=='king' and cardsA[1]=='king':
                return True
            else:
                return False
        elif len(cardsB)==4 and len(set(cardsB))==1:
            if len(cardsA)==4 and len(set(cardsA))==1 and \
               order.find(cardsA[0])<order.find(cardsB[0]):
                return True
            else:
                return False
        elif len(cardsA)==4 and len(set(cardsA))==1:
            return True
        elif len(cardsB)>=20
            






        else:
            return False



    def PutRules(self,cards):
        order=['A','2','3','4','5','6','7','8','9','10','J','Q','K']
        Order=''.join(order)
        NewCards=[]
        for ele in order:
            for card in cards:
                if card[1] == ele:
                    NewCards.append(card[1])
        if len(NewCards)==1:
            return True
        if len(NewCards)==2:
            if NewCards[0]==NewCards[1]:
                return True
            else:
                return False
        if len(NewCards)==3:
            if NewCards[0]==NewCards[1]==NewCards[2]:
                return True
            else:
                return False
        if len(NewCards)==4:
            if NewCards[0]==NewCards[1]==NewCards[2]==NewCards[3]:
                return True
            elif NewCards[0]==NewCards[1]==NewCards[2] or \
                 NewCards[1]==NewCards[2]==NewCards[3]:
                return True
            else:
                return False
        if len(NewCards)>=5:
            if '2' not in NewCards and ''.join(NewCards) in Order:
                return True
            else:
                num1=len(NewCards)
                num2=len(set(NewCards))
                NewCards=list(set(NewCards))
                New_Cards=[]
                for ele in order:
                    for card in NewCards:
                        if card == ele:
                            New_Cards.append(card)
                if num1==6 and num2-num1==3:
                    return True
                    
                elif num1==8 and num2-num1==4:
                    for i in range(3):
                        if ''.join(New_Cards[i:i+2]):
                            return Ture
                    else:
                        return False
                    
                elif num1==12 and num2-num1==6:
                    for i in range(4):
                        if ''.join(New_Cards[i:i+3]):
                            return Ture
                    else:
                        return False
                    
                elif num1==16 and num2-num1==8:
                    for i in range(5):
                        if ''.join(New_Cards[i:i+4]):
                            return Ture
                    else:
                        return False
                elif num1==20 and num2-num1==10:
                    for i in range(6):
                        if ''.join(New_Cards[i:i+5]):
                            return Ture
                    else:
                        return False
                
                
            
        


        
    def main(self):
        print('Become a landlord or not')
        res=input('Please input yes or not:')
        if res =='yes':
            self.Player_cards=self.Player_cards+self.FinalCares
        else:
            if random.randint(1,2)==1:
                self.PlayerA_cards=self.PlayerA_cards+self.FinalCares
            else:
                self.PlayerB_cards=self.PlayerB_cards+self.FinalCares
                
        self.Player_cards=self.Arrange(self.Player_cards)
        self.PlayerA_cards=self.Arrange(self.PlayerA_cards)
        self.PlayerB_cards=self.Arrange(self.PlayerB_cards)
        self.Player_cards=self.Order(self.Player_cards)
        print('\n','your cards:',self.Player_cards,'\n')
        self.Playcards(self.Player_cards)
        
poker=Poker()
poker.main()
