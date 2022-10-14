import Base.fill!
import Base.setindex!

abstract type AbstractBoard end


struct SimpleBoard{S, M, N} <: AbstractBoard
    board::Matrix{S}
    function SimpleBoard(M, N)
        S = Symbol
        board = Matrix{S}(undef, M, N)
        new{S, M, N}(board)
    end
end

Base.fill!(board::SimpleBoard{S}, x::S) where S = fill!(board.board, x)
Base.setindex!(board::SimpleBoard{S}, X::S, inds::CartesianIndex) where S = setindex!(board.board, X, inds)

