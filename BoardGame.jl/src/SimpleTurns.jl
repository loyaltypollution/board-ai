using Base: peek

struct SimpleTurn{N}
    players::Base.Iterators.Stateful
end
SimpleTurn(players::NTuple{N, AbstractPlayer}) where N = SimpleTurn{N}(players |> enumerate |> Iterators.cycle |> Iterators.Stateful)

who_ind(turn::SimpleTurn) = Base.peek(turn.players)[1]
who(turn::SimpleTurn) = Base.peek(turn.players)[2]

next(turn::SimpleTurn) = Base.first(turn.players)
get(turn::SimpleTurn, ind::Integer) = turn.players.itr.xs.itr[ind]