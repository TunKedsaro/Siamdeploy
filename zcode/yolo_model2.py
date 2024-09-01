from ultralytics import YOLOv10
import matplotlib.pyplot as plt
import matplotlib.patches as patches
from operator import itemgetter
import base64
from PIL import Image
import io

# print("done")

# Load your model
# model_path = os.path.join(os.path.dirname(__file__), 'models/best.pt')
# model_path = r"C:\Users\Acer\Desktop\MSiam\zcode\models\200824.0558.pt"
# model = YOLOv10(model_path)

# def predict_label_with_boxes(img):
#     # img = plt.imread(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
#     results = model(source=img,
#                     conf=0.15
#     )
#      # Set the figure size before plotting
#     fig, ax = plt.subplots(1, figsize=(12, 8))  # Adjust the figsize as needed
#     ax.imshow(img)

#     for result in results:
#         if result.boxes:
#             boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
#             clases = [int(cls) for cls in result.boxes.cls.tolist()]

#             for box, cls in zip(boxes, clases):
#                 x_min, y_min, x_max, y_max = box
#                 rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
#                                          linewidth=1, edgecolor='r', facecolor='none')
#                 ax.add_patch(rect)
#                 plt.text(x_min, y_min, f'', color='white', fontsize=12,
#                          bbox=dict(facecolor='red', alpha=0.5))
#     plt.imshow(img)
#     plt.show()
#     return len(box)


model_path = r"C:\Users\Acer\Desktop\MSiam\zcode\models\200824.0558.pt"
model = YOLOv10(model_path)

# # img -> base64
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string


# # base64 -> img
def base64_to_image(encoded_string):
    image_data = base64.b64decode(encoded_string)
    image = Image.open(io.BytesIO(image_data))
    return image

def img_predict(base64img):
    img = base64_to_image(base64img)
    results = model(source=img,
                conf=0.15
    )
    # Set the figure size before plotting
    fig, ax = plt.subplots(1, figsize=(12, 8))  # Adjust the figsize as needed
    ax.imshow(img)

    for result in results:
        if result.boxes:
            boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
            clases = [int(cls) for cls in result.boxes.cls.tolist()]

            for box, cls in zip(boxes, clases):
                x_min, y_min, x_max, y_max = box
                rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
                                        linewidth=1, edgecolor='r', facecolor='none')
                ax.add_patch(rect)
                plt.text(x_min, y_min, f'', color='white', fontsize=12,
                        bbox=dict(facecolor='red', alpha=0.5))
    # plt.imshow(img)
    # plt.show()
    # print(len(boxes))
    return img,len(boxes)

base64img = image_to_base64(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
# img = base64_to_image(base64img)
fimg,fval = img_predict(base64img)
plt.imshow(fimg)
plt.show()

print(fval)
# results = model(source=img,
#                 conf=0.15
# )
# # Set the figure size before plotting
# fig, ax = plt.subplots(1, figsize=(12, 8))  # Adjust the figsize as needed
# ax.imshow(img)

# for result in results:
#     if result.boxes:
#         boxes = result.boxes.xyxy.tolist()  # xyxy format for drawing boxes
#         clases = [int(cls) for cls in result.boxes.cls.tolist()]

#         for box, cls in zip(boxes, clases):
#             x_min, y_min, x_max, y_max = box
#             rect = patches.Rectangle((x_min, y_min), x_max - x_min, y_max - y_min,
#                                     linewidth=1, edgecolor='r', facecolor='none')
#             ax.add_patch(rect)
#             plt.text(x_min, y_min, f'', color='white', fontsize=12,
#                     bbox=dict(facecolor='red', alpha=0.5))
# plt.imshow(img)
# plt.show()
# print(len(boxes))