class YahtzeeScore:
    @staticmethod
    def chance(dice: list[int,int,int,int,int]) ->int:
        total = sum(dice)
        return total
    
    @staticmethod
    def yahtzee(dice: list[int,int,int,int,int]) ->int:
        if len(dice) == dice.count(dice[0]):
            return 50
        return 0
    
    @staticmethod
    def count(count: int, dice: list[int,int,int,int,int]) ->int:
        return dice.count(count) * count


class Yahtzee:

    @staticmethod
    def chance(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.chance([d1, d2, d3, d4, d5])

    @staticmethod
    def yahtzee(dice: list[int,int,int,int,int]) ->int:
        return YahtzeeScore.yahtzee(dice)
    
    @staticmethod
    def ones(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.count(1, [d1, d2, d3, d4, d5])

    @staticmethod
    def twos(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.count(2, [d1, d2, d3, d4, d5])
    
    @staticmethod
    def threes(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.count(3, [d1, d2, d3, d4, d5])

    def __init__(self, d1: int, d2: int, d3: int, d4: int, _5: int):
        self.dice = []
        self.dice.append(d1)
        self.dice.append(d2)
        self.dice.append(d3)
        self.dice.append(d4)
        self.dice.append(_5)
        return
    
    def fours(self) ->int:
        return YahtzeeScore.count(4, self.dice)

    def fives(self) ->int:
        return YahtzeeScore.count(5, self.dice)

    def sixes(self) ->int:
        return YahtzeeScore.count(6, self.dice)
    
    @staticmethod
    def score_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        at = 0
        for at in range(6):
            if (counts[6-at-1] == 2):
                return (6-at)*2
        return 0
    
    @staticmethod
    def two_pair( d1,  d2,  d3,  d4,  d5):
        counts = [0]*6
        counts[d1-1] += 1
        counts[d2-1] += 1
        counts[d3-1] += 1
        counts[d4-1] += 1
        counts[d5-1] += 1
        n = 0
        score = 0
        for i in range(6):
            if (counts[6-i-1] == 2):
                n = n+1
                score += (6-i)
                    
        if (n == 2):
            return score * 2
        else:
            return 0
    
    @staticmethod
    def four_of_a_kind( _1,  _2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[_1-1] += 1
        tallies[_2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        for i in range(6):
            if (tallies[i] == 4):
                return (i+1) * 4
        return 0
    

    @staticmethod
    def three_of_a_kind( d1,  d2,  d3,  d4,  d5):
        t = [0]*6
        t[d1-1] += 1
        t[d2-1] += 1
        t[d3-1] += 1
        t[d4-1] += 1
        t[d5-1] += 1
        for i in range(6):
            if (t[i] == 3):
                return (i+1) * 3
        return 0
    

    @staticmethod
    def smallStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[0] == 1 and
            tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1):
            return 15
        return 0
    

    @staticmethod
    def largeStraight( d1,  d2,  d3,  d4,  d5):
        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1
        if (tallies[1] == 1 and
            tallies[2] == 1 and
            tallies[3] == 1 and
            tallies[4] == 1
            and tallies[5] == 1):
            return 20
        return 0
    

    @staticmethod
    def fullHouse( d1,  d2,  d3,  d4,  d5):
        tallies = []
        _2 = False
        i = 0
        _2_at = 0
        _3 = False
        _3_at = 0

        tallies = [0]*6
        tallies[d1-1] += 1
        tallies[d2-1] += 1
        tallies[d3-1] += 1
        tallies[d4-1] += 1
        tallies[d5-1] += 1

        for i in range(6):
            if (tallies[i] == 2): 
                _2 = True
                _2_at = i+1
            

        for i in range(6):
            if (tallies[i] == 3): 
                _3 = True
                _3_at = i+1
            

        if (_2 and _3):
            return _2_at * 2 + _3_at * 3
        else:
            return 0
