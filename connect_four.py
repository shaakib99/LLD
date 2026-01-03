class Player:
    color: str


class Board:
    board: list[list[str]] = [[''] * 7 for _ in range(6)]

    def placeDisc(self, column: int, player: Player) -> bool:
        for row in range(5, -1, -1):
            if self.board[row][column] == '':
                self.board[row][column] = player.color
                return True
        return False
    
    def checkWin(self, filler: str) -> bool:
        # Check horizontal
        for row in range(6):
            for col in range(4):
                if all(self.board[row][col + i] == filler for i in range(4)):
                    return True
        
        # Check vertical
        for col in range(7):
            for row in range(3):
                if all(self.board[row + i][col] == filler for i in range(4)):
                    return True
        
        # Check diagonal (bottom-left to top-right)
        for row in range(3, 6):
            for col in range(4):
                if all(self.board[row - i][col + i] == filler for i in range(4)):
                    return True
        
        # Check diagonal (top-left to bottom-right)
        for row in range(3):
            for col in range(4):
                if all(self.board[row + i][col + i] == filler for i in range(4)):
                    return True
        
        return False
    
    def checkDraw(self) -> bool:
        for col in range(7):
            if self.board[0][col] == '':
                return False
        return True


class GameManager:
    player1: Player
    player2: Player
    board: Board
    state: str
    current_turn: Player
    def __init__(self, player1: Player, player2: Player):
        self.player1 = player1
        self.player2 = player2
        self.board = Board()
        self.current_turn = player1
        self.state = 'ONGOING'
    
    def makeMove(self, player: Player, column: int) -> str:
        if self.state != 'ONGOING':
            raise Exception('GAME_ALREADY_ENDED')
        
        if player != self.current_turn:
            raise Exception('NOT_YOUR_TURN')
        
        self.board.placeDisc(column, player)
        
        if self.board.checkWin(player.color):
            self.state = f'{player.color}_WINS'
            return self.state
        
        # Check for draw
        if self.board.checkDraw():
            self.state = 'DRAW'
            return self.state
        
        self.setTurn()
        return 'MOVE_ACCEPTED'
    
    def setTurn(self):
        if self.current_turn == self.player1:
            self.current_turn = self.player2
        else:
            self.current_turn = self.player1

    def getCurrentPlayer(self) -> Player:
        return self.current_turn

    def checkGameState(self, filler: str) -> str:
        return self.state