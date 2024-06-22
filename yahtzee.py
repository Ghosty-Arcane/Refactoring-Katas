class YahtzeeScore:
    @staticmethod
    def chance(dice: list[int]) ->int:
        total = sum(dice)
        return total
    
    @staticmethod
    def yahtzee(dice: list[int]) ->int:
        if len(dice) == dice.count(dice[0]):
            return 50
        return 0
    
    @staticmethod
    def count(count: int, dice: list[int]) ->int:
        return dice.count(count) * count
    
    @staticmethod
    def of_a_kind(count: int, dice: list[int]) ->int:
        score = 0
        for i in dice:
            if dice.count(i) == count:
                score = max(i*count, score)
        return score

    @staticmethod
    def two_pair(dice: list[int]) ->int:
        pair = []
        for i in dice:
            if i in pair:
                continue
            if dice.count(i) == 2:
                pair.append(i)
        if len(pair) == 2:
            return sum(pair) *2
        return 0
    
    staticmethod
    def straight(start, dice: list[int]) ->bool:
        diceList = sorted(dice)
        compare = start
        for i in diceList:
            if i != compare:
                return False
            compare += 1
        return True

class Yahtzee:
    def __init__(self, d1: int, d2: int, d3: int, d4: int, _5: int):
        self.dice = []
        self.dice.append(d1)
        self.dice.append(d2)
        self.dice.append(d3)
        self.dice.append(d4)
        self.dice.append(_5)
        return

    @staticmethod
    def chance(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.chance([d1, d2, d3, d4, d5])

    @staticmethod
    def yahtzee(dice: list[int]) ->int:
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
    
    def fours(self) ->int:
        return YahtzeeScore.count(4, self.dice)

    def fives(self) ->int:
        return YahtzeeScore.count(5, self.dice)

    def sixes(self) ->int:
        return YahtzeeScore.count(6, self.dice)
    
    @staticmethod
    def score_pair(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.of_a_kind(2, [d1, d2, d3, d4, d5])
    
    @staticmethod
    def two_pair(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.two_pair([d1, d2, d3, d4, d5])
    
    @staticmethod
    def three_of_a_kind(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.of_a_kind(3, [d1, d2, d3, d4, d5])
    
    @staticmethod
    def four_of_a_kind(_1: int, _2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.of_a_kind(4, [_1, _2, d3, d4, d5])

    @staticmethod
    def smallStraight(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        if YahtzeeScore.straight(1, [d1, d2, d3, d4, d5]):
            return 15
        return 0

    @staticmethod
    def largeStraight(d1: int, d2: int, d3: int, d4: int, d5: int):
        if YahtzeeScore.straight(2, [d1, d2, d3, d4, d5]):
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
