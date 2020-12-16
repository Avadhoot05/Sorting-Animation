import numpy as np
import cv2 as cv
import random



def display(l,storePix,typ='b'):
	img = np.zeros([600,1200,3],dtype=np.uint8)
	img.fill(0) 

	img = cv.line(img,(15,550),(800,550),(119, 120, 117),1)  #Horizontal 
	img = cv.line(img,(50,0),(50,585),(119, 120, 117),1)     #Vertical

	if typ == 'q':
		img = cv.putText(img,'Quick Sort',(500,30),cv.FONT_HERSHEY_SIMPLEX, 0.7,(214, 255, 102),2,cv.LINE_AA)
	else:
		img = cv.putText(img,'Bubble Sort',(500,30),cv.FONT_HERSHEY_SIMPLEX, 0.7,(214, 255, 102),2,cv.LINE_AA)

	for x in l:
		img = cv.line(img,(storePix[x],548-x),(storePix[x],548),(0,0,255),2)
	cv.imshow('img',img)
	cv.waitKey(1)


def bubble(l,storePix):
	for i in range(len(l)):  	
		flag =0
		for j in range(0, len(l)-i-1):
			if l[j] >l[j+1]:
				flag=1
				storePix[l[j]],storePix[l[j+1]] = storePix[l[j+1]],storePix[l[j]]
				l[j],l[j+1] = l[j+1],l[j]
		
				display(l,storePix)

		if flag ==0:
			break


def quick(l,storePix):

	def quickSort(l,start,end):
		if start <end:
			Pindex = partition(l,start,end)
			quickSort(l,start,Pindex-1)
			quickSort(l,Pindex+1,end)

	def partition(l,start,end):
		piv = l[end]
		pindex =start

		for i in range(start,end):
			if l[i] <= piv:
				storePix[l[i]],storePix[l[pindex]] = storePix[l[pindex]],storePix[l[i]]
				l[i],l[pindex] = l[pindex],l[i]

				display(l,storePix,'q')
				
				pindex+=1


		l[pindex],l[end] = l[end],l[pindex]
		storePix[l[end]],storePix[l[pindex]] = storePix[l[pindex]],storePix[l[end]]
		display(l,storePix,'q')
		return pindex

	quickSort(l,0,len(l)-1)




#list must contain maximum 574 (since we have working area of 1200-51=1149 pixels and each line as thickness=2 hence 1149//2 = 574)
l = []
for i in range(300,49,-2):
	l.append(i)
random.shuffle(l)


#since we have only vertival lines, 
#X pixel will increment by 2 and remain same for start and end of respective line and 
#yEnd is same for each line but yStart pixel according to size of element

x  = 53
storePix = {}

for i in l:
	storePix.update({i:x})    
	x +=4


choice = int(input("Press 1 for bubble sort\nPress 2 for Quick sort\n"))


if choice == 1:
	bubble(l,storePix)
elif choice ==2:
	quick(l,storePix)
else:
	print("Invalid Input")


while cv.waitKey(1) !=ord('q'):
	continue
cv.destroyAllWindows()