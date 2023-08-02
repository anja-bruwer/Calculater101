class my_class(object):
    pass

while True:
   print("1. Addition")
   print("2. Subtraction")
   print("3. Multiplication")
   print("4. Division")
   print("5. Exit")
   ###diffferent options that can be used for caluculations

   print("\nEnter Your Choice (1-5): ")
   ###input the option chosen

   answ = int(input())

   if answ>=1 and answ<=4:
      print("\nEnter Two Numbers: ")
      numOne = float(input())
      numTwo = float(input())
      ### if on of the option is chosen ask for the two numbers for the calculations 

   if answ==1:
      res = numOne + numTwo
      print("\nResult =", res)
      ### if addition is chosen the two numbers will be + together 

   elif answ==2:
      res = numOne - numTwo
      print("\nResult =", res)
      ### if subtraction is chosen the two numbers will be - together 

   elif answ==3:
      res = numOne * numTwo
      print("\nResult =", res)
      ### if multiplution is chosen the two numbers will be x together 

   elif answ==4:
      res = numOne / numTwo
      print("\nResult =", res)
      ### if division is chosen the two numbers will be / 

   elif answ==5:
      break
        ### if exit is chose the program will end

   else:
      print("\nInvalid Input!..Try Again!")
      ## if unvalid option is chosen error message will show

   print("\n---Next Calculation---")
   print("------------------------")  
   ### shows start of next calculation


