#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Sun Jun 14 14:58:25 2020

@author: arjun-singh
"""


def allocator(Region,NY_ListPrice,NY_Cap,capacity,time):
    dum_cap = capacity;
    iterator = -1
    OptimisedPrice = 0
    machineList = []
    for i in NY_ListPrice:
      noOfTimes = 0 
      temp = 0 
      temp1 = 0
      iterator += 1
      cap = NY_Cap[iterator];
      price = NY_ListPrice[iterator];
      tempPrice = 0
      Nyregion = {
        "region": Region
      }
      while(dum_cap >= temp1):
        noOfTimes += 1
        temp = noOfTimes * cap
        tempPrice = noOfTimes * price
        temp1 = temp + cap
      if temp > dum_cap:
        continue
      #print(str(noOfTimes)+" units  is used for ",str(UnitNameMapping.get(cap)) , " capacity")
      tuple1 = (UnitNameMapping.get(cap), noOfTimes);
      machineList.append(tuple1)
      dum_cap = dum_cap - temp;
      #print("dumpt_cap   "+str(dum_cap))
      OptimisedPrice += tempPrice
    #print(machineList)
    Nyregion["total_cost"] = OptimisedPrice * time;
    Nyregion["machines"] = machineList;
    return Nyregion
#print(Nyregion)

# Main program starts from here

NY_ListPrice = [1400, 774, 450, 230, 120];
NY_Cap = [160 ,80 ,40 ,20 ,10];
IN_ListPrice = [1300, 413, 140];
IN_Cap = [160, 40, 10];
CH_ListPrice = [1180, 670, 200, 110]
CH_Cap = [160, 80, 20, 10]
UnitNameMapping = {
  10: "Large",
  20: "XLarge",
  40: "2XLarge",
  80: "4XLarge",
  160: "8XLarge"
};
capacity = int(input("Enter the capacity"));
time = int(input("Enter time"));
output_list = []
nyoutput = allocator("New York",NY_ListPrice,NY_Cap,capacity,time)
output_list.append(nyoutput)
inoutput = allocator("India",IN_ListPrice,IN_Cap,capacity,time)
output_list.append(inoutput)
choutput = allocator("China",CH_ListPrice,CH_Cap,capacity,time)
output_list.append(choutput)
output= {"Output": output_list}
print(output)