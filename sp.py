import cv2
import matplotlib.pyplot as plt
import random

image = list( {"pic/t" + str(i) +".jpg" for i in range(1,48) } )
random.shuffle(image)
image = image[:27]

def display(s,ilist):
    #To Display groups of image in console by using cv2 a subplot 
    
    print("##########################Group{0} ##############################################".format(s))
    for i in range(len(ilist)):
        img = cv2.imread(ilist[i],1)
        img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
        plt.subplot(4,3,i+1)
        plt.imshow(img)
        plt.xticks([])
        plt.yticks([])
    plt.show()
    
    return 1

def MindArrange(p,a):
    #This function help to divide list of image in groups to do calculation and 
    #its call display function to display 
    g0,g1,g2 = [],[],[]
    for i in range(len(image)):
        if i%3 == 0:
            g0.append(image[i])
        elif i%3 == 1:
            g1.append(image[i])

        else:
            g2.append(image[i])
    
    print("$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$$\n")
    ready = display("A",g0) # its help  display images  and ready flag tells display is complited
    ready = display("B",g1)
    ready = display("C",g2)
    while ready and True:
        #its take input from user to ask which group his/her slected image is present 
        groupOp = input("Please Enter you  group name as A,B,C:") 
        # validing correct option netered by user
        if groupOp in list("ABCabc"):
            break
        else :
            print("Please enter valid Group name")
    return (groupOp,g0,g1,g2)
    
print("Think of any one image from below three groups (A, B, C). \nNow provide the group name in which the image you thought is present. \nImages will be shuffled now and ans the same ques again.\nAgain the images will be shuffled and ans the same ques.\n") 
print("Magic! The image you thought will be displayed")

for p in range(3):
    
    image = MindArrange(p,image)
    op = image[0].upper()
    #putting the seleted group of image in between list
    if op == 'A':
        image = image[2] + image[1] + image[3]
    elif op == 'B':
        image = image[3] + image[2] + image[1]
    elif op == 'C':
        image = image[2] + image[3] +image[1]
        
#Displaying middle image  of list of image after calculation 
img = cv2.imread(image[len(image)//2],1)
img = cv2.cvtColor(img , cv2.COLOR_BGR2RGB)
plt.subplot(1,1,1)
print("Here you Selected ")
plt.imshow(img)
plt.xticks([])
plt.yticks([])

