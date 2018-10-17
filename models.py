from otree.api import (
    models, widgets, BaseConstants, BaseSubsession, BaseGroup, BasePlayer,
    Currency as c, currency_range
)
import random
from . import config as config_py
doc = """
In a common value auction game, players simultaneously bid on the item being
auctioned.<br/>
Prior to bidding, they are given an estimate of the actual value of the item.
This actual value is revealed after the bidding.<br/>
Bids are private. The player with the highest bid wins the auction, but
payoff depends on the bid amount and the actual value.<br/>
"""


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
        for g in self.get_groups():
            g.item_value = roundConfig['cost']
            g.showGuide = roundConfig['stated']
            g.valueEstimate = roundConfig['statedPrice']
            g.ItemImagePath = 'common_value_auction/' + config[0][self.round_number - 1]['fileName']


class Group(BaseGroup):
    showGuide = models.BooleanField()
    item_value = models.FloatField()
    ItemImagePath = models.StringField()
    valueEstimate = models.FloatField()

    highest_bid = models.FloatField()

    def set_winner(self):
        players = self.get_players()
        self.highest_bid = max([p.bid_amount for p in players])

        players_with_highest_bid = [p for p in players if p.bid_amount == self.highest_bid]
        winner = random.choice(
            players_with_highest_bid)  # if tie, winner is chosen at random
        winner.is_winner = True




class Player(BasePlayer):
    item_value_estimate = models.FloatField()

    bid_amount = models.FloatField()

    is_winner = models.BooleanField(
        initial=False,
        doc="""Indicates whether the player is the winner"""
    )

    def set_payoff(self):
        if self.is_winner:
            self.payoff = self.group.item_value - self.bid_amount
            if self.payoff < 0:
                self.payoff = 0
        else:
            self.payoff = 0
