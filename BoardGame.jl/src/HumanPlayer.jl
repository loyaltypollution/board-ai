struct HumanPlayer <: AbstractPlayer 
    name::String
end

function decide(player::HumanPlayer, gamestate::AbstractGamestate)
    display(gamestate)
    for move in moves(gamestate)
        println(move)
    end

    userIn = match(r"(\d+).+(\d+)", readline()).captures
    x, y = parse.(Int, userIn)
    return CartesianIndex((x, y))
end
