import qrcode
import tkinter as tk
from tkinter import *
import ttkbootstrap as ttk
import os

#conversion logic
def convert():
    input_data = entry_link.get()
    qr = qrcode.QRCode(version = 1, box_size = 10, border = 5)
    qr.add_data(input_data)
    qr.make(fit = True)
    img = qr.make_image(fill = "black", back_color = "white")   
    # Get the user's Pictures folder path
    pics_folder = os.path.join(os.path.expanduser("~"), "Desktop")
    # Set the output file path to the Pictures folder with the filename "QR_Code.png"
    output_file_path = os.path.join(pics_folder, "QR_Code.png")
    img.save(output_file_path)
    output_string.set(f"QR Code generated at {output_file_path}")

# window
window = ttk.Window(themename= "darkly")
window.title("QR Code Generator")
window.geometry("600x200")

# title
title_label = ttk.Label(master = window, text = "Enter link to turn into a QR Code", font = "Calibri 24 bold")
title_label.pack()

#input field
input_frame = ttk.Frame(master = window)
entry_link = tk.StringVar()
entry = ttk.Entry(master = input_frame, textvariable = entry_link)
button = ttk.Button(master = input_frame, text = "Convert", command = convert)
entry.pack(side = "left", padx = 10)
button.pack(side = "left")
input_frame.pack(pady = 10)

#output the QR code image
output_string = tk.StringVar()
output_label = ttk.Label(master = window, text = "Output", font = "Calibri 16", textvariable = output_string)
output_label.pack(pady = 5)



# run
window.mainloop()