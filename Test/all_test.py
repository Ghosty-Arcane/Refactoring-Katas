# -*- coding: utf-8 -*-

import pytest
from tennis import TennisGame
from Test.tennis_unittest import test_cases, play_game
from yahtzee import Rule, Yahtzee, YahtzeeScore

class TestTennis:

    @pytest.mark.parametrize('p1Points p2Points score p1Name p2Name'.split(), test_cases)
    def test_get_score(self, p1Points, p2Points, score, p1Name, p2Name):
        game = play_game(p1Points, p2Points, p1Name, p2Name)
        assert score == game.score()


class TestYahtzee:
	def test_invalid_Score_rule(self):
		assert 0 == YahtzeeScore.Score('badRule', [1, 2, 3, 4, 5])

	def test_chance_scores_sum_of_all_dice(self):
		assert 15 == Yahtzee.chance(2,3,4,5,1)
		assert 16 == Yahtzee.chance(3,3,4,5,1)
		assert 15 == YahtzeeScore.Score(Rule.CHANCE, [2,3,4,5,1])
		assert 16 == YahtzeeScore.Score(Rule.CHANCE, [3,3,4,5,1])

	def test_yahtzee_scores_50(self):
		assert 50 == Yahtzee.yahtzee([4,4,4,4,4])
		assert 50 == Yahtzee.yahtzee([6,6,6,6,6])
		assert 0 == Yahtzee.yahtzee([6,6,6,6,3])
		assert 50 == YahtzeeScore.Score(Rule.YAHTZEE, [4,4,4,4,4])
		assert 50 == YahtzeeScore.Score(Rule.YAHTZEE, [6,6,6,6,6])
		assert 0 == YahtzeeScore.Score(Rule.YAHTZEE, [6,6,6,6,3])

	def test_1s(self):
		assert 1 == Yahtzee.ones(1,2,3,4,5)
		assert 2 == Yahtzee.ones(1,2,1,4,5)
		assert 0 == Yahtzee.ones(6,2,2,4,5)
		assert 4 == Yahtzee.ones(1,2,1,1,1)
		assert 1 == YahtzeeScore.Score(Rule.ONES, [1,2,3,4,5])
		assert 2 == YahtzeeScore.Score(Rule.ONES, [1,2,1,4,5])
		assert 0 == YahtzeeScore.Score(Rule.ONES, [6,2,2,4,5])
		assert 4 == YahtzeeScore.Score(Rule.ONES, [1,2,1,1,1])

	def test_2s(self):
		assert 4 == Yahtzee.twos(1,2,3,2,6)
		assert 10 == Yahtzee.twos(2,2,2,2,2)
		assert 4 == YahtzeeScore.Score(Rule.TWOS, [1,2,3,2,6])
		assert 10 == YahtzeeScore.Score(Rule.TWOS, [2,2,2,2,2])

	def test_threes(self):
		assert 6 == Yahtzee.threes(1,2,3,2,3)
		assert 12 == Yahtzee.threes(2,3,3,3,3)
		assert 6 == Yahtzee.threes(1,2,3,2,3)
		assert 12 == Yahtzee.threes(2,3,3,3,3)

	def test_fours_test(self):
		assert 12 == Yahtzee(4,4,4,5,5).fours()
		assert 8 == Yahtzee(4,4,5,5,5).fours()
		assert 4 == Yahtzee(4,5,5,5,5).fours()
		assert 12 == Yahtzee(4,4,4,5,5).fours()
		assert 8 == Yahtzee(4,4,5,5,5).fours()
		assert 4 == Yahtzee(4,5,5,5,5).fours()

	def test_fives(self):
		assert 10 == Yahtzee(4,4,4,5,5).fives()
		assert 15 == Yahtzee(4,4,5,5,5).fives()
		assert 20 == Yahtzee(4,5,5,5,5).fives()
		assert 10 == Yahtzee(4,4,4,5,5).fives()
		assert 15 == Yahtzee(4,4,5,5,5).fives()
		assert 20 == Yahtzee(4,5,5,5,5).fives()

	def test_sixes_test(self):
		assert 0 == Yahtzee(4,4,4,5,5).sixes()
		assert 6 == Yahtzee(4,4,6,5,5).sixes()
		assert 18 == Yahtzee(6,5,6,6,5).sixes()
		assert 0 == Yahtzee(4,4,4,5,5).sixes()
		assert 6 == Yahtzee(4,4,6,5,5).sixes()
		assert 18 == Yahtzee(6,5,6,6,5).sixes()

	def test_one_pair(self):
		assert 6 == Yahtzee.score_pair(3,4,3,5,6)
		assert 10 == Yahtzee.score_pair(5,3,3,3,5)
		assert 12 == Yahtzee.score_pair(5,3,6,6,5)
		assert 6 == Yahtzee.score_pair(3,4,3,5,6)
		assert 10 == Yahtzee.score_pair(5,3,3,3,5)
		assert 12 == Yahtzee.score_pair(5,3,6,6,5)

	def test_two_Pair(self):
		assert 16 == Yahtzee.two_pair(3,3,5,4,5)
		assert 0 == Yahtzee.two_pair(3,3,5,5,5)
		assert 16 == Yahtzee.two_pair(3,3,5,4,5)
		assert 0 == Yahtzee.two_pair(3,3,5,5,5)
  
	def test_three_of_a_kind(self):
		assert 9 == Yahtzee.three_of_a_kind(3,3,3,4,5)
		assert 15 == Yahtzee.three_of_a_kind(5,3,5,4,5)
		assert 0 == Yahtzee.three_of_a_kind(3,3,3,3,5)
		assert 9 == Yahtzee.three_of_a_kind(3,3,3,4,5)
		assert 15 == Yahtzee.three_of_a_kind(5,3,5,4,5)
		assert 0 == Yahtzee.three_of_a_kind(3,3,3,3,5)
  
	def test_four_of_a_knd(self):
		assert 12 == Yahtzee.four_of_a_kind(3,3,3,3,5)
		assert 20 == Yahtzee.four_of_a_kind(5,5,5,4,5)
		assert 0 == Yahtzee.three_of_a_kind(3,3,3,3,3)
		assert 12 == Yahtzee.four_of_a_kind(3,3,3,3,5)
		assert 20 == Yahtzee.four_of_a_kind(5,5,5,4,5)
		assert 0 == Yahtzee.three_of_a_kind(3,3,3,3,3)

	def test_smallStraight(self):
		assert 15 == Yahtzee.smallStraight(1,2,3,4,5)
		assert 15 == Yahtzee.smallStraight(2,3,4,5,1)
		assert 0 == Yahtzee.smallStraight(1,2,2,4,5)
		assert 15 == Yahtzee.smallStraight(1,2,3,4,5)
		assert 15 == Yahtzee.smallStraight(2,3,4,5,1)
		assert 0 == Yahtzee.smallStraight(1,2,2,4,5)

	def test_largeStraight(self):
		assert 20 == Yahtzee.largeStraight(6,2,3,4,5)
		assert 20 == Yahtzee.largeStraight(2,3,4,5,6)
		assert 0 == Yahtzee.largeStraight(1,2,2,4,5)
		assert 20 == Yahtzee.largeStraight(6,2,3,4,5)
		assert 20 == Yahtzee.largeStraight(2,3,4,5,6)
		assert 0 == Yahtzee.largeStraight(1,2,2,4,5)

	def test_fullHouse(self):
		assert 18 == Yahtzee.fullHouse(6,2,2,2,6)
		assert 0 == Yahtzee.fullHouse(2,3,4,5,6)
		assert 18 == Yahtzee.fullHouse(6,2,2,2,6)
		assert 0 == Yahtzee.fullHouse(2,3,4,5,6)
   
