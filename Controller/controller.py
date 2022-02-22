from Model.model_player_class import Model
from View.view import View


class Controller:
    """controller"""

    def __init__(self, model: Model, view: View) -> None:
        self.model = model
        self.view = view

    def start(self):
        self.view.print_board(self)
        self.view.start_main_loop()
