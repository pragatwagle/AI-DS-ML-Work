# Program to sum the rows of an input matrix.
# Date: 06/27/2021
# Author: Pragat Wagle

def in_matrix():
    rows = int(input("Enter the number of rows: "))
    columns = int(input("\nEnter the number of columns: "))
    mxn = [rows, columns]
    mx = []
    for i in range(rows):
      row = []
      for j in range(columns):
        element = int(input("Enter next element of row " + str(i) + ": "))
        row.append(element)
      mx.append(row)
    return mx

def print_matrix(mx):
    print("Input matrix:")
    for i in mx:
        for j in i:
            print(j, end ="\t")
            if(j==i[len(i)-1]):
                print("\n")
def sum_rows(mx):
    sumOfRows = []
    for i in mx:
        sumOfRow = 0
        for j in i:
            sumOfRow += int(j)
        sumOfRows.append(sumOfRow)
    return sumOfRows

def main():
    print("Program to sum the rows of an input matrix.\n")
    mx = in_matrix()
    print_matrix(mx)
    sumOfRows = sum_rows(mx)
    row = 0
    for i in sumOfRows:
        print("Sum of numbers in row " + str(row) + " is " + str(i))
        row += 1
main()

















