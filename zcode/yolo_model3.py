from ultralytics import YOLOv10
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from operator import itemgetter
import base64
from PIL import Image
import io
from io import BytesIO

model_path = r"C:\Users\Acer\Desktop\MSiam\zcode\models\200824.0558.pt"
model = YOLOv10(model_path)

# # img -> base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string

# def img_to_base64(img):
#     encoded_string = base64.b64encode(img.decode('utf-8'))
#     return encoded_string


# # base64 -> img
def base64_to_image(encoded_string):
    image_data = base64.b64decode(encoded_string)
    image = Image.open(io.BytesIO(image_data))
    return image

def pil_image_to_base64(img):
    buffered = BytesIO()
    img.save(buffered, format="PNG")
    img_str = base64.b64encode(buffered.getvalue()).decode("utf-8")
    return img_str

# def img_predict(base64img):
#     img = base64_to_image(base64img)
#     results = model(source=img,
#                 conf=0.15
#     )
#     # Set the figure size before plotting
#     fig, ax = plt.subplots(1, figsize=(12, 8))  # Adjust the figsize as needed
#     ax.imshow(img)

#     for result in results:
#         if result.boxes:
#             boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
#             clases = [int(cls) for cls in result.boxes.cls.tolist()]

#             for box, cls in zip(boxes, clases):
#                 x_min, y_min, x_max, y_max = box
#                 rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
#                                         linewidth=1, edgecolor='r', facecolor='none')
#                 ax.add_patch(rect)
#                 plt.text(x_min, y_min, f'', color='white', fontsize=12,
#                         bbox=dict(facecolor='red', alpha=0.5))
#     # plt.imshow(img)
#     # plt.show()
#     # print(len(boxes))
#     return img,len(boxes)

# base64img = image_to_base64(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
# img = base64_to_image(base64img)
# fimg,fval = img_predict(base64img)
# plt.imshow(fimg)
# plt.show()

# print(fval)


# def img_predict(base64img):
#     img = base64_to_image(base64img)
#     results = model(source=img,
#                 conf=0.15
#     )
#     # Set the figure size before plotting
#     fig, ax = plt.subplots(1, figsize=(12, 8))  # Adjust the figsize as needed
#     ax.imshow(img)

#     for result in results:
#         if result.boxes:
#             boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
#             clases = [int(cls) for cls in result.boxes.cls.tolist()]

#             for box, cls in zip(boxes, clases):
#                 x_min, y_min, x_max, y_max = box
#                 rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
#                                         linewidth=1, edgecolor='r', facecolor='none')
#                 ax.add_patch(rect)
#                 plt.text(x_min, y_min, f'', color='white', fontsize=12,
#                         bbox=dict(facecolor='red', alpha=0.5))
#     # plt.imshow(img)
#     # plt.show()
#     # print(len(boxes))
#     return img,len(boxes)

# base64img = image_to_base64(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
# img = base64_to_image(base64img)
# fimg,fval = img_predict(base64img)
# plt.imshow(fimg)
# plt.show()

# print(fval)


def img_predict(base64img):
    img = base64_to_image(base64img)
    results = model(source=img, conf=0.15)

    # Set up the figure for plotting
    fig, ax = plt.subplots(1, figsize=(12, 8), frameon=False)
    ax.imshow(img)

    for result in results:
        if result.boxes:
            boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
            classes = [int(cls) for cls in result.boxes.cls.tolist()]

            for box, cls in zip(boxes, classes):
                x_min, y_min, x_max, y_max = box
                rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                         linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                plt.text(x_min, y_min, f'', color='white', fontsize=12,
                         bbox=dict(facecolor='red', alpha=0.5))
    
    # Remove axis, ticks, and padding
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
    
    return annotated_img, len(boxes)