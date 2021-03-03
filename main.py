from kivy.lang import Builder
from kivymd.app import MDApp
from kivy.config import Config
# from kivy.core.window import Window
from kivy.uix.screenmanager import Screen, ScreenManager
from kivy.properties import ObjectProperty


class WindowManager(ScreenManager):
    pass


class NormalScreen(Screen):
    pass


class WinScreen(Screen):
    pass


class TicTacToe(MDApp):
    window = ObjectProperty(None)

    Config.set('graphics', 'resizable', False)

    def __init__(self, **kwargs):
        super(TicTacToe, self).__init__(**kwargs)
        self.matrix_equivalent = [['0', '0', '0'] for _ in range(3)]
        self.box_index = {'a': '00', 'b': '01', 'c': '02', 'd': '10', 'e': '11', 'f': '12', 'g': '20', 'h': '21',
                          'i': '22'}
        self.number_press = 0
        self.x_score = 0
        self.o_score = 0

    def build(self):
        kv_file = Builder.load_file('tictac.kv')
        return kv_file

    def button_pressed(self, identity):
        index = self.box_index[identity]

        if self.matrix_equivalent[int(index[0])][int(index[1])] == '0':

            if self.number_press % 2 == 0:
                self.root.window.get_screen('normal').ids[identity].text = 'X'
                self.root.window.get_screen('normal').ids[identity].color = (84 / 255, 84 / 255, 84 / 255, 1)
                self.root.window.get_screen('normal').ids.turn.text = 'O  Turn'
                self.matrix_equivalent[int(index[0])][int(index[1])] = 'X'

            else:
                self.root.window.get_screen('normal').ids[identity].text = 'O'
                self.root.window.get_screen('normal').ids[identity].color = (242 / 255, 235 / 255, 211 / 255, 1)
                self.root.window.get_screen('normal').ids.turn.text = 'X  Turn'
                self.matrix_equivalent[int(index[0])][int(index[1])] = 'O'
        if self._is_win():
            self.root.current = 'win'
            if self._is_win() == 'X':
                self.root.window.get_screen('win').ids.win.text = f'''
[b][size=200sp][color=#545454]{self._is_win()}[/size][/b]
[size=80sp]WINNER![/size][/color]
'''
                self.x_score += 1
                self.root.window.get_screen(
                    'normal').ids.score_x.text = f'X                                                    {self.x_score}'
            else:
                self.root.window.get_screen('win').ids.win.text = f'''
[b][size=200sp]{self._is_win()}[/size][/b]
[size=80sp][color=#545454]WINNER![/size][/color]
'''
                self.o_score += 1
                self.root.window.get_screen(
                    'normal').ids.score_o.text = f'O                                                    {self.o_score}'

            self.restart_game()
            return
        self.number_press += 1
        if self.number_press == 9:
            self.root.current = 'win'
            self.root.window.get_screen('win').ids.win.text = f'''
[b][size=200sp][color=#545454]X[/size][/b][/color] O
[size=80sp][color=#545454]DRAW![/size][/color]
'''
            self.restart_game()
            return

    def restart_game(self):
        self.matrix_equivalent = [['0', '0', '0'] for _ in range(3)]
        self.root.window.get_screen('normal').ids.turn.text = 'X  Turn'
        self.number_press = 0
        for identity in self.box_index.keys():
            self.root.window.get_screen('normal').ids[identity].text = ''

    def _is_win(self):
        a = self.matrix_equivalent

        # rows
        if a[0][0] == a[0][1] == a[0][2] != '0':
            return a[0][0]
        elif a[1][0] == a[1][1] == a[1][2] != '0':
            return a[1][0]
        elif a[2][0] == a[2][1] == a[2][2] != '0':
            return a[2][0]

        # columns
        elif a[0][0] == a[1][0] == a[2][0] != '0':
            return a[0][0]
        elif a[0][1] == a[1][1] == a[2][1] != '0':
            return a[0][1]
        elif a[0][2] == a[1][2] == a[2][2] != '0':
            return a[0][2]

        # diagonal
        elif a[0][0] == a[1][1] == a[2][2] != '0':
            return a[0][0]
        elif a[0][2] == a[1][1] == a[2][0] != '0':
            return a[0][2]

    def quit(self):
        self.stop()


if __name__ == "__main__":
    TicTacToe().run()
