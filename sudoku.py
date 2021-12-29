'''
Name: Kaniz Fathma Sinethyah
Comments: Done using 9X9 grid
'''


#------------------------------------------------------------------#
# provided function - do NOT remove or change

def load_puzzle(filename):

    ''' Reads a sudoku puzzle from the text file 'filename' in the current directory. 
        Returns a list of lists of integers that represents the game.
            load_puzzle(filename:str) -> str[str[int]]
        Empty cells in the game are denoted by 0s in the file (and the output list)
    '''
    puzzle = [] 
    with open('puzzle.csv', "r") as f:
        for line in f:
            puzzle.append( [int(val) for val in line.split(",")] )
        
    return puzzle

    
#------------------------------------------------------------------#
#------------------------------------------------------------------#

#printing the puzzle
def puzzle_to_string(puzzle):

    '''dividing the puzzle into groups of 3X3 using gridlines and printing the entire puzzle'''

    for i in range(len(puzzle)):
        if i%3==0 and i!=0:
            print('------+--------+--------')

        for j in range(len(puzzle[0])):
            if j%3==0 and j!=0:
                print("|",end="  ")

            

            if j==len(puzzle[0])-1:
                print(puzzle[i][j]) 
            else:
                print(str(puzzle[i][j]),end=" ")

#validate rows

def check_rows(puzzle):

    ''' checking rows and returning invalid rows if found'''
    
    invalid_rows=[]

    for i in range(len(puzzle)):
        already_seen=[]

        for j in range(len(puzzle)):
            element=puzzle[i][j]

            if element==0:
                continue

            if element in already_seen:
                invalid_rows.append(i)
                break
            else:
                already_seen.append(element)

    return invalid_rows

#validate columns

def check_cols(puzzle):
    ''' checking columns, return invalid cols if invalid cols found'''
    invalid_cols=[]


    for i in range(len(puzzle)):
        already_seen=[]
        
        for j in range(len(puzzle)):
            element=puzzle[j][i]

            if element==0:
                continue

            if element in already_seen:
                invalid_cols.append(i)
            else:
                already_seen.append(element)
        

    return invalid_cols

#validate subgrids

def check_subgrids(puzzle):
    ''' checking in boxes of 3X3 for validating'''
    invalid_subgrids=[]

    store=-1

    for i in range(0,len(puzzle),3):
        for j in range(0,len(puzzle),3):
            list1=[]

            store+=1

            for x in range(i,i+3):
                for y in range(j,j+3):
                    element=puzzle[x][y]
                    if element==0:
                        continue

                    if element in list1:
                        invalid_subgrids.append(store)

                    else:
                        list1.append(element)
    
    return invalid_subgrids

#keep a track of whether the puzzle is complete or not, going to be used in puzzle.py


def check_puzzle_complete(puzzle):

    ''' doing it by keeping track of 0s'''
    
    zeroes_present_puzzle_incomplete=0
    for x in range(len(puzzle)):
        for y in range(len(puzzle)):
            element=puzzle[x][y]
            if element==0:
                zeroes_present_puzzle_incomplete+=1
    if zeroes_present_puzzle_incomplete!=0:
        print("The game has ended\nThe puzzle is NOT completed")               
    else:
        print("The game is over\nThe puzzle is complete")
    


                    
                    




#------------------------------------------------------------------#
#------------------------------------------------------------------#



#------------------------------------------------------------------#
# Your "program" is driven by the main method
# Modify as needed to test your functions
def main():
    puzzle = load_puzzle('puzzle.csv')   
    puzzle_to_string(puzzle)
    print("The rows that are invalid:",check_rows(puzzle))
    print("The cols that are invalid:",check_cols(puzzle))
    print("The subgrids that are invalid are:",check_subgrids(puzzle))




#------------------------------------------------------------------#
# Guard for main function - do NOT remove or change
if __name__ == "__main__":
    main()



