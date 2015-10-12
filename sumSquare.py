def sumOverList(squares):
    SUM = 0
    for i in range(len(squares)):
        SUM = SUM + squares[i]
    return SUM

squares = []
notSquares = []
for i in range(101):
    notSquares.append(i)
    squares.append(i*i)

squaresSum = sumOverList(squares)
notSquaresSum = sumOverList(notSquares)
notSquaresSum = notSquaresSum * notSquaresSum
diff = notSquaresSum - squaresSum
print squares
print diff
