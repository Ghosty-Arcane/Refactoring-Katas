from enum import Enum, auto

class Rule(Enum):
    CHANCE = auto()
    YAHTZEE = auto()
    ONES = auto()
    TWOS = auto()
    THREES = auto()
    FOURS = auto()
    FIVES = auto()
    SIXES = auto()
    PAIR = auto()
    TWO_PAIR = auto()
    THREE_KIND = auto()
    SMALL_STRAIGHT = auto()
    LARGE_STRAIGHT = auto()
    FULL_HOUSE = auto()
    

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
    
    @staticmethod
    def straight(start: int, dice: list[int]) ->bool:
        diceList = sorted(dice)
        compare = start
        for i in diceList:
            if i != compare:
                return False
            compare += 1
        return True
    
    @staticmethod
    def fullHouse(dice: list[int]) ->int:
        pair = YahtzeeScore.of_a_kind(2, dice)
        trio = YahtzeeScore.of_a_kind(3, dice)
        if pair != 0 and trio != 0:
            return pair + trio
        return 0
    
    @staticmethod
    def Score(selection, dice: list[int]) ->int:
        match selection:
            case Rule.CHANCE:
                return YahtzeeScore.chance(dice)
            case _:
                return 0
    

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
    def largeStraight(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        if YahtzeeScore.straight(2, [d1, d2, d3, d4, d5]):
            return 20
        return 0

    @staticmethod
    def fullHouse(d1: int, d2: int, d3: int, d4: int, d5: int) ->int:
        return YahtzeeScore.fullHouse([d1, d2, d3, d4, d5])
