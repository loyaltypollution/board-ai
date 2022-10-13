using Base: peek

struct SimpleTurn{N}
    players::Base.Iterators.Stateful
end
function SimpleTurn(players::NTuple{N, AbstractPlayer}) where N
    SimpleTurn{N}(Iterators.Stateful(Iterators.cycle(players)))
end

who(turn::SimpleTurn) = Base.peek(turn.players)
next(turn::SimpleTurn) = Base.first(turn.players)
