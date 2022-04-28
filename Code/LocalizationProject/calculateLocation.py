# -*- coding: utf-8 -*-
"""
Created on Tue Apr 19 14:38:18 2022

@author: 13863
"""

import math
import time    

#This function takes in the DOA values from two microphones, and calculates coordinates
#for the location of the sound RELATIVE TO THE TOP MICROPHONE (The top microphone is regarded as coordinate point (0,0))
#Parameters: distance_btw_mics is the distance (whatever unit chosen will reflect on the output - if distance is in meters, 
#the output coordinate of the sound location will also be in meters)
#Parameters: DOA1 is the DOA value taken from the TOP microphone
#Parameters: DOA2 is the DOA value taken from the BOTTOM microphone

def calculate_distance(distance_btw_mics, DOA1, DOA2):
    #Function assumes DOA1 comes from top microphone, and DOA2 from bottom microphone
    #If erroneous DOA values are inputted into the function, the distances calculated will be negative
    #In the case that this ^^ occurs, the function will not output anything at all to the text file
    #If valid DOA values are inputted, function will output the calculated coordinate to the text file named 'CoordinateOutputs.txt'
    #(Uncomment all print statements below to see how the function progresses through calculations)
    
    
    #print("DOA of top microphone is:", DOA1, "- DOA of bottom microphone is:", DOA2)

    inner_angle1 = calculate_inner_angle("top", DOA1)
    #print("inner angle top mic is: ", inner_angle1)

    inner_angle2 = calculate_inner_angle("bottom", DOA2)
    #print("inner angle bottom mic is: ", inner_angle2)

    outer_angle = 180 - inner_angle1 - inner_angle2
    #print("outer angle is: ", outer_angle)

    distance_from_mic1 = (distance_btw_mics * math.sin(math.radians(inner_angle2))) / math.sin(math.radians(outer_angle))
    distance_from_mic2 = (distance_btw_mics * math.sin(math.radians(inner_angle1))) / math.sin(math.radians(outer_angle))

    #print("distance from top mic is ", distance_from_mic1)
    #print("distance from bottom mic is ", distance_from_mic2)
    
    if(distance_from_mic1 > 0 and distance_from_mic2 > 0):
        
        if inner_angle1 >= 90 and DOA1 > 270:               #if sound is northeast of mic 1 (scenario 1)
            angleD = 180 - inner_angle1                                                                                 # D = 90 - B
            angleE = 180 - 90 - angleD                                                                                  # E = 180 - 90 - D
            distanceNorth = math.sin(math.radians(angleE)) * distance_from_mic1                                         # e = sin(E) * c
            distanceEast = math.sin(math.radians(angleD)) * distance_from_mic1                                          # d = sin(D) * c
            #print("Sound is ", distanceNorth, " meters north and ", distanceEast, " meters east of Mic 1\n")
            coordinateString = str(distanceEast) + ', ' + str(distanceNorth)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

        elif inner_angle1 >= 90 and 270 > DOA1 >= 180:       #if sound is northwest of mic 1 (scenario 3)  
            angleD = 180 - inner_angle1
            angleE = 180 - 90 - angleD
            distanceNorth = math.sin(math.radians(angleE)) * distance_from_mic1
            distanceWest = math.sin(math.radians(angleD)) * distance_from_mic1
            #print("Sound is ", distanceNorth, " meters north and ", distanceWest, " meters west of Mic 1\n")
            coordinateString = str(distanceWest * -1) + ', ' + str(distanceNorth)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

        elif inner_angle1 < 90 and inner_angle2 < 90 and DOA1 < 90:       #if sound is southeast of mic 1 and northeast of mic 2 (scenario 2)
            angleD = 90 - inner_angle1
            angleE = 180 - 90 - angleD
            distanceEast = math.sin(math.radians(angleE)) * distance_from_mic1
            distanceSouth = math.sin(math.radians(angleD)) * distance_from_mic1
            #print("Sound is ", distanceSouth, " meters south and ", distanceEast, " meters east of Mic 1\n")
            coordinateString = str(distanceEast) + ', ' + str(distanceSouth * -1)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

        elif inner_angle1 < 90 and inner_angle2 < 90 and DOA1 > 90:       #if sound is southwest of mic 1 and northwest of mic 2 (scenario 4)
            angleD = 90 - inner_angle1
            angleE = 180 - 90 - angleD
            distanceWest = math.sin(math.radians(angleE)) * distance_from_mic1
            distanceSouth = math.sin(math.radians(angleD)) * distance_from_mic1
            #print("Sound is ", distanceSouth, " meters south and ", distanceWest, " meters west of Mic 1\n")
            coordinateString = str(distanceWest * -1) + ', ' + str(distanceSouth * -1)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

        elif inner_angle2 >= 90 and DOA1 > 90:                          #if sound is southwest of mic 2 (scenario 5)
            angleD = 90 - inner_angle1
            angleE = 180 - 90 - angleD
            distanceWest = math.sin(math.radians(angleE)) * distance_from_mic1
            distanceSouth = math.sin(math.radians(angleD)) * distance_from_mic1
            #print("Sound is ", distanceSouth, " meters south and ", distanceWest, " meters west of Mic 1\n")
            coordinateString = str(distanceWest * -1) + ', ' + str(distanceSouth * -1)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

        elif inner_angle2 >= 90 and DOA1 < 90:                          #if sound is southeast of mic 2 (scenario 6)
            angleD = 90 - inner_angle1
            angleE = 180 - 90 - angleD
            distanceEast = math.sin(math.radians(angleE)) * distance_from_mic1
            distanceSouth = math.sin(math.radians(angleD)) * distance_from_mic1
            #print("Sound is ", distanceSouth, " meters south and ", distanceEast, " meters east of Mic 1\n")
            coordinateString = str(distanceEast) + ', ' + str(distanceSouth * -1)
            print (coordinateString)
            with open('CoordinateOutputs.txt', 'w') as f:
                f.write(coordinateString)

    


#This function calculates the inner angle for a mic given the DOA that is taken from it.
#Different calculation based on whether the mic is the top or bottom mic

def calculate_inner_angle(top_or_bottom, DOA):
    if top_or_bottom == "top":
        if DOA > 270:                       #if sound is in 4th quadrant
            return 450 - DOA
        elif 270 > DOA >= 180:              #if sound is in 3rd quadrant
            return DOA - 90
        elif 180 > DOA > 90:                #if sound is in 2nd quadrant
            return DOA - 90
        elif 90 > DOA >= 0:                 #if sound is in 1st quadrant
            return 90 - DOA
        elif DOA == 270:
            return "Angle from top mic is 270: sound is straight up from mic"
        elif DOA == 90:
            return "Angle from top mic is 90: sound is straight down from mic"

    elif top_or_bottom == "bottom":
        if DOA > 270:                       #if sound is in 4th quadrant
            return DOA - 270
        elif 270 > DOA >= 180:              #if sound is in 3rd quadrant
            return 270 - DOA
        elif 180 > DOA > 90:                #if sound is in 2nd quadrant
            return 270 - DOA
        elif 90 > DOA >= 0:                 #if sound is in 1st quadrant
            return DOA + 90
        elif DOA == 270:
            return "Angle from bottom mic is 270: sound is straight up from mic"
        elif DOA == 90:
            return "Angle from bottom mic is 90: sound is straight down from mic"

#This function loops the calculation of sound location indefinetly
#It will send output values for location to the text file in intervals of seconds defined by the time.sleep function
#DOA values for the microphones should be calculated within the while loop
def loop_localization_calculation():
    file1 = open("CoordinateInputs.txt", "r")
    myline = file1.readline()
    
    while myline:
        chunks = myline.split(',')
        dist_btw_mics = int(chunks[0])
        DOA_top = int(chunks[1])
        DOA_bot = int(chunks[2])
        calculate_distance(dist_btw_mics, DOA_top, DOA_bot)
        myline = file1.readline()
        time.sleep(0.5)
    #while (1):
        #calculatedDOA1 = TBD: calculate DOA for top microphone and assign it to this variable
        #calculatedDOA2 = TBD: calculate DOA for bottom microphone and assign it to this variable
        
        #input the calculated DOA values and the distance between the mics in the following function call:
        #calculate_distance(distance_btw_mics, calculatedDOA1, calculatedDOA2) 
        
     #   time.sleep(5) #calculate a location for sound every 5 seconds (change the number of seconds as you wish)
        
loop_localization_calculation()





#Testing cases below:
    
#print(calculate_inner_angle("top", 280))
#print(calculate_inner_angle("top", 230))
#print(calculate_inner_angle("top", 150))
#print(calculate_inner_angle("top", 30))
#print(calculate_inner_angle("top", 270))
#print(calculate_inner_angle("top", 90))

#print(calculate_inner_angle("bottom", 280))
#print(calculate_inner_angle("bottom", 230))
#print(calculate_inner_angle("bottom", 150))
#print(calculate_inner_angle("bottom", 30))
#print(calculate_inner_angle("bottom", 270))
#print(calculate_inner_angle("bottom", 90))

#calculate_distance(2, 300, 290)               #scenario 1: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 301, 289)               # 8 simulated values for scenario 1
#calculate_distance(2, 302, 288)
#calculate_distance(2, 303, 287)
#calculate_distance(2, 330, 310)
#calculate_distance(2, 329, 309)
#calculate_distance(2, 331, 305)
#calculate_distance(2, 345, 300)

#calculate_distance(2, 30, 330)                #scenario 2: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 31, 320)                # 8 simulated values for scenario 2
#calculate_distance(2, 33, 315)
#calculate_distance(2, 35, 310)
#calculate_distance(2, 45, 330)
#calculate_distance(2, 42, 306)
#calculate_distance(2, 24, 340)
#calculate_distance(2, 20, 290)

#calculate_distance(2, 240, 260)               #scenario 3: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 195, 230)
#calculate_distance(2, 200, 220)
#calculate_distance(2, 225, 240)
#calculate_distance(2, 220, 255)
#calculate_distance(2, 215, 235)
#calculate_distance(2, 245, 250)
#calculate_distance(2, 190, 210)

#calculate_distance(2, 150, 190)               #scenario 4: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 145, 195)
#calculate_distance(2, 140, 200)  
#calculate_distance(2, 135, 205)
#calculate_distance(2, 130, 210)
#calculate_distance(2, 125, 215)
#calculate_distance(2, 120, 220)
#calculate_distance(2, 115, 225)
     
#calculate_distance(2, 120, 160)               #scenario 5: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 115, 165)
#calculate_distance(2, 110, 170)
#calculate_distance(2, 105, 155)
#calculate_distance(2, 100, 150)
#calculate_distance(2, 95, 145)
#calculate_distance(2, 125, 143)
#calculate_distance(2, 130, 138)

#calculate_distance(2, 70, 45)                 #scenario 6: all distances (b, c, d, e) check out on calculator, correct output to text file
#calculate_distance(2, 75, 50)
#calculate_distance(2, 80, 55)
#calculate_distance(2, 65, 40)
#calculate_distance(2, 60, 35)
#calculate_distance(2, 55, 30)
#calculate_distance(2, 50, 25)
#calculate_distance(2, 45, 20)


#calculate_distance(2, 240, 220)               #invalid DOA values, causes lines to diverge and never intersect, results in negative distance values                
#calculate_distance(2, 110, 100)               #invalid DOA values, causes lines to diverge and never intersect, results in negative distance values (maybe we just don't show results if they are negative)