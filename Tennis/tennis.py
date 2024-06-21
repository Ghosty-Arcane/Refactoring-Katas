# -*- coding: utf-8 -*-

tennisScore = {
    0: 'Love',
    1: 'Fifteen',
    2: 'Thirty',
    3: 'Forty'
}

class TennisGameDefactored1:

    def __init__(self, player1Name: str, player2Name: str):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0
        return
        
    def won_point(self, playerName) ->None:
        if playerName == self.player1Name:
            self.p1Points += 1
        else:
            self.p2Points += 1
        return
    
    def score(self) ->str:
        result = ''
        if self.p1Points > 3 or self.p2Points > 3:                      ## Endgame
            minusResult = self.p1Points-self.p2Points
            if minusResult == 0:
                result = 'Deuce'
            elif minusResult == 1:
                result = f'Advantage {self.player1Name}'
            elif minusResult == -1:
                result = f'Advantage {self.player2Name}'
            elif minusResult > 1:
                result = f'Win for {self.player1Name}'
            else:
                result = f'Win for {self.player2Name}'

        elif self.p1Points == self.p2Points:                            ## Tie game prior to endgame
            result = f'{tennisScore[self.p1Points]}-All'

        else:                                                           ## Early game, no tie
            result = f'{tennisScore[self.p1Points]}-{tennisScore[self.p2Points]}'
        return result


class TennisGameDefactored2:
    def __init__(self, player1Name, player2Name):
        self.player1Name = player1Name
        self.player2Name = player2Name
        self.p1Points = 0
        self.p2Points = 0
        
    def won_point(self, playerName):
        if playerName == self.player1Name:
            self.SetP1Score(1)
        else:
            self.SetP2Score(1)
    
    def score(self):
        result = ''
        P1res = ''
        P2res = ''
        if self.p1Points < 4:
            P1res = tennisScore[self.p1Points]
        if self.p2Points < 4:
            P2res = tennisScore[self.p2Points]

        if P1res == P2res and P1res == '':
            result = 'Deuce'
        elif P1res == P2res:
            result = f'{P1res}-All'
        else:
            result = P1res + "-" + P2res
        
        if self.p1Points > self.p2Points and self.p2Points >= 3:
            result = "Advantage " + self.player1Name
        
        if (self.p2Points > self.p1Points and self.p1Points >= 3):
            result = "Advantage " + self.player2Name
        
        if (self.p1Points>=4 and (self.p1Points-self.p2Points)>=2):
            result = "Win for " + self.player1Name
        if (self.p2Points>=4 and (self.p2Points-self.p1Points)>=2):
            result = "Win for " + self.player2Name
        return result
    
    def SetP1Score(self, number):
        for _ in range(number):
            self.p1Points +=1
            
    def SetP2Score(self, number):
        for _ in range(number):
            self.p2Points +=1
            
    
class TennisGameDefactored3:
    def __init__(self, player1Name, player2Name):
        self.p1N = player1Name
        self.p2N = player2Name
        self.p1 = 0
        self.p2 = 0
        
    def won_point(self, n):
        if n == self.p1N:
            self.p1 += 1
        else:
            self.p2 += 1
    
    def score(self):
        if (self.p1 < 4 and self.p2 < 4):
            p = ["Love", "Fifteen", "Thirty", "Forty"]
            s = p[self.p1]
            return s + "-All" if (self.p1 == self.p2) else s + "-" + p[self.p2]
        else:
            if (self.p1 == self.p2):
                return "Deuce"
            s = self.p1N if self.p1 > self.p2 else self.p2N
            return "Advantage " + s if ((self.p1-self.p2)*(self.p1-self.p2) == 1) else "Win for " + s

# NOTE: You must change this to point at the one of the three examples that you're working on!
TennisGame = TennisGameDefactored2
