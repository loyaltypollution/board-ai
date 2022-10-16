import BoardGame: HumanPlayer
import BoardGame: TicTacToe
import BoardGame: play
using Test

@testset "TicTacToe" begin
    @testset "TicTacToe Construction" begin
        gamestate = TicTacToe{Symbol}(HumanPlayer("A"), HumanPlayer("B"))
        play(gamestate)
        play(gamestate)
        play(gamestate)
        play(gamestate)
        play(gamestate)
        play(gamestate)
        display(gamestate)
    end
end