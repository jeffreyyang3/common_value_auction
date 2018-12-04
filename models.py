from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer
)
import random
from . import config as config_py


class Constants(BaseConstants):
    config = config_py.export_data()
    name_in_url = 'common_value_auction'
    players_per_group = None
    num_rounds = 3

    instructions_template = 'common_value_auction/Instructions.html'

    min_allowable_bid = 0
    max_allowable_bid = 300




class Subsession(BaseSubsession):
    def creating_session(self):
        config = Constants.config
        roundConfig = config[0][self.round_number - 1]
        self.group_randomly()
        for player in self.get_players():

                player.nickname = "Player " + str(player.id_in_group)
        for g in self.get_groups():
            g.sequential = roundConfig['sequential']
            g.showStats = roundConfig['showStats']
            g.item_value = roundConfig['cost']
            g.showGuide = roundConfig['stated']
            g.valueEstimate = roundConfig['statedPrice']
            g.max_allowable_bid = random.randint(int(g.item_value *2), int(g.item_value * 4))
            g.ItemImagePath = 'common_value_auction/' + config[0][self.round_number - 1]['fileName']
            g.displayRange = roundConfig['displayRange']
            


class Group(BaseGroup):
    sequential = models.BooleanField()
    showGuide = models.BooleanField()
    item_value = models.FloatField()
    ItemImagePath = models.StringField()
    valueEstimate = models.FloatField()
    max_allowable_bid = models.IntegerField()
    displayRange = models.IntegerField()
    showStats = models.BooleanField()

    highest_bid = models.FloatField()

    def set_winner(self):
        print("set winner")
        players = self.get_players()
        self.highest_bid = max([p.bid_amount for p in players])

        players_with_highest_bid = [p for p in players if p.bid_amount == self.highest_bid]
        winner = random.choice(
            players_with_highest_bid)  # if tie, winner is chosen at random
        winner.is_winner = True




class Player(BasePlayer):
    item_value_estimate = models.FloatField()
    nickname = models.CharField()

    bid_amount = models.FloatField()
    payoff = models.FloatField()

    is_winner = models.BooleanField(
        initial=False,
        doc="""Indicates whether the player is the winner"""
    )

    def set_payoff(self):
        if self.is_winner:
            self.payoff = self.group.item_value - self.bid_amount

        else:
            self.payoff = 0
