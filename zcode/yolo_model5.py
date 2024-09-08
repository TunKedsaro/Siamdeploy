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
    seat = ["A1","A2","A3","A4","A5","A6","A7","A8","B1","B2","B3","B4","B5","B6","B7","B8","C1","C2","C3","C4","C5","C6","C7","C8","D1","D2","D3","D4","D5","D6","D7","D8","E1","E2","E3","E4","E5","E6","E7","E8","F1","F2","F3","F4","F5","F6","F7","F8","G1","G2","G3","G4","G5","G6","G7","G8","H1","H2","H3","H4","H5","H6","H7","H8","H9"]
    # seat = ["A1","A2","A3","A4","A5","A6","A7","A8"]
    seat = {i:False for i in seat}

    # Frames area
    areas = {
    # 1 /
        "A8": {"x_min": 1000, "y_min": 1500, "width": 50*10,"height": 50*5},        # A1 -> A8
        "A7": {"x_min": 1550, "y_min": 1300, "width": 50*8, "height": 50*8},        # B1 -> A7
        "A6": {"x_min": 2450, "y_min": 1150, "width": 50*7, "height": 50*7},        # C1 -> A6
        "A5": {"x_min": 2750, "y_min": 1100, "width": 50*5, "height": 50*6},        # D1 -> A5
        "A4": {"x_min": 3150, "y_min": 1100, "width": 50*4, "height": 50*4},        # E1 -> A4
        "A3": {"x_min": 3300, "y_min": 1050, "width": 50*3, "height": 50*4},        # F1 -> A3
        "A2": {"x_min": 3400, "y_min": 1000, "width": 50*3, "height": 50*4},        # G1 -> A2
        "A1": {"x_min": 3500, "y_min": 1000, "width": 50*3, "height": 50*4},        # H1 -> A1
    # 2 /
        "B8": {"x_min": 950, "y_min": 1050, "width": 50*6, "height": 50*5},         # A2 -> B8
        "B7": {"x_min": 1400, "y_min": 950, "width": 50*5, "height": 50*6},         # B2 -> B7
        "B6": {"x_min": 2100, "y_min": 950, "width": 50*5, "height": 50*5},         # C2 -> B6
        "B5": {"x_min": 2400, "y_min": 950, "width": 50*5, "height": 50*4},         # D2 -> B5
        "B4": {"x_min": 2850, "y_min": 900, "width": 50*4, "height": 50*4},         # E2 -> B4
        "B3": {"x_min": 3000, "y_min": 850, "width": 50*3, "height": 50*4},         # F2 -> B3
        "B2": {"x_min": 3100, "y_min": 850, "width": 50*4, "height": 50*3},         # G2 -> B2
        "B1": {"x_min": 3250, "y_min": 850, "width": 50*2, "height": 50*3},         # H2 -> B1
    # 3
        "C8": {"x_min": 850, "y_min": 800, "width": 50*6, "height": 50*5},          # A3 -> C8
        "C7": {"x_min": 1200, "y_min": 750, "width": 50*5, "height": 50*5},         # B3 -> C7
        "C6": {"x_min": 1900, "y_min": 750, "width": 50*4, "height": 50*4},         # C3 -> C6
        "C5": {"x_min": 2100, "y_min": 750, "width": 50*4, "height": 50*4},         # D3 -> C5
        "C4": {"x_min": 2500, "y_min": 700, "width": 50*4, "height": 50*4},         # E3 -> C4
        "C3": {"x_min": 2700, "y_min": 700, "width": 50*3, "height": 50*4},         # F3 -> C3
        "C2": {"x_min": 2850, "y_min": 750, "width": 50*4, "height": 50*3},         # G3 -> C2
    # "C1": {"x_min": 0, "y_min": 0, "width": 50*0, "height": 50*0},              # H3 -> C1
    # 4
        "D8": {"x_min": 900, "y_min": 700, "width": 50*5, "height": 50*3},          # A4 -> D8
        "D7": {"x_min": 1200, "y_min": 650, "width": 50*4, "height": 50*4},         # B4 -> D7
        "D6": {"x_min": 1650, "y_min": 600, "width": 50*5, "height": 50*4},         # C4 -> D6
        "D5": {"x_min": 1850, "y_min": 650, "width": 50*5, "height": 50*3},         # D4 -> D5
        "D4": {"x_min": 2250, "y_min": 600, "width": 50*4, "height": 50*4},         # E4 -> D4
        "D3": {"x_min": 2450, "y_min": 650, "width": 50*3, "height": 50*2},         # F4 -> D3
        "D2": {"x_min": 2650, "y_min": 650, "width": 50*3, "height": 50*2},         # G4 -> D2
        # "D1": {"x_min": 0, "y_min": 0, "width": 50*0, "height": 50*0},            # H4 -> D1
    # 5
        "E8": {"x_min": 850, "y_min": 550, "width": 50*4, "height": 50*4},          # A5 -> E8
        "E7": {"x_min": 1100, "y_min": 550, "width": 50*4, "height": 50*3},         # B5 -> E7
        "E6": {"x_min": 1500, "y_min": 500, "width": 50*3, "height": 50*3},         # C5 -> E6
        "E5": {"x_min": 1700, "y_min": 500, "width": 50*3, "height": 50*3},         # D5 -> E5
        # "E4": {"x_min": 2100, "y_min": 550, "width": 50*3, "height": 50*3},       # E5 -> E4
        "E3": {"x_min": 2200, "y_min": 550, "width": 50*3, "height": 50*2},         # E6 -> E3
        "E2": {"x_min": 2400, "y_min": 550, "width": 50*3, "height": 50*2},         # E7 -> E2
        # "E1": {"x_min": 0, "y_min": 0, "width": 50*1, "height": 50*1},            # E8 -> E1

    # 6
        "F8": {"x_min": 850,  "y_min": 450, "width": 50*3, "height": 50*3},         # A6 -> F8
        "F7": {"x_min": 1050, "y_min": 450, "width": 50*3, "height": 50*3},         # B6 -> F7
        "F6": {"x_min": 1350, "y_min": 450, "width": 50*4, "height": 50*3},         # C6 -> F6
        "F5": {"x_min": 1550, "y_min": 450, "width": 50*4, "height": 50*3},         # D6 -> F5
        "F4": {"x_min": 1900, "y_min": 450, "width": 50*3, "height": 50*3},         # E6 -> F4
        "F3": {"x_min": 2050, "y_min": 450, "width": 50*3, "height": 50*3},         # F6 -> F3
        "F2": {"x_min": 2200, "y_min": 450, "width": 50*2, "height": 50*3},         # G6 -> F2
        "F1": {"x_min": 2300, "y_min": 450, "width": 50*2, "height": 50*3},         # H6 -> F1
    # 7
        "G8": {"x_min": 850, "y_min": 450, "width": 50*3, "height": 50*2},          # A7 -> G8
        "G7": {"x_min": 1000, "y_min": 450, "width": 50*3, "height": 50*2},         # B7 -> G7
        "G6": {"x_min": 1300, "y_min": 400, "width": 50*3, "height": 50*2},         # C7 -> G6
        "G5": {"x_min": 1500, "y_min": 400, "width": 50*2, "height": 50*2},         # D7 -> G5
        "G4": {"x_min": 1750, "y_min": 400, "width": 50*3, "height": 50*2},         # E7 -> G4
        "G3": {"x_min": 1900, "y_min": 400, "width": 50*3, "height": 50*2},         # F7 -> G3
        "G2": {"x_min": 2000, "y_min": 400, "width": 50*2, "height": 50*2},         # G7 -> G2
        "G1": {"x_min": 2100, "y_min": 400, "width": 50*2, "height": 50*2},         # H7 -> G1
    # 8
        "H9": {"x_min": 800, "y_min": 400, "width": 50*2, "height": 50*2},
        "H8": {"x_min": 900, "y_min": 400, "width": 50*2, "height": 50*2},
        "H7": {"x_min": 1000, "y_min": 350, "width": 50*2, "height": 50*2},
        "H6": {"x_min": 1250, "y_min": 350, "width": 50*2, "height": 50*2},
        "H5": {"x_min": 1400, "y_min": 350, "width": 50*2, "height": 50*2},
        "H4": {"x_min": 1675, "y_min": 375, "width": 25*4, "height": 25*3},
        "H3": {"x_min": 1800, "y_min": 375, "width": 25*4, "height": 25*3},
        "H2": {"x_min": 1925, "y_min": 375, "width": 25*4, "height": 25*3},
        "H1": {"x_min": 2000, "y_min": 375, "width": 25*4, "height": 25*3},
    }

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