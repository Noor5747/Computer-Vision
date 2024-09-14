import cv2

# Load the image
image = cv2.imread('C:\\Users\\Noor\\Desktop\\147d19aec8a8ee0def71737eade566b5.jpg')

# Check if image loaded successfully
if image is None:
    print("Error: Could not load image.")
else:
    # Display the image
    cv2.imshow('Loaded Image', image)

    # Wait until a key is pressed
    cv2.waitKey(0)

    # Close the window
    cv2.destroyAllWindows()
