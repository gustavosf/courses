require '../part2.rb'
require 'test/unit'

class TestPart2 < Test::Unit::TestCase
	def testGameWinner
		# basic testing with P1 winning
		assert_equal(["Armando", "S"], rps_game_winner([["Armando", "S"], ["Dave", "P"]]))
		assert_equal(["Armando", "R"], rps_game_winner([["Armando", "R"], ["Dave", "S"]]))
		assert_equal(["Armando", "P"], rps_game_winner([["Armando", "P"], ["Dave", "R"]]))

		# draw test, p1 must win
		assert_equal(["Armando", "S"], rps_game_winner([["Armando", "S"], ["Dave", "S"]]))

		# basic testing with P2 winning
		assert_equal(["Dave", "S"], rps_game_winner([["Armando", "P"], ["Dave", "S"]]))
		assert_equal(["Dave", "R"], rps_game_winner([["Armando", "S"], ["Dave", "R"]]))
		assert_equal(["Dave", "P"], rps_game_winner([["Armando", "R"], ["Dave", "P"]]))

		# Testing minuscules :O
		assert_equal(["Dave", "s"],    rps_game_winner([["Armando", "p"], ["Dave", "s"]]))
		assert_equal(["Armando", "s"], rps_game_winner([["Armando", "s"], ["Dave", "p"]]))

		# Testing exceptions
		assert_raise NoSuchStrategyError do
			rps_game_winner([["Armando", "x"], ["Dave", "S"]])
		end
		assert_raise NoSuchStrategyError do
			rps_game_winner([["Armando", "S"], ["Dave", "x"]])
		end
		assert_raise WrongNumberOfPlayersError do
			rps_game_winner([["Armando", "S"]])
		end
		assert_raise WrongNumberOfPlayersError do
			rps_game_winner([["Armando", "S"], ["Armando", "P"], ["Richard", "R"]])
		end
		assert_raise WrongNumberOfPlayersError do
			rps_game_winner(nil)
		end
	end

	def testTournamentWinner
		assert_equal(
			["Richard", "R"],
			rps_tournament_winner([[
				[["Armando", "P"], ["Dave", "S"]],
				[["Richard", "R"],  ["Michael", "S"]],
			],[ 
				[["Allen", "S"], ["Omer", "P"]],
				[["David E.", "R"], ["Richard X.", "P"]]
			]]))

		assert_equal(
			["Richard", "R"],
			rps_tournament_winner([["Richard", "R"],  ["Michael", "S"]]))
	end
end