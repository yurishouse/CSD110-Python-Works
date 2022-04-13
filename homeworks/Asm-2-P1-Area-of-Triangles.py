# Made by Shiina Yuri

# Let the user input the base and height of the first triangle
# creates tr1Bse / tr1Height
tr1Base = eval(input("please input the base of the first triangle: "))
tr1Height = eval(input("please input the height of the first triangle: "))

# Let the user input the base and height of the first triangle
# creates tr2Bse / tr2Height
tr2Base = eval(input("please input the base of the Second triangle: "))
tr2Height = eval(input("please input the height of the Second triangle: "))

# the calculation of tr1Area

tr1Area = ((tr1Base * tr1Height)/2)

# the calculation of tr2Area

tr2Area = ((tr2Base * tr2Height)/2)

# compare the area of tr1Area and tr2Area
if tr1Area == tr2Area:
    print("The two triangles have a equal size")  # print out the result
elif tr1Area > tr2Area:
    print("The first triangle is larger than the second triangle")  # print out the result
else:
    print("The second triangle is larger than the first triangle")  # print out the result
