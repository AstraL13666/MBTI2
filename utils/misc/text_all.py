from .text import data


class AllText:
    """['notify', 'button', 'MBTI', 'user']"""
    def __init__(self):
        self.data = data

    def notify(self, key):
        return self.data['notify'][key]

    def button(self, key):
        return self.data['button'][key]

    def mbti(self, key):
        return self.data['MBTI'][key]

    def user(self, key):
        return self.data['user'][key]


txt = AllText()
