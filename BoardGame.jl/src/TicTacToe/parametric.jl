empty(::Type{TicTacToe{Symbol}}) = :_
function player2cell(::Type{TicTacToe{Symbol}}, ind::Integer)
    ind == 1 && return :X
    ind == 2 && return :O
end

function cell2player(::Type{TicTacToe{Symbol}}, cell::Symbol)
    cell == :X && return 1
    cell == :O && return 2
end