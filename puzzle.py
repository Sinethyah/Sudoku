def main():

    #naming the file where the puzzle is present
    filename=input('Enter the filename:')

    f=open(filename,'r')
    puzzle=[]

    for line in f:
        puzzle.append([int(val) for val in line.split(",")])

    #sudoku is imported where the validity functions are present
    import sudoku

    print("Current grid")
    sudoku.puzzle_to_string(puzzle)
    print("The columns that are invalid:",sudoku.check_cols(puzzle))
    print("The rows that are invalid:",sudoku.check_rows(puzzle))
    print("The subgrids that are invalid:",sudoku.check_subgrids(puzzle))



    place_num=True

    num_of_moves=0
    num_of_invalid_moves=0



    while place_num:

        
        #asking for input
        var=input("Enter the row/col/number(quit to exit):")
        if var.lower()=='quit':
            ''' if quit then exits the game and prints the invalid moves, total no of moves'''

            sudoku.check_puzzle_complete(puzzle)
            print('You entered',num_of_moves,'in total')
            print('You entered',num_of_invalid_moves,'invalid numbers in total')       
            break

        num=[int(x) for x in var.split(",")]
        num_of_moves+=1

        
            
        num1=num[0]
        num2=num[1]
        num3=num[2]
        
        ''' iterates through the puzzle and places value in the specified position if valid or else not'''
        if num1 in range(0,len(puzzle)) and num2 in range(0,len(puzzle)) and num3 in range(0,len(puzzle)+1):
            original_num=puzzle[num1][num2]
            puzzle[num1][num2]=num3
            #print(sudoku.check_rows(puzzle))
            #print(sudoku.check_cols(puzzle))
            #print(sudoku.check_subgrids(puzzle))
            
            if (sudoku.check_cols(puzzle) or sudoku.check_rows(puzzle) or sudoku.check_subgrids(puzzle)):
                print("Invalid input") 
                num_of_invalid_moves+=1
                puzzle[num1][num2]=original_num
                place_num=True 

        
            else:           
                sudoku.puzzle_to_string(puzzle)

        '''after the puzzle is complete (with or without quit), checks if it is completed or not'''
        all_num=0
        for x in range(len(puzzle)):
            for y in range(len(puzzle)):
                element=puzzle[x][y]
                if element==0:
                    continue
                all_num+=1
        if all_num==81:
            print('The game has ended\nPuzzle is complete')
            print('You entered',num_of_moves,'in total')
            print('You entered',num_of_invalid_moves,'invalid numbers in total')
            break
            

                            


                        
########### main function##############

if __name__=='__main__':
    main()


