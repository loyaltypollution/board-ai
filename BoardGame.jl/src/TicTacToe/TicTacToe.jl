import Base.show


struct TicTacToe{S} <: AbstractGamestate
    board::SimpleBoard{S}
    turn::SimpleTurn
end
function TicTacToe{S}(players::Vararg{AbstractPlayer}) where S
    board = SimpleBoard(3, 3)
    fill!(board, empty(TicTacToe{S}))
    TicTacToe{S}(board, SimpleTurn(players))
end

function Base.show(io::IO, mime::MIME"text/plain", game::TicTacToe{S}) where S
    board = game.board
    b = idx -> (board.board[idx] == empty(TicTacToe{S})) ? " " : board.board[idx]
    println("$(b(1)) | $(b(2)) | $(b(3))") 
    println("---------")
    println("$(b(4)) | $(b(5)) | $(b(6))") 
    println("---------")
    println("$(b(7)) | $(b(8)) | $(b(9))") 
end

include("game.jl")
include("parametric.jl")