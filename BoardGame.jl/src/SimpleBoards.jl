import Base: fill!, setindex!, findall, get!, empty!
import Base: <
using Base: rotr90, rot180, rotl90

using Memoize
using StaticArrays

struct SimpleBoard{S, M, N} <: AbstractBoard
    board::SMatrix{S}
    function SimpleBoard{S}(M::Integer, N::Integer, init::S=undef)
        board = SMatrix{S}(init, M, N)
        
        hsym = 
        vsym = 
        syms = (hsym, vsym, rotr90, rotl90, rot180, rotr90∘hsym, rotl90∘hsym)
        s = map(f -> f(board), syms)
        
        
        new{S, M, N}(board)
    end
end

Base.findall(f::Function, board::SimpleBoard) = findall(f, board.board)

rows(board::SimpleBoard) = eachrow(board.board)
cols(board::SimpleBoard) = eachcol(board.board)
function diag(board::SimpleBoard{S, N, N}) where {S, N}
    gen1 = @view board.board[CartesianIndex.(1:N, 1:N)]
    gen2 = @view board.board[CartesianIndex.(1:N, N:-1:1)]
    return (gen1, gen2)
end