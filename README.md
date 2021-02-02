# webcam

made a pdf scanner using python,Ip-Cam app,and also used few image processing technique.

This Pdf scanner is made using ip webcam and few  image processing techniques. Technology Stack used: Python, openCV.
Features of pdf scanner:
1. Connected the phone camera with the laptop using python.
2. Used black and white conversion (if the image is normal and readable)
3. Used adaptive threshoding(if the image is unclear and not readable)
Additional features added:
1. The first feature I have added is whitening the pixels, we can cut a section of rectangular area of the image.
It is useful  when we don’t want some part of the scanned image(Text) .we can simply enter the value of the coordinates of the pixel values of the required  area of the section that we don’t want to be included…The area of the section may be as small as a letter or as large as the whole image.  

2.   The second feature I have included is, if we want a particular outline of a image to give description about the edges in the scanned image and erasing all the noise around the surroundings we can use the Canny function in OpenCv module. It detects the edges of the (scanned) image.
For example if we scan a photo that has some table and we need to show the outline of the tabular form, we can use canny function.
 If we need any particular shape to be focused, we can use this function.
           A USE OF WHITENING OF THE PIXELS:   We can put some text in between the scanned image with or without whitening the respective pixels by using  the function cv2.putText() .  
