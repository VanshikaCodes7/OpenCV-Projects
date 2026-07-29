import cv2

image=cv2.imread("Untitled design.png")

print("Welcome to 1st OpenCV Project")

print("1.Press 1 for opening Image")
print("2.Press 2 for opening GrayScale Image")
print("3.Press 3 for saving original Image")
print("4.Press 4 for saving GrayScale Image")

choice=int(input("Enter Your Choice: "))

match choice:

    case 1:
        image=cv2.resize(image, (640,360))
        cv2.imshow("Your Image", image)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    case 2:
        grayScaleImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

        grayScaleImage=cv2.resize(grayScaleImage, (1280,720))
        cv2.imshow("Grayscale Image", grayScaleImage)
        cv2.waitKey(0)
        cv2.destroyAllWindows()

    case 3:
        name=input("Enter image name: ")
        cv2.imwrite(name ,image)

    case 4:
        grayScaleImage=cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)
        name=input("Enter image name: ")
        cv2.imwrite(name ,grayScaleImage)