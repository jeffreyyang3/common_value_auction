from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
    def is_displayed(self):
        return self.round_number == 1


class Bid(Page):
    form_model = 'player'
    form_fields = ['bid_amount']
    def vars_for_template(self):
        print(self.group.ItemImagePath)
        return{
            'image_path': self.group.ItemImagePath,
            'showGuide': self.group.showGuide,
            'guidePrice': self.player.item_value_estimate
        }


class NonSeqWait(WaitPage):
    def is_displayed(self):
        return not self.group.sequential
    def vars_for_template(self):
        return{
            'nickname': "Player " + str(self.player.id_in_group())
        }
    def after_all_players_arrive(self):
        self.group.set_winner()
        for p in self.group.get_players():
            p.set_payoff()
class SeqWait(WaitPage):
    template_name = 'common_value_auction/SeqWait.html'
    def is_displayed(self):
        return self.group.sequential


class Results(Page):
    def vars_for_template(self):
        return {
            'payoff': self.player.payoff,
            'is_greedy': self.group.item_value - self.player.bid_amount < 0
        }


page_sequence = [Introduction,
                 Bid,
                 NonSeqWait,
                 SeqWait,
                 Results]
