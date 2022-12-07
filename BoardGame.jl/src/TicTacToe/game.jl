function moves(game::TicTacToe{S}) where S
    board = game.board
    blank = empty(TicTacToe{S})
    findall(isequal(blank), board)

    ## should return TicTacToe type
end

function move(game::TicTacToe{S}, move::CartesianIndex{2}) where S
    board, turn = game.board, game.turn
    board[move] = player2cell(TicTacToe{S}, who_ind(turn))

    ## should return TicTacToe type
end

function play(game::TicTacToe)
    board, turn = game.board, game.turn
    winner = win(game)
    winner == 0 || return get(turn, winner)

    player = who(turn)
    decision = decide(player, game)
    @assert decision in moves(game)
    move(game, decision)
    next(turn)
end

function win(game::TicTacToe{S}) where S
    board, turn = game.board, game.turn
    lines = Iterators.flatten((rows(board), cols(board), diag(board)))
    for line in lines
        line[1] == empty(TicTacToe{S}) && continue
        all( ==(line[1]), line) && return 1
    end
    return 0
end