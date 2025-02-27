from ultralytics import YOLOv10
import matplotlib.pyplot as plt
from operator import itemgetter

import matplotlib.pyplot as plt
import matplotlib.patches as patches
from operator import itemgetter
print("done")

# Load your model
# model_path = os.path.join(os.path.dirname(__file__), 'models/best.pt')
model_path = r"C:\Users\Acer\Desktop\MSiam\zcode\models\200824.0558.pt"
model = YOLOv10(model_path)

# thaichar = {0: '0', 1: '1', 2: '2', 3: '3', 4: '4', 5: '5', 6: '6', 7: '7', 8: '8', 9: '9', 10: 'ก', 11: 'ข', 12: 'ฃ', 13: 'ค', 14: 'ฅ', 15: 'ฆ', 16: 'ง', 17: 'จ', 18: 'ฉ', 19: 'ช', 20: 'ซ', 21: 'ฌ', 22: 'ญ', 23: 'ฎ', 24: 'ฏ', 25: 'ฐ', 26: 'ฑ', 27: 'ฒ', 28: 'ณ', 29: 'ด', 30: 'ต', 31: 'ถ', 32: 'ท', 33: 'ธ', 34: 'น', 35: 'บ', 36: 'ป', 37: 'ผ', 38: 'ฝ', 39: 'พ', 40: 'ฟ', 41: 'ภ', 42: 'ม', 43: 'ย', 44: 'ร', 45: 'ล', 46: 'ว', 47: 'ศ', 48: 'ษ', 49: 'ส', 50: 'ห', 51: 'ฬ', 52: 'อ', 53: 'ฮ'}
# junwat = {54: 'กรุงเทพมหานคร', 55: 'กระบี่', 56: 'กาญจนบุรี', 57: 'กาฬสินธุ์', 58: 'กำแพงเพชร', 59: 'ขอนแก่น', 60: 'จันทบุรี', 61: 'ฉะเชิงเทรา', 62: 'ชลบุรี', 63: 'ชัยนาท', 64: 'ชัยภูมิ', 65: 'ชุมพร', 66: 'เชียงราย', 67: 'เชียงใหม่', 68: 'ตรัง', 69: 'ตราด', 70: 'ตาก', 71: 'นครนายก', 72: 'นครปฐม', 73: 'นครพนม', 74: 'นครราชสีมา', 75: 'นครศรีธรรมราช', 76: 'นครสวรรค์', 77: 'นนทบุรี', 78: 'นราธิวาส', 79: 'น่าน', 80: 'บึงกาฬ', 81: 'บุรีรัมย์', 82: 'ปทุมธานี', 83: 'ประจวบคีรีขันธ์', 84: 'ปราจีนบุรี', 85: 'ปัตตานี', 86: 'พระนครศรีอยุธยา', 87: 'พังงา', 88: 'พัทลุง', 89: 'พิจิตร', 90: 'พิษณุโลก', 91: 'เพชรบุรี', 92: 'เพชรบูรณ์', 93: 'แพร่', 94: 'พะเยา', 95: 'ภูเก็ต', 96: 'มหาสารคาม', 97: 'มุกดาหาร', 98: 'แม่ฮ่องสอน', 99: 'ยะลา', 100: 'ยโสธร', 101: 'ร้อยเอ็ด', 102: 'ระนอง', 103: 'ระยอง', 104: 'ราชบุรี', 105: 'ลพบุรี', 106: 'ลำปาง', 107: 'ลำพูน', 108: 'เลย', 109: 'ศรีสะเกษ', 110: 'สกลนคร', 111: 'สงขลา', 112: 'สตูล', 113: 'สมุทรปราการ', 114: 'สมุทรสงคราม', 115: 'สมุทรสาคร', 116: 'สระแก้ว', 117: 'สระบุรี', 118: 'สิงห์บุรี', 119: 'สุโขทัย', 120: 'สุพรรณบุรี', 121: 'สุราษฎร์ธานี', 122: 'สุรินทร์', 123: 'หนองคาย', 124: 'หนองบัวลำภู', 125: 'อ่างทอง', 126: 'อุดรธานี', 127: 'อุทัยธานี', 128: 'อุตรดิตถ์', 129: 'อุบลราชธานี', 130: 'อำนาจเจริญ'}

# def convert2label(clases):
#     label = ''
#     for i in clases:
#         if i in junwat.keys():
#             if i == 54:
#                 label = '0'
#             else:
#                 label = '1'
#     for j in clases:
#         if j in thaichar.keys():
#             label = label + thaichar[j]
#     return label

# def predict_label(image_path):
#     img = plt.imread(image_path)
#     results = model(source=img, conf=0.35)
#     for result in results:
#         if result.boxes:
#             boxes = result.boxes.xywh.tolist()
#             clases = [int(cls) for cls in result.boxes.cls.tolist()]
#             bc = []
#             for b, c in zip(boxes, clases):
#                 bc.append([c, b[0]])
#             ls = sorted(bc, key=itemgetter(1))
#             q = [i[0] for i in ls]
#             result_label = convert2label(q)
#             return result_label
#     print("There are no box")
#     return None

def predict_label_with_boxes(img):
    # img = plt.imread(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
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
    plt.imshow(img)
    plt.show()
    return len(box)


# r = predict_label(r"C:\Users\Acer\Desktop\labelapp - Copy\media\dGVfMjAyNy5qcGc_1KGml9L.jpg")
# print(r)


import base64
import matplotlib.pyplot as plt
def image_to_base64(image_path):
    with open(image_path, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read()).decode('utf-8')
    return encoded_string
base64img = image_to_base64(r"C:\Users\Acer\Desktop\MSiam\zcode\073124_131500.jpg")
# base64img


from PIL import Image
import io

def base64_to_image(encoded_string):
    image_data = base64.b64decode(encoded_string)
    image = Image.open(io.BytesIO(image_data))
    return image
# predict_label_with_boxes()

img = base64_to_image(base64img)
# plt.imshow(img)
# plt.show()

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
print(len(boxes))