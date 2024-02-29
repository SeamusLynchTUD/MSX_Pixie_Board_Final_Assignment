import random

fairyX1, fairyX2, fairyX3, fairyX4, fairyX5, fairyX6, fairyX7, fairyX8 = 960, 960, 960, 960, 960, 960, 960, 960
fairyY1, fairyY2, fairyY3, fairyY4, fairyY5, fairyY6, fairyY7, fairyY8 = 540, 540, 540, 540, 540, 540, 540, 540
fairyDirX1, fairyDirX2, fairyDirX3, fairyDirX4, fairyDirX5, fairyDirX6, fairyDirX7, fairyDirX8 = random.randint(1, 5), random.randint(-5, -1), random.randint(1, 5), random.randint(-5, -1), random.randint(1, 5), random.randint(-5, -1), random.randint(1, 5), random.randint(-5, -1)
fairyDirY1, fairyDirY2, fairyDirY3, fairyDirY4, fairyDirY5, fairyDirY6, fairyDirY7, fairyDirY8 = random.randint(1, 5), random.randint(1, 5), random.randint(-5, -1), random.randint(-5, -1), random.randint(1, 5), random.randint(1, 5), random.randint(-5, -1), random.randint(-5, -1)
fairyWingY1, fairyWingY2, fairyWingY3, fairyWingY4, fairyWingY5, fairyWingY6, fairyWingY7, fairyWingY8 = 0, 0, 0, 0, 0, 0, 0, 0
fairyWingDir1, fairyWingDir2, fairyWingDir3, fairyWingDir4, fairyWingDir5, fairyWingDir6, fairyWingDir7, fairyWingDir8 = 1, 1, 1, 1, 1, 1, 1, 1
fairyXList = [fairyX1, fairyX2, fairyX3, fairyX4, fairyX5, fairyX6, fairyX7, fairyX8]
fairyYList = [fairyY1, fairyY2, fairyY3, fairyY4, fairyY5, fairyY6, fairyY7, fairyY8]
fairyDirXList = [fairyDirX1, fairyDirX2, fairyDirX3, fairyDirX4, fairyDirX5, fairyDirX6, fairyDirX7, fairyDirX8]
fairyDirYList = [fairyDirY1, fairyDirY2, fairyDirY3, fairyDirY4, fairyDirY5, fairyDirY6, fairyDirY7, fairyDirY8]
fairyWingYList = [fairyWingY1, fairyWingY2, fairyWingY3, fairyWingY4, fairyWingY5, fairyWingY6, fairyWingY7, fairyWingY8]
fairyWingDirList = [fairyWingDir1, fairyWingDir2, fairyWingDir3, fairyWingDir4, fairyWingDir5, fairyWingDir6, fairyWingDir7, fairyWingDir8]

x1, x2, x3, x4, x5, x6, x7 = -33, -110, -187, -264, -341, -418, -495
x8, x9, x10, x11 = -92, -236, -380, -524
x12, x13, x14 = 1920, 1920, 1920
x15 = 1920
x16, x17, x18, x19 = -92, -92, -236, -236

def setup():
    size(1920, 1080)
    colorMode(HSB)
    fullScreen()

def draw():
    global x1, x2, x3, x4, x5, x6, x7, x8, x9, x10, x11, x12, x13, x14, x15, x16, x17, x18, x19, x20, x21, x22
    background(0, 0, 200)
    fill(110, 200, 180)
    noStroke()
    #rect(581, 235, 758, 610)
    rect(391.5, 82.5, 1137, 915)
    fill(0, 0, 255)
    
    rect(1105.5, 147.5, 82, 3)
    rect(1105.5, 147.5, 3, 102)
    rect(958.5, 246.5, 148, 3)
    rect(958.5, 246.5, 3, 215)
    rect(958.5, 458.5, 228, 3)
    rect(1185.5, 147.5, 3, 314)
    
    rect(404.5, 496.5, 175, 3)
    rect(404.5, 496.5, 3, 45)
    rect(404.5, 539.5, 32, 3)
    rect(435.5, 539.5, 3, 29)
    rect(435.5, 567.5, 143, 3)
    rect(577.5, 496.5, 3, 74)
    
    rect(582.5, 496.5, 411, 3)
    rect(582.5, 496.5, 3, 74)
    rect(582.5, 567.5, 411, 3)
    rect(991.5, 496.5, 3, 74)
    
    rect(404.5, 577.5, 179, 3)
    rect(404.5, 577.5, 3, 102)
    rect(404.5, 677.5, 179, 3)
    rect(581.5, 577.5, 3, 102)
    
    rect(591.5, 577.5, 126, 3)
    rect(591.5, 577.5, 3, 102)
    rect(591.5, 677.5, 12, 3)
    rect(601.5, 677.5, 3, 21)
    rect(601.5, 696.5, 114, 3)
    rect(715.5, 577.5, 3, 122)
    
    rect(472.5, 687.5, 121, 3)
    rect(472.5, 687.5, 3, 35)
    rect(404.5, 720.5, 70, 3)
    rect(404.5, 720.5, 3, 172)
    rect(404.5, 890.5, 30, 3)
    rect(432.5, 890.5, 3, 26)
    rect(432.5, 914.5, 223, 3)
    rect(591.5, 687.5, 3, 22)
    rect(591.5, 707.5, 64, 3)
    rect(653.5, 707.5, 3, 210)
    rect(725.5, 577.5, 158, 3)
    rect(725.5, 577.5, 3, 131)
    rect(663.5, 707.5, 65, 3)
    rect(663.5, 707.5, 3, 253)
    rect(663.5, 958.5, 283, 3)
    rect(881.5, 577.5, 3, 154)
    rect(881.5, 729.5, 64, 3)
    rect(943.5, 729.5, 3, 230)
    
    rect(952.5, 653.5, 270, 3)
    rect(952.5, 653.5, 3, 120)
    rect(952.5, 771.5, 111, 3)
    rect(1061.5, 757.5, 3, 16)
    rect(1061.5, 757.5, 162, 3)
    rect(1221.5, 653.5, 3, 106)
    
    rect(1071.5, 767.5, 137, 3)
    rect(1071.5, 767.5, 3, 59)
    rect(952.5, 823.5, 120, 3)
    rect(952.5, 823.5, 3, 136)
    rect(952.5, 958.5, 257, 3)
    rect(1206.5, 767.5, 3, 191)
    
    rect(1216.5, 766.5, 143, 3)
    rect(1216.5, 766.5, 3, 160)
    rect(1216.5, 924.5, 30, 3)
    rect(1244.5, 924.5, 3, 35)
    rect(1244.5, 958.5, 217, 3)
    rect(1357.5, 766.5, 3, 105)
    rect(1357.5, 869.5, 104, 3)
    rect(1459.5, 869.5, 3, 92)
    
    rect(1396.5, 417.5, 58, 3)
    rect(1396.5, 417.5, 3, 341)
    rect(1366.5, 756.5, 32, 3)
    rect(1366.5, 756.5, 3, 106)
    rect(1366.5, 861.5, 97, 3)
    rect(1451.5, 417.5, 3, 218)
    rect(1451.5, 633.5, 12, 3)
    rect(1461.5, 633.5, 3, 230)
    
    rect(1251.5, 180.5, 206, 2)
    rect(1251.5, 180.5, 2, 210)
    rect(1251.5, 388.5, 227, 2)
    rect(1455.5, 180.5, 2, 71)
    rect(1455.5, 249.5, 23, 2)
    rect(1476.5, 249.5, 2, 140)

    if x1 < 911.5:
        x1 += 1
    if x2 < 834.5:
        x2 += 1
    if x3 < 757.5:
        x3 += 1
    if x4 < 680.5:
        x4 += 1
    if x5 < 603.5:
        x5 += 1
    if x6 < 526.5:
        x6 += 1
    if x7 < 449.5:
        x7 += 1
    if x8 < 896.5:
        x8 += 1
    if x9 < 752.5:
        x9 += 1
    if x10 < 608.5:
        x10 += 1
    if x11 < 446.5:
        x11 += 1
    if x12 > 1003.5:
        x12 -= 1
    if x13 > 1003.5:
        x13 -= 1
    if x14 > 1003.5:
        x14 -= 1
    if x15 > 1027.5:
        x15 -= 1
    if x16 < 835.5:
        x16 += 1
    if x17 < 835.5:
        x17 += 1
    if x18 < 693.5:
        x18 += 1
    if x19 < 693.5:
        x19 += 1

    fill(0)
    rect(x1, 100, 33, 322)
    rect(x2, 100, 33, 322)
    rect(x3, 100, 33, 322)
    rect(x4, 100, 33, 322)
    rect(x5, 100, 33, 322)
    rect(x6, 100, 33, 322)
    rect(x7, 100, 33, 322)
    rect(x8, 508.5, 92, 35)
    rect(x9, 508.5, 92, 35)
    rect(x10, 508.5, 92, 35)
    rect(x11, 508.5, 92, 35)
    rect(x11, 508.5, 92, 35)
    rect(x12, 270.5, 92, 35)
    rect(x13, 337.5, 92, 35)
    rect(x14, 404.5, 92, 35)
    rect(x15, 685.5, 184, 62)
    rect(x16, 747.5, 92, 35)
    rect(x17, 817.5, 92, 35)
    rect(x18, 747.5, 92, 35)
    rect(x19, 817.5, 92, 35)
    
    for i in range(8):
        ##wings##
        fill(255)
        ellipse(fairyXList[i]-25, (fairyYList[i] + fairyWingYList[i])-15, 50, 25)
        ellipse(fairyXList[i]+25, (fairyYList[i] + fairyWingYList[i])-15, 50, 25)
    
        ##fairyball##
        fill(fairyXList[i] / 8, 255, 255)
        circle(fairyXList[i], fairyYList[i], 50)
        fill(fairyXList[i] / 8, 255, 255, 50)
        ellipse(fairyXList[i], fairyYList[i] + 100, 75, 25)
    
        ##movement##
        fairyXList[i] += fairyDirXList[i]
        fairyYList[i] += fairyDirYList[i]
        fairyWingYList[i] += fairyWingDirList[i]
        if fairyXList[i] >= 1528.5:
            fairyDirXList[i] = random.randint(-5, -1)
        if fairyXList[i] <= 391.5:
            fairyDirXList[i] = random.randint(1, 5)
        if fairyYList[i] >= 897.5:
            fairyDirYList[i] = random.randint(-5, -1)
        if fairyYList[i] <= -17.5:
            fairyDirYList[i] = random.randint(1, 5)
    
        ##wingflaps##
        if fairyWingYList[i] >= 25:
            fairyWingDirList[i] = -12.5
        if fairyWingYList[i] <= 25 :
            fairyWingDirList[i] = 12.5
