import os
from PIL import Image
import tkinter as tk
from tkinter import filedialog, messagebox

def repair_images():
    # Prompt user to select a folder
    folder_path = filedialog.askdirectory(title="Select Folder")
    
    if not folder_path:
        messagebox.showinfo("Error", "No folder selected.")
        return
    
    # Get the list of files in the folder
    files = os.listdir(folder_path)
    
    # Iterate over each file
    for file in files:
        file_path = os.path.join(folder_path, file)
        
        # Check if the file is an image
        if is_image_file(file):
            try:
                # Open the image and save it again to repair any errors
                image = Image.open(file_path)
                image.save(file_path)
                print(f"Repaired image: {file}")
            except Exception as e:
                print(f"Error repairing image: {file} - {str(e)}")

def is_image_file(file):
    # Check if the file has an image extension
    image_extensions = ['.jpg', '.jpeg', '.png', '.gif', '.bmp']
    file_extension = os.path.splitext(file)[1].lower()
    return file_extension in image_extensions

# Create the main window
window = tk.Tk()
window.title("Divin Image Repair Tool")

# Create the repair button
repair_button = tk.Button(window, text="Repair Images", command=repair_images)
repair_button.pack(pady=20)

# Start the GUI event loop
window.mainloop()
