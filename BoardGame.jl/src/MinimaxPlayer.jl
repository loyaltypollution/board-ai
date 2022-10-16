struct MinimaxPlayer <: AbstractPlayer 
    name::String
end

function decide(player::MinimaxPlayer, gamestate::AbstractGamestate)
    for move in moves(gamestate)
        println(move)
    end
end
