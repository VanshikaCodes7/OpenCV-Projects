import cv2
import numpy as np


def nothing(x):
    pass

def save_edited_image(image_to_save):
    """Prompts the user whether they want to save the final image."""
    print("""\nDo you want to save the edited image?
1. Yes
2. No""")
    save_choice = input("Enter your choice (1 or 2): ").strip()

    if save_choice == "1":
        file_name = input("Enter filename to save (e.g., my_drawing.png): ").strip()
        
        # Default extension if user forgets to type one
        if not (file_name.endswith(".png") or file_name.endswith(".jpg") or file_name.endswith(".jpeg")):
            file_name += ".png"

        cv2.imwrite(file_name, image_to_save)
        print(f"✅ Image successfully saved as '{file_name}'!")
    elif save_choice == "2":
        print("Image was not saved.")
    else:
        print("Invalid choice. Image was not saved.")

def draw_on_image(target_image):
    """Prompts user for drawing inputs and applies them to target_image."""
    print("""
1. Choose one for drawing line
2. Choose two for drawing rectangle
3. Choose three for drawing circle
4. Choose four for writing text
""")
    choice = int(input("Enter your choice: "))

    match choice:
        case 1:
            print("We are drawing a line!")
            pt1 = input("Enter starting point x and y axes separated by spaces: ").split()
            pt1_tuple = tuple(int(x) for x in pt1)
            pt2 = input("Enter ending point x and y axes separated by spaces: ").split()
            pt2_tuple = tuple(int(x) for x in pt2)
            pt3 = input("Enter BGR colors(0-255) separated by spaces: ").split()
            pt3_tuple = tuple(int(x) for x in pt3)
            thickness = int(input("Enter the thickness: "))
            
            cv2.line(target_image, pt1_tuple, pt2_tuple, pt3_tuple, thickness)
            cv2.imshow("Edited Image!", target_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            save_edited_image(target_image)

        case 2:
            print("We are drawing a Rectangle!")
            pt1 = input("Enter top-left point x and y axes separated by spaces: ").split()
            pt1_tuple = tuple(int(x) for x in pt1)
            pt2 = input("Enter bottom-right point x and y axes separated by spaces: ").split()
            pt2_tuple = tuple(int(x) for x in pt2)
            pt3 = input("Enter BGR colors(0-255) separated by spaces: ").split()
            pt3_tuple = tuple(int(x) for x in pt3)
            thickness = int(input("Enter the thickness(Enter -1 for filling the shape): "))
            
            cv2.rectangle(target_image, pt1_tuple, pt2_tuple, pt3_tuple, thickness)
            cv2.imshow("Edited Image!", target_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            save_edited_image(target_image)

        case 3:
            print("We are drawing a circle!")
            pt1 = input("Enter center point x and y axes separated by spaces: ").split()
            pt1_tuple = tuple(int(x) for x in pt1)
            radius = int(input("Enter the radius: "))
            pt3 = input("Enter BGR colors(0-255) separated by spaces: ").split()
            pt3_tuple = tuple(int(x) for x in pt3)
            thickness = int(input("Enter the thickness(Enter -1 for filling the shape): "))
            
            cv2.circle(target_image, pt1_tuple, radius, pt3_tuple, thickness)
            cv2.imshow("Edited Image!", target_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()
            save_edited_image(target_image)

        case 4:
            print("We are adding text to the Image!")
            text = input("Enter the text you want to display: ")
            pt1 = input("Enter starting point x and y axes separated by spaces: ").split()
            pt1_tuple = tuple(int(x) for x in pt1)
            font_scale = float(input("Enter the font-scale: "))
            pt3 = input("Enter BGR colors(0-255) separated by spaces: ").split()
            pt3_tuple = tuple(int(x) for x in pt3)
            thickness = int(input("Enter the thickness: "))
            save_edited_image(target_image)
                 
            cv2.putText(target_image, text, pt1_tuple, cv2.FONT_HERSHEY_SCRIPT_COMPLEX, font_scale, pt3_tuple, thickness)
            cv2.imshow("Edited Image!", target_image)
            cv2.waitKey(0)
            cv2.destroyAllWindows()

        case _:
            print("Invalid Choice!")

img=cv2.imread("Untitled design.png")
image = cv2.resize(img, (1280, 720))

print("Welcome to drawing on Image Program!")
print("You can consider the following dimensions for better styling or use a blank canvas!")
print("""
1. Choose one for using the project's image
2. Choose two for using a blank canvas
""")

choice = int(input("Enter your choice: "))

match choice:
    case 1:
        print(f""" Dimension Guidance:
    1. Left Photo
    Rect left(0, 0, 420, 350);

    2. Center Photo
    Rect center(460, 265, 420, 395);

    3. Right Photo
    Rect right(930, 495, 350, 225);

    4. Text
    Point goals(470, 250);
    Point make it happen(820, 700);
    
    5. Fairy lights
    Point fairyStart(930, 15);
    Point fairyEnd(1275, 110);

    6. Sparkle region
    Rect sparkle(0, 500, 220, 220);
    """)
        
        draw_on_image(image)

    case 2:
        print("\n--- Blank Canvas Setup ---")
        cv2.namedWindow("Set Canvas Color")
        cv2.createTrackbar("R", "Set Canvas Color", 0, 255, nothing)
        cv2.createTrackbar("G", "Set Canvas Color", 0, 255, nothing)
        cv2.createTrackbar("B", "Set Canvas Color", 0, 255, nothing)

        canvas = np.zeros((500, 500, 3), dtype="uint8")

        print("Adjust background color with trackbars.")
        print("Press 'c' or SPACEBAR to confirm your background color, or ESC to exit.")

        while True:
            r = cv2.getTrackbarPos("R", "Set Canvas Color")
            g = cv2.getTrackbarPos("G", "Set Canvas Color")
            b = cv2.getTrackbarPos("B", "Set Canvas Color")

            canvas[:] = [b, g, r]
            cv2.imshow("Set Canvas Color", canvas)

            key = cv2.waitKey(1) & 0xFF
            if key in [ord('c'), 32]: 
                break
            elif key == 27:  
                cv2.destroyAllWindows()
                exit()

        cv2.destroyAllWindows()

        draw_on_image(canvas)

    case _:
        print("Invalid Choice!")