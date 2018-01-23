#Author: Eric Lo

#Combine two images used by grayscale to create a 3-D image

#Create the main function
def proj2():
  file=pickAFile()        #Pick the first picture
  pic1=makePicture(file)
  
  file=pickAFile()
  pic2=makePicture(file) #Pick the second picture

  image(pic1,pic2)
  
  
#We have to make sure both images have the same resolution, but I cannot make sure the images are the same
def image(pic1,pic2):
  width1=getWidth(pic1)
  height1=getHeight(pic1)
  
  totalpixs1= (width1*height1)
  
  width2=getWidth (pic2)
  height2=getHeight (pic2)
  
  totalpixs2=(width2*height2)

#Now we type out an "if" statement help us confirm the two pictures have the same resolution
  if (totalpixs1 != totalpixs2):
    print "The pictures you've selected for this program do not have the same resolution. Please select the same pictures for this program "
    return
  
  elif (totalpixs1 == totalpixs2):
    ThreeDimage(pic1,pic2)

#We need to make a function to change the images to red
def redimage(pic1):
  pixs=getPixels(pic1)
  
  for pix in pixs:
    red=getRed(pix)
    green=getGreen(pix)
    blue=getBlue(pix)
    
    grayscale=(red*0.299+green*0.587+green*0.114)
    
    setRed(pix,grayscale)
    setGreen(pix,0)
    setBlue(pix,0)
    
  return (pic1)
  
#The blue image now    
def blueimage(pic2):
  pixs=getPixels(pic2)
  
  for pix in pixs:
    red=getRed(pix)
    green=getGreen(pix)
    blue=getBlue(pix)
    
    grayscale=(red*0.299+green*0.587+green*0.114)
    
    setRed(pix,0)
    setGreen(pix,grayscale)
    setBlue(pix,grayscale)
    
  return (pic2)

#Now I will put these functions in to my 3D function and combine them  
#This function will create the 3-D image
def ThreeDimage(pic1,pic2):

#Turn the images to the colors for 3D  
  redimage(pic1)
  blueimage(pic2)

#Create a third image to put the two images together
  width=getWidth(pic1)
  height=getHeight(pic1)

  pic3=makeEmptyPicture(width,height)

  #Getting all the pixels fromt the pictures  
  for x in range (width):
    for y in range (height):
      pix1=getPixel(pic1,x,y)
      pix2=getPixel(pic2,x,y)
      pix3=getPixel(pic3,x,y)
      
      r1=getRed (pix1)
      g1=getGreen (pix1)
      b1=getBlue (pix1)
      
      r2=getRed(pix2)
      g2=getGreen(pix2)
      b2=getBlue(pix2)
     
   #The combining of the pixels   
      r3 = (r1+r2)/2
      g3 = (g1+g2)/2
      b3 = (b1+g2)/2
      
    #Put these new pixels to third picture
      setRed (pix3, r3)
      setGreen (pix3, g3)
      setBlue (pix3,b3)

#Show and save
  show (pic3)
  
  savefile=pickAFile()
  writePictureTo (pic3,savefile)
      
      
  
  