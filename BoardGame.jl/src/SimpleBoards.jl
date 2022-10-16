import Base: fill!, setindex!, findall, get!, empty!
import Base: <
using Base: rotr90, rot180, rotl90
using Memoize

abstract type AbstractBoard end


mutable struct SimpleBoard{S, M, N} <: AbstractBoard
    board::Matrix{S}
    function SimpleBoard(M, N)
        S = Symbol
        board = Matrix{S}(undef, M, N)
        new{S, M, N}(board)
    end
end

Base.fill!(board::SimpleBoard{S}, x::S) where S = fill!(board.board, x)
Base.findall(f::Function, board::SimpleBoard) = findall(f, board.board)
function Base.setindex!(board::SimpleBoard{S}, X::S, inds::CartesianIndex) where S
    setindex!(board.board, X, inds)
    board.board = symmetry(SimpleBoard, board.board)
end

rows(board::SimpleBoard) = eachrow(board.board)
cols(board::SimpleBoard) = eachcol(board.board)
function diag(board::SimpleBoard{S, N, N}) where {S, N}
    gen1 = @view board.board[CartesianIndex.(1:N, 1:N)]
    gen2 = @view board.board[CartesianIndex.(1:N, N:-1:1)]
    return (gen1, gen2)
end

hsym(board::Matrix) = reverse(board, dims=1)
vsym(board::Matrix) = reverse(board, dims=2)

@memoize function symmetry(::Type{SimpleBoard}, board::Matrix)
    syms = (hsym, vsym, rotr90, rotl90, rot180, rotr90∘hsym, rotl90∘hsym)
    s = map(f -> f(board), syms)
    _, i = findmin(hash, s)
    s[i]
end