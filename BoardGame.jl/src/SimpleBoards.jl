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

Base.fill!(board::SimpleBoard, x::S) = fill!(board.board, x)
Base.setindex!(board::SimpleBoard, X::S, inds::CartesianIndex) = setindex!(board.board, X, inds)