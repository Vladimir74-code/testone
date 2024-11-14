def print_board(board):
    #отображает текущее состояние игрового поля
    print("\n".join(" | ".join(row) for row in board))
    print("-" * 9)

def check_winner(board):
    #Проверяет, завершилась ли игра
    lines = board + list(zip(*board)) + [ [board[i][i] for i in range(3)], [board[i][2-i] for i in range(3)] ]
    if any(line[0] == line[1] == line[2] != " " for line in lines):
        return line[0]
    if all(cell != " " for row in board for cell in row):
        return "Ничья"
    return None

def is_valid_move(board, row, col):
    #Проверяет корректность хода
    return 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " "

def main():
    #Основная функция игры
    board = [[" " for _ in range(3)] for _ in range(3)]
    current_player = "X"

    while True:
        print_board(board)
        try:
            row, col = map(int, input(f"Игрок {current_player}, введите координаты (строка и столбец): ").split())
            if is_valid_move(board, row, col):
                board[row][col] = current_player
                winner = check_winner(board)
                if winner:
                    print_board(board)
                    print("Игра завершилась ничьей!" if winner == "Ничья" else f"Поздравляем, игрок {winner} выиграл!")
                    break
                current_player = "O" if current_player == "X" else "X"
            else:
                print("Некорректный ход. Попробуйте снова.")
        except ValueError:
            print("Пожалуйста, введите два целых числа, разделенных пробелом.")
#запускаем игру
if __name__ == "__main__":
    main()