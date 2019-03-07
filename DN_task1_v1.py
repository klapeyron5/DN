def makeprediction(path):
    try:
        img = cv2.imread(path,0)

        d = 11
        sigmaColor = 17
        sigmaSpace = 17
        img = cv2.bilateralFilter(img,d=d,sigmaColor=sigmaColor,sigmaSpace=sigmaSpace)

        k = 3
        img = cv2.medianBlur(img,k)

        cannythr1 = 140
        cannythr2 = 180
        apertureSize = 3
        img = cv2.Canny(img,cannythr1,cannythr2,apertureSize=apertureSize,L2gradient=True)

        minlinelen = int(img.shape[1]*0.2)
        angle_bias = np.pi/2
        angle_window = 15
        angle_delta = 3
        min_theta = angle_bias-np.pi*(angle_window+angle_delta)/180
        max_theta = angle_bias+np.pi*(angle_window+angle_delta)/180
        lines = cv2.HoughLines(img,1,np.pi/180,minlinelen,min_theta=min_theta,max_theta=max_theta)
        lines = np.reshape(lines,(lines.shape[0],lines.shape[2]))

        def filter_lines(lines):
            theta_threshold = np.pi*1/180
            similar_lines = {i : [] for i in range(len(lines))}
            for i in range(len(lines)):
                for j in range(len(lines)):
                    if i == j:
                        continue
                    rho_i,theta_i = lines[i]
                    rho_j,theta_j = lines[j]
                    if abs(theta_i - theta_j) < theta_threshold:
                        similar_lines[i].append(j)
            indices = [i for i in range(len(lines))]
            indices.sort(key=lambda x : len(similar_lines[x]))
            return lines[0]

        filtered_line = filter_lines(lines)
        theta = filtered_line[1]
        angle = -(theta*180/np.pi - 90)

        return round(angle)
    except Exception:
        return 0

def main(args):
    path = args[0]
    print(makeprediction(path))

if __name__ == '__main__':
    import sys
    import os

    import numpy as np
    import cv2

    main(sys.argv[1:])
