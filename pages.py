from ._builtin import Page, WaitPage
from otree.api import Currency as c, currency_range
from .models import Constants


class Introduction(Page):
   pass

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


class ResultsWaitPage(WaitPage):
    def after_all_players_arrive(self):
        self.group.set_winner()
        for p in self.group.get_players():
            p.set_payoff()


class Results(Page):
    def vars_for_template(self):
        return {
            'is_greedy': self.group.item_value - self.player.bid_amount < 0
        }


page_sequence = [Introduction,
                 Bid,
                 ResultsWaitPage,
                 Results]
