from Website.NewWebsiteController import RequestWebsiteController
from datetime import datetime as d

def ReturnFullURL(username, api_key, function):
    return f"https://{username}:{api_key}@api.challonge.com/v1/{function}.json"

class ChallongeController:
    def __init__(self, username, api_key):
        self.tournaments = self.Tournaments(username, api_key)

    class Tournaments:
        def __init__(self, username, api_key):
            self.username = username
            self.api_key = api_key
            self.request_controller = RequestWebsiteController()

        def ReturnIndex(self, params=None):
            full_url = ReturnFullURL(self.username, self.api_key, "tournaments")
            return self.request_controller.ReturnWebpage(webpage_url=full_url, headers={"User-Agent": "CardGamesOnHoverboards"}, params=params)

        def ReturnIndexWithIDOrUrlID(self, value, params=None):
            full_url = ReturnFullURL(self.username, self.api_key, f"tournaments/{str(value)}")
            return self.request_controller.ReturnWebpage(webpage_url=full_url, headers={"User-Agent": "CardGamesOnHoverboards"}, params=params)

        def Create(self, tournament):
            full_url = ReturnFullURL(self.username, self.api_key, "tournaments")
            return self.request_controller.ReturnWebpage(webpage_url=full_url, method="POST", headers={"User-Agent": "CardGamesOnHoverboards"}, params=tournament)

class ChallongeTournamentObject:
    def __init__(self,
                 name, tournament_type="single elimination", url="", subdomain="", description="", open_signup=False,
                 hold_third_place_match=False, pts_for_match_win=2, pts_for_match_tie=1, pts_for_game_win=2, pts_for_game_tie=1,
                 pts_for_bye=2, swiss_rounds=3, ranked_by="match wins", rr_pts_for_match_win=2, rr_pts_for_match_tie=1,
                 rr_pts_for_game_win=2, rr_pts_for_game_tie=1, accept_attachments=False, hide_forum=False, show_rounds=True,
                 private=True, notify_users_when_matches_open=True, notify_users_when_the_tournament_ends=True, sequential_pairings=False,
                 signup_cap=100, start_at=None, check_in_duration=100, grand_finals_modifier=""):

        if start_at == None:
            start_at = d.now()

        self.tournament = {}
        self.tournament['name'] = name
        self.tournament['tournament_type'] = tournament_type
        self.tournament['url'] = url
        self.tournament['subdomain'] = subdomain
        self.tournament['description'] = description
        self.tournament['open_signup'] = open_signup
        self.tournament['hold_third_place_match'] = hold_third_place_match
        self.tournament['pts_for_match_win'] = pts_for_match_win
        self.tournament['pts_for_match_tie'] = pts_for_match_tie
        self.tournament['pts_for_game_win'] = pts_for_game_win
        self.tournament['pts_for_game_tie'] = pts_for_game_tie
        self.tournament['pts_for_bye'] = pts_for_bye
        self.tournament['swiss_rounds'] = swiss_rounds
        self.tournament['ranked_by'] = ranked_by
        self.tournament['rr_pts_for_match_win'] = rr_pts_for_match_win
        self.tournament['rr_pts_for_match_tie'] = rr_pts_for_match_tie
        self.tournament['rr_pts_for_game_win'] = rr_pts_for_game_win
        self.tournament['rr_pts_for_game_tie'] = rr_pts_for_game_tie
        self.tournament['accept_attachments'] = accept_attachments
        self.tournament['hide_forum'] = hide_forum
        self.tournament['show_rounds'] = show_rounds
        self.tournament['private'] = private
        self.tournament['notify_users_when_matches_open'] = notify_users_when_matches_open
        self.tournament['notify_users_when_the_tournament_ends'] = notify_users_when_the_tournament_ends
        self.tournament['sequential_pairings'] = sequential_pairings
        self.tournament['signup_cap'] = signup_cap
        self.tournament['start_at'] = start_at
        self.tournament['check_in_duration'] = check_in_duration
        self.tournament['grand_finals_modifier'] = grand_finals_modifier

    def ReturnTournament(self):
        return self.tournament



