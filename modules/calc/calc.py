from chatterbot import ChatBot
from unicodedata import numeric
import modules.calc.dict as dicts

class Calc():
    def __init__(self, querry):
        self.querry = querry
    @classmethod
    def chinese2num(self, s):
        c = ''
        for x in s:
            if (x not in dicts.stops):
                c += x
        if (c[0] == '十'):
            c = '一' + c[0:]
        number = ''
        flag = True
        for x in c:
            if (x in dicts.digit):
                flag = False
                break

        if (flag):
            for x in c:
                number += dicts.num[x]
            return int(number)
        else:
            amount = 0
            for ch in c:
                number = numeric(ch)
                if number < 10:
                    digit = number
                else:
                    amount = (amount + digit) * number if number > amount else amount + digit * number 
                    digit = 0
            if len(c) > 1 and numeric(c[-2]) != 0:
                return int(amount + digit * numeric(c[-2]) / 10)
            return int(amount + digit)
    def process(self):
        try:
            math_bot = ChatBot(
                    'MathBot',
                    logic_adapters=['chatterbot.logic.MathematicalEvaluation']
            )

            cut = []
            text = ''
            for i, x in enumerate(self.querry):
                if (x in dicts.ops):
                    num = self.chinese2num(text)
                    text = ''
                    cut.append(num)
                    cut.append(dicts.ops[x])
                else:
                    if (i >= len(self.querry) - 1):
                        text += x
                        num = self.chinese2num(text)
                        cut.append(num)
                    else:
                        text += x

            input_text = ''
            for x in cut:
                input_text += str(x) + ' '
            return math_bot.get_response(input_text).text
        except Exception as err:
            print(err)
            return '對不起 我看不懂這段數學式'

