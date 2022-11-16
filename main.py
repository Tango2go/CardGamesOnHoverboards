from Challonge.ChallongeController import ChallongeController
from Challonge.ChallongeController import ChallongeTournamentObject

challonge_controller = ChallongeController("Closeplanet", "AgCdMIckcOqemQtdO6SPeKjJaLtXggTdS2P2Gemn")
challongeTournment = ChallongeTournamentObject("name")
returnn = challonge_controller.tournaments.Create(challongeTournment.ReturnTournament())
print(returnn)