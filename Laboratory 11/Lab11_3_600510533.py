#!/usr/bin/env Python3
# จักรกฤษณ์ บุญเนตร
# 600510533
# Lab 11
# Problem 3
# 204111 Sec 01A

def main():
    board = [[2, 7, 6],
             [9, 5, 1],
             [4, 3, 8]]

    print(is_magic_square(board))


def is_magic_square(board):
    for i in range(len(board)):
        for j in range(len(board[0])):
            num_access = board[i][j] # ตัวเลขที่เข้าถึง
            for x in range(len(board)): # จะหาต
                for y in range(len(board[0])):
                    # แถวกับหลักไม่เท่ากัน      # ถ้ามันซ้ำกับ board
                    if x != i and j != y and num_access == board[x][y]:
                        return False

                    if num_access <= 0 or num_access > len(board) ** 2 : # เช็คช่วงที่มีเลขอยู่ได้ เช่น board = 3 (3*3) จะมีเลขได้ไม่เกิน 9 และไม่ซ้ำกัน
                        return False

                    if len(board) != len(board[i]): # จำนวณหลักไม่เท่าจำนวณแถว
                        return False


    sum_i = [0] * len(board) # แต่ละตัวของ list ก็คือ แถวนั่นเอง
    sum_j = [0] * len(board[0]) # แต่ละตัวของ list ใน list อีกที นั่นคือ หลักนั่นเอง
    sum_cross_l = 0
    sum_cross_r = 0
    for i in range(len(board)):
        for j in range(len(board[0])):
            sum_i[i] += board[i][j] # ผลบวกของแถว([i] คือหลายๆแถว)
            sum_j[j] += board[i][j] # ผลบวกของคอลัม([j] คือหลายๆคอลัม)
            if i == j:
                sum_cross_l += board[i][j] # ผลรวมของมุมเฉียงซ้ายไปขวา
            if i + j == len(board) -1:
                sum_cross_r += board[i][j] # ผลรวมของมุมเฉียงขวาไปซ้าย

    for i in range(len(board)):
        for j in range(len(board[0])): # ดูตัวที่ไม่ซ้ำกัน
            if i != j and sum_i[i] != sum_i[j]:
                return False

    for i in range(len(board)): # ดูตัวที่ไม่ซ้ำกัน
        for j in range(len(board[0])):
            if i != j and sum_j[i] != sum_j[j]:
                return False


    if sum_i == sum_j and sum_cross_r == sum_cross_l and sum_i[0] == sum_cross_r and sum_i[0] == sum_cross_l: # เช็คจำนวณทุกแถวว่าเท่ากันมั้ย
        return True
    else:
        return False



if __name__ == '__main__':
    main()