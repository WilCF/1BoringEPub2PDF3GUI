import os
import tkinter as tk
from tkinter import filedialog
from tkinterdnd2 import DND_FILES, TkinterDnD
from ebooklib import epub
from PyPDF2 import PdfFileWriter, PdfFileReader

# Function to convert EPUB to PDF
def epub_to_pdf(epub_path, pdf_path):
    book = epub.read_epub(epub_path)

    for item in book.get_items():
        if item.get_type() == ebooklib.ITEM_DOCUMENT:
            with open(pdf_path, 'wb') as pdf_file:
                pdf_file.write(item.get_content().decode('utf-8'))

    print(f'Converted {epub_path} to {pdf_path}')

# Function to handle file drop event
def drop(event):
    epub_path = event.data
    pdf_path = filedialog.asksaveasfilename(defaultextension='.pdf')
    if pdf_path:
        epub_to_pdf(epub_path, pdf_path)

# Create a TkinterDnD window
root = TkinterDnD.Tk()

# Create a label with instructions
label = tk.Label(root, text='Drag and drop an EPUB file here:', font=('Arial', 14))
label.pack(padx=10, pady=10)

# Bind the drop event to the drop function
root.drop_target_register(DND_FILES)
root.dnd_bind('<<Drop>>', drop)

# Run the main loop
root.mainloop()
