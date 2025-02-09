class GameController:
    def __init__(self):
        self.board = Board()
        self.players = [Player(0), Player(1)]
        self.rule_engine = RuleEngine()
        self.state = GameState()

    def play_turn(self):
        current_player = self.players[self.state.current_player_idx]
        opponent = self.players[1 - self.state.current_player_idx]
        
        action = current_player.select_move(self.board, self.board.territories[current_player.player_id])
        print(f"\nPlayer {current_player.get_player_number()} chooses action: {action}")

        final_row, final_col = self.rule_engine.execute_move(current_player, action, self.board)
        self.rule_engine.check_capture(current_player, opponent, final_row, final_col, self.board)
        self.state.print_move_result(self.board, current_player)

        winner = self.rule_engine.check_winner(self.players)
        if winner:
            self.state.game_over = True
            print(f"\nGame Over! Player {winner.get_player_number()} wins!")
            print(f"Final territory captures: {[p.captured_territories for p in self.players]}")
            return

        if self.board.is_empty():
            self.state.start_new_round()
            self.board.reset()

    def play(self):
        while not self.state.game_over:
            self.state.print_game_state(self.board, self.players[self.state.current_player_idx])
            self.play_turn()

        input("\nPress Enter to exit...")