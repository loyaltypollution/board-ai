struct TicTacToe <: AbstractGamestate
    board::SimpleBoard
    turn::SimpleTurn
end
function TicTacToe()
    players = (HumanPlayer("A"), HumanPlayer("B"))
    board = SimpleBoard(3, 3)
    fill!(board, :_)
    TicTacToe(board, SimpleTurn(players))
end

function moves(gamestate::TicTacToe)
    findall(isequal(:_), gamestate.board.board)
end
function move(gamestate::TicTacToe, move::CartesianIndex{2})
    board = gamestate.board
    board[move] = Symbol(who(gamestate.turn).name)
    next(gamestate.turn)
end

import Base.show
function Base.show(io::IO, mime::MIME"text/plain", game::TicTacToe)
    board = game.board
    b = idx -> (board.board[idx] == :_) ? " " : board.board[idx]
    println("$(b(1)) | $(b(2)) | $(b(3))") 
    println("---------")
    println("$(b(4)) | $(b(5)) | $(b(6))") 
    println("---------")
    println("$(b(7)) | $(b(8)) | $(b(9))") 
    println(who(game.turn).name, "'s turn")
end

function play(gamestate::TicTacToe)
    player = who(gamestate.turn)
    decision = decide(player, gamestate)
    @assert decision in moves(gamestate)
    move(gamestate, decision)
end
