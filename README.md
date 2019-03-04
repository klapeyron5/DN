CV algorithm which predicts the angle of car number on the photo. The car number must have angle variance [-15,15] from the horizon and occupy a significant place on the photo (minimum is around 0.25 of the image area). Negative angle means clockwise rotation.

The scripts get a path of an image in standard input and return the angle in degrees into standard output.

DN_task1_vX.py - version X of a deterministic variant.

### task1_v1 Report:
#### Algorithm:
1) read the image in gray scale  
2) apply Bilateral Filter  
3) apply Median Filter  
4) apply Canny Edge Detector  
5) apply Hough Transform  
6) restrict lines from the previous step by length and angle (trying to keep only lines of longer sides of a car number)  
7) find similar lines by angle  
8) the line which has the greatest number of similar lines has the angle as the prediction of the algorithm  

#### Validation:
1) were picked only photos from 'real_plates'
2) points of longer sides were placed by hands  
3) linear regression was used to get lines  
4) label - angle is average of angles of two lines from above  
5) **Accuracy**: 0.95; **MSE**: 0.18
