class GameController:
    def __init__(self, agent1, agent2):
        self.agent1 = agent1
        self.agent2 = agent2
        self.state = GameState()

    def play_game(self):
        while not RuleEngine.is_game_over(self.state.board):
            current_agent = self.agent1 if self.state.current_player == 0 else self.agent2
            action = current_agent.act(self.state.get_state())
            self.state.board.sow(*action)
            self.state.switch_player()
