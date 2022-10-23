# Task № 1
# Создайте программу для игры с конфетами человек против человека.
# Условие задачи: На столе лежит 2021 конфета. Играют два игрока делая ход друг после друга. Первый ход определяется жеребьёвкой.
# За один ход можно забрать не более чем 28 конфет. Все конфеты оппонента достаются сделавшему последний ход.
# Сколько конфет нужно взять первому игроку, чтобы забрать все конфеты у своего конкурента?
# Добавьте игру против бота
# Подумайте как наделить бота ""интеллектом""


# from random import randint


# first_move = randint(1,2)
# maximum_candies = 2021
# print(first_move)

# if (first_move == 1):
#   while(maximum_candies > 0):
#      player1 = int(input('Enter numbers of candies player1: '))
#      player2 = int(input('Enter numbers of candies player2: '))
#      if ((player1 > 28) and (player2 > 28)):
#       print('Input error')
#      else:
#         maximum_candies = maximum_candies - player1
#         if (maximum_candies < 0):
#             break
#         print(f'after the first player has taken away', str(player1) ,'candies, the remainder of the maximum number = ' + str(maximum_candies)) 
#         maximum_candies = maximum_candies - player2
#         if (maximum_candies < 0):
#             break
#         print(f'after the second player has taken away', str(player2) ,'candies, the remainder of the maximum number = ' + str(maximum_candies))  

# elif(first_move == 2):
  
#   while(maximum_candies > 0):
#     player2 = int(input('Enter numbers of candies player2: '))
#     player1 = int(input('Enter numbers of candies player1: '))
#     if (player1 and player2 > 28):
#      print('Error')
#     else:
#         maximum_candies = maximum_candies - player2
#         if (maximum_candies < 0):
#             break
#         print(f'after the second player has taken away', str(player2) ,'candies, the remainder of the maximum number = ' + str(maximum_candies))
#         maximum_candies = maximum_candies - player1
#         if (maximum_candies < 0):
#             break
#         print(f'after the first player has taken away', str(player1) ,'candies, the remainder of the maximum number = ' + str(maximum_candies)) 



# Task № 2 
# Создайте программу для игры в ""Крестики-нолики"".
# board = list(range(1,10))

# def draw_board(board):
#     print ("-" * 13)
#     for i in range(3):
#         print ("|", board[0+i*3], "|", board[1+i*3], "|", board[2+i*3], "|")
#         print ("-" * 13)

# def take_input(player_token):
#     valid = False
#     while not valid:
#         player_answer = input("Where will we put it " + player_token+"? ")
#         try:
#             player_answer = int(player_answer)
#         except:
#             print ("Incorrect input. Are you sure you entered a number?")
#             continue
#         if player_answer >= 1 and player_answer <= 9:
#             if (str(board[player_answer-1]) not in "XO"):
#                 board[player_answer-1] = player_token
#                 valid = True
#             else:
#                 print ("This cell is already occupied")
#         else:
#             print ("Incorrect input. Enter a number from 1 to 9 to make a move")

# def check_win(board):
#     win_coord = ((0,1,2),(3,4,5),(6,7,8),(0,3,6),(1,4,7),(2,5,8),(0,4,8),(2,4,6))
#     for each in win_coord:
#         if board[each[0]] == board[each[1]] == board[each[2]]:
#             return board[each[0]]
#     return False

# def main(board):
#     counter = 0
#     win = False
#     while not win:
#         draw_board(board)
#         if counter % 2 == 0:
#             take_input("X")
#         else:
#             take_input("O")
#         counter += 1
#         if counter > 4:
#             tmp = check_win(board)
#             if tmp:
#                 print (tmp, "won!")
#                 win = True
#                 break
#         if counter == 9:
#             print ("draw!")
#             break
#     draw_board(board)

# main(board)


# Task № 3 
# Реализуйте RLE алгоритм: реализуйте модуль сжатия и восстановления данных.
# Входные и выходные данные хранятся в отдельных текстовых файлах.

# rle_string = input('Enter rle: ')
# data = open('input_rle_string.txt', 'w')
# data.write(str(rle_string) + ' ')
# data = open('output_rle_string.txt', 'w')
# count = 1
# for i in range(len(rle_string)-1):
#     if (i < len(rle_string)-1):
#         if rle_string[i] == rle_string[i+1]:
#             count = count + 1
#         else:
#             a = rle_string[i]
#             print(count,rle_string[i])
#             count = 1
#     data.write(str((count,rle_string[i]))+ '\n')
# print(count,rle_string[i])


# data.close()






 
