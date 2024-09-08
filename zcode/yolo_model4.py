# # base64 -> img
import base64
import io
from PIL import Image
import numpy as np
import matplotlib.pyplot as plt


from ultralytics import YOLOv10
import matplotlib.patches as patches
from operator import itemgetter
from io import BytesIO


model_path = r"C:\Users\Acer\Desktop\MSiam\zcode\models\200824.0558.pt"
model = YOLOv10(model_path)

def base64_to_image(encoded_string):
    # Decode base64 and open the image
    image_data = base64.b64decode(encoded_string)
    image = Image.open(io.BytesIO(image_data)).convert('RGB')
    
    # Resize the image to the target size (2160, 3840)
    target_size = (3840, 2160)  # PIL expects (width, height)
    resized_image = image.resize(target_size, Image.Resampling.LANCZOS)
    
    # Convert to NumPy array
    image_np = np.array(resized_image)
    
    return image_np

def fn(contents):
    # with open(r"C:\Users\Acer\Desktop\MSiam\zcode\img5.txt",'r') as f:
    #     contents = f.read()

    img = base64_to_image(contents)
    print(img.shape)
    results = model(source=img, conf=0.15)
    # Set up the figure for plotting
    fig, ax = plt.subplots(1, figsize=(12, 8), frameon=False)
    ax.imshow(img)

    # Frames
    areas = {
    "A8": {"x_min": 1000, "y_min": 1500, "width": 50*10,"height": 50*5},        # A1 -> A8
    "A7": {"x_min": 1550, "y_min": 1300, "width": 50*8, "height": 50*8},        # B1 -> A7
    "A6": {"x_min": 2450, "y_min": 1150, "width": 50*7, "height": 50*7},        # C1 -> A6
    "A5": {"x_min": 2750, "y_min": 1100, "width": 50*5, "height": 50*6},        # D1 -> A5
    "A4": {"x_min": 3150, "y_min": 1100, "width": 50*4, "height": 50*4},        # E1 -> A4
    "A3": {"x_min": 3300, "y_min": 1050, "width": 50*3, "height": 50*4},        # F1 -> A3
    "A2": {"x_min": 3400, "y_min": 1000, "width": 50*3, "height": 50*4},        # G1 -> A2
    "A1": {"x_min": 3500, "y_min": 1000, "width": 50*3, "height": 50*4},        # H1 -> A1
    }

    seat = ["A1","A2","A3","A4","A5","A6","A7","A8"]
    seat = {i:False for i in seat}
    # print(seat)

        # Draws Frames on images
    for area_name, area in areas.items():
        rect_area = patches.Rectangle((area["x_min"], area["y_min"]), area["width"], area["height"],
                                    linewidth=1, edgecolor='blue', facecolor='none', label=area_name)
        ax.add_patch(rect_area)

    for result in results:
        if not result.boxes:
            print("There are no boxes")
        else:
            boxes = result.boxes.xyxy.tolist()
            clases = [int(cls) for cls in result.boxes.cls.tolist()]
            for box, cls in zip(boxes, clases):
                # Center of box
                x_min, y_min, x_max, y_max = box
                center_x = (x_min + x_max) / 2
                center_y = (y_min + y_max) / 2

                # Track if the center is in any area
                center_in_any_area = False

                # Loop to check each area
                for area_name, area in areas.items():
                    area_x_max = area["x_min"] + area["width"]
                    area_y_max = area["y_min"] + area["height"]
                    in_area = (area["x_min"] <= center_x <= area_x_max) and (area["y_min"] <= center_y <= area_y_max)

                    # Update seat status and mark center_in_any_area
                    if in_area:
                        seat[area_name] = True
                        center_in_any_area = True

                # # Draw box of the detected object
                # rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                #                          linewidth=1, edgecolor='r', facecolor='none')
                # ax.add_patch(rect)

                # Mark the center of the box; green if in any area, red otherwise
                ax.plot(center_x, center_y, 'go' if center_in_any_area else 'ro')
    ax.axis('off')
    plt.subplots_adjust(left=0, right=1, top=1, bottom=0, wspace=0, hspace=0)
    plt.margins(0)
    plt.gca().xaxis.set_major_locator(plt.NullLocator())
    plt.gca().yaxis.set_major_locator(plt.NullLocator())

    # Draw the canvas without displaying it
    fig.canvas.draw()  # Draws the figure in memory

    # Save the figure to a BytesIO object as a PIL image
    buf = BytesIO()
    plt.savefig(buf, format='PNG', bbox_inches='tight', pad_inches=0)
    buf.seek(0)
    annotated_img = Image.open(buf)

    plt.close(fig)  # Close the figure to free memory
    
    return annotated_img, len(boxes), seat

# a,b,c = fn('abc')
# plt.imshow(a)
# plt.show()
# print(b)
# print(c)



# import configparser
# import ast  

# config = configparser.ConfigParser()
# config.read(r"C:\Users\Acer\Desktop\MSiam\zcode\seat_data.ini")

# seat_str = config.get('room1', 'seat')

# seat_list = ast.literal_eval(seat_str)

# print(seat_list)

# import configparser
# import json

# # Initialize the config parser
# config = configparser.ConfigParser()

# # Read the .ini file
# config.read(r"C:\Users\Acer\Desktop\MSiam\zcode\seat_data.ini")

# # Get the areas string from the ini file
# areas_str = config.get('room1', 'areas')

# # Convert the string back to a dictionary
# areas = json.loads(areas_str)

# # Print the areas dictionary
# print(areas)

# import configparser
# import json

# config = configparser.ConfigParser()
# config.read(r"C:\Users\Acer\Desktop\MSiam\zcode\seat_data.ini")

# areas_str = config.get('room1', 'areas')
# areas = json.loads(areas_str)  # Convert JSON string to dictionary
# print(areas)