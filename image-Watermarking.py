import tkinter as tk
from tkinter import filedialog
from PIL import Image, ImageDraw, ImageFont

#Upload the Image
def upload_image():
    file_path = filedialog.askopenfilename(filetypes=[("Image files", "*.jpg *.png")])
    if file_path:
        image = Image.open(file_path)
        add_watermark(image)

def add_watermark(image):
    watermark = Image.new('RGBA', image.size, (0, 0, 0, 0))

    font = ImageFont.truetype('arial.ttf', 50)

    draw = ImageDraw.Draw(watermark)

    text = 'Watermark'
    text_width, text_height = draw.textsize(text, font)
    x = image.width - text_width - 10
    y = image.height - text_height - 10

    draw.text((x, y), text, font=font, fill=(255, 255, 255, 128))

    watermarked_image = Image.alpha_composite(image.convert('RGBA'), watermark).convert('RGB')

    output_path = filedialog.asksaveasfilename(defaultextension='.jpg', filetypes=[("JPEG files", "*.jpg")])
    if output_path:
        watermarked_image.save(output_path)
        tk.messagebox.showinfo('Success', 'Watermark added and image saved successfully!')

###Create the Window
window = tk.Tk()
window.title('Image Watermark')

instruction_label = tk.Label(window, text='Click the button below to upload an image and add a watermark.')
instruction_label.pack(pady=10)

upload_button = tk.Button(window, text='Upload Image', command=upload_image)
upload_button.pack(pady=10)

window.mainloop()
