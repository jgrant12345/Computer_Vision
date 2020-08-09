from PIL import Image
import numpy as np
import os
from skimage import color
from skimage import io
from PIL import Image, ImageOps
import _csv



#NOTES:
#Stuff to Fill out
#Image Dimensions
WidthofPicture = 60
HeightOfPicture = 60

#Name of Path for folder Here
PATH = 'NameOfPathGoesHere'




#Put Name of CSV Here
CSV_NAME = 'NameOfCSVGoesHere.csv'

#No more need to fill out

#Number of Pixels to fill label
NumberOfPixels = WidthofPicture*HeightOfPicture


label = 0
pixelcount = 1
csv_array = []
#Make Headers
header = []
header.append('Label')
for i in range(NumberOfPixels):
    header.append(i)
    pixelcount = pixelcount + 1

with open(CSV_NAME,'a+') as f:
    theWriter = _csv.writer(f,delimiter = ',')
    theWriter.writerow(header)
    

for element in os.listdir(PATH):
    for element2 in os.listdir(os.path.join(PATH,element)):
        # take the image and resize it, turn it into grayscale and convert it into an array
        print(element)
        im1 = Image.open(PATH +'/' + element+ '/' + element2).convert('L')
        resize = im1.resize((WidthofPicture, HeightOfPicture))
        array= np.array(resize)
        array = np.array(array, dtype='int')


     
          #add pixel values to an excel spreadsheet
        csv_array = []
        csv_array.append(label)
        for index1 in range(len(array)): #assuming picture is the same length and width
            for index2 in range(len(array[0])): #length of a single sub array
                print(array[index2][index1])
                csv_array.append(array[index1][index2])
        with open(CSV_NAME,'a+') as f:
            theWriter = _csv.writer(f,delimiter = ',')
            theWriter.writerow(csv_array)
    label = label + 1  
  

    
               
                   


                
        
               
