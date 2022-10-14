using BoardGame
using Test

@testset "TicTacToe" begin
    @testset "TicTacToe Construction" begin
        gamestate = BoardGame.TicTacToe()
        BoardGame.play(gamestate)
    end
end