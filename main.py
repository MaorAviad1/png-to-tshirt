from PIL import Image
import os


def overlay_images(tshirt_path, image_dir, output_dir):
    # Get a list of all the image files in the directory
    image_files = [f for f in os.listdir(image_dir) if f.endswith('.png')]

    for image_file in image_files:
        # Load the t-shirt image
        tshirt_img = Image.open(tshirt_path)

        # Open the image file
        img = Image.open(os.path.join(image_dir, image_file))

        # Resize the png file as necessary.
        img = img.resize((600, 600))  # Change this to desired size

        # Calculate the center position
        width, height = tshirt_img.size
        position = ((width - img.width) // 2, (height - img.height) // 2)

        # Place the image on the t-shirt.
        tshirt_img.paste(img, position, img)  # The second argument is the top-left corner of the image

        # Save the result
        tshirt_img.save(os.path.join(output_dir, 'tshirt_with_' + image_file))


# Use the function
overlay_images('D:\\shirts\\t-shirt-image\\Black_Tee_Back_1200x1200.webp', 'D:\\shirts\\pngs', 'D:\\shirts\\result')
