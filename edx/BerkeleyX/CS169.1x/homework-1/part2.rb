# Part 2 - Rock-Paper-Scissors

## (a) Who will win a Rock-Paper-Scissors game?

# Standard exception definitions
class WrongNumberOfPlayersError < StandardError ; end
class NoSuchStrategyError < StandardError ; end

# Defines the winner of a game
# Input is case-insensitive.
# I'll uppercase inside the codeblock, but it must return the same case of the input
def rps_game_winner(game)
	raise WrongNumberOfPlayersError if !game.is_a?(Array) || game.size != 2
	raise NoSuchStrategyError if game.collect{|i| i[1]}.join.match(/^[rps]{2}$/i).nil?

	# i'll use uppercase (replicating)
	games = game.map{|g| [g[0], g[1].upcase]}

	rule_to_win = { "R" => "S", "P" => "R", "S" => "P" }
	
	if rule_to_win[games[0][1]] == games[1][1] || games[0][1] == games[1][1]
		game[0]
	else
		game[1]
	end
end

## (b) Who will win a rock-paper-scissors tournament?
# Defines the winner of a Tournament
def rps_tournament_winner(games)
	if games[0][0].is_a?(Array)
		rps_game_winner([rps_tournament_winner(games[0]), rps_tournament_winner(games[1])])
	else
		rps_game_winner(games)
	end
end