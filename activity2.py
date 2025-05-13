#Basic
def basic():
  for x in range (1,151):
    print(x)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")

#Multiple of five  
def multiple():
  for x in range (5,1001,5):
    print(x)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")

#Counting,My Way
def counting():
  for x in range (1,1001):
    numbType = '' if x %  5 else 'Lucky 5' if x %10 else 'Twice the charm'
    print(x,numbType)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")  
  
#Woah Large Sum
def largesum():
  oddnm=0
  for x in range (1,5000001):
      if x%2==0:
        oddnm+=x
  print(oddnm)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")

#Countdown by fours
def countfour():
  for x in range (2018,0,-4):
    print(x)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")
  
#Flexible Counter
def flex():
  lowNum = 2
  highNum = 9
  mult = 3
  
  for x in range(lowNum,highNum+1):
    if(x%mult==0):
      print(x)
  print("INF225_RelOps_Lopena_Ferjhon_HrgYnMl091Ifs2225")
flex()