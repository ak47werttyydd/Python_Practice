from PIL import Image, ImageDraw

# Load the uploaded image
image_path = "/Users/adrianhwang/Downloads/power.png"
image = Image.open(image_path)

# Create a drawing object to edit the image
draw = ImageDraw.Draw(image)

# Define the region for the dashed line and 'TDP' annotation
# Approximate coordinates for the red dashed line and TDP label
line_y_position = 60  # Rough estimate based on normalized power ~1.0
image_width = image.width
text_x, text_y = 460, 30  # Coordinates of 'TDP'

# Remove the dashed line by drawing over it
draw.line([(0, line_y_position), (image_width, line_y_position)], fill=(255, 255, 255), width=3)

# Remove 'TDP' by overwriting with a white rectangle
text_width, text_height = 40, 20  # Approximate size of 'TDP' text
draw.rectangle([(text_x, text_y), (text_x + text_width, text_y + text_height)], fill=(255, 255, 255))

# Save the edited image
output_path = "/Users/adrianhwang/Downloads/edited_image.png"
image.save(output_path)

# Show the edited image to the user
output_path