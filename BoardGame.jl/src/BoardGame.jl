module BoardGame

abstract type AbstractTurn end
abstract type AbstractGamestate end
abstract type AbstractPlayer end
abstract type AbstractBoard end

include("HumanPlayer.jl")
include("SimpleBoards.jl")
include("SimpleTurns.jl")

include("TicTacToe/TicTacToe.jl")

end