# Program P1.1 - Area of Square
# Given length of side, calculate area of square
function areaOfSquare()
    print("Enter length of side: 提示: 先空格+回车 再 回答+回车 ")
    s = parse(Int, readline()) # fetch the length typed by the user
    a = s * s # calculate area; store in a
    print("Area of square is $a")
    end

areaOfSquare() # call the function to get the action started 