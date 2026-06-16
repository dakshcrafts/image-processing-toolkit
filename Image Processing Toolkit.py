from PIL import Image, ImageFilter, ImageEnhance, ImageTk
import numpy as np
import tkinter as tk
from tkinter import filedialog

img = ""

BG       = "#0f0f1a"
CARD     = "#1a1a2e"
PREVIEW  = "#16213e"
ACCENT   = "#6366f1"
ACCENT2  = "#818cf8"
TEXT     = "#e2e8f0"
TEXT_DIM = "#64748b"
BORDER   = "#2d2d4e"


def on_enter(event):
    event.widget.config(bg=ACCENT2)

def on_leave(event):
    event.widget.config(bg=ACCENT)

def load_image():
    global img

    file = filedialog.askopenfilename(
        title="Select Image",
        filetypes=[("Image Files", "*.png *.jpg *.jpeg *.bmp *.webp")]
    )

    if file:
        img = file

        img = Image.open(file)
        img.thumbnail((210, 210))
        photo = ImageTk.PhotoImage(img)

        preview_label.config(image=photo, text="")
        preview_label.image = photo

        filename = file.split("/")[-1]
        file_label.config(text="  " + filename, fg="#22d3ee")
  

def main_window():

    def make_btn(parent, label, cmd, width=12):
        b = tk.Button(parent, text=label, command=cmd, bg=ACCENT, fg="white",
                      activebackground=ACCENT2, activeforeground="white",
                      relief="flat", cursor="hand2",
                      font=("Segoe UI", 9, "bold"), width=width, pady=5)
        b.bind("<Enter>", on_enter)
        b.bind("<Leave>", on_leave)
        return b

    def make_entry(parent, placeholder, width=6):
        e = tk.Entry(parent, bg="#0d0d1f", fg=TEXT, insertbackground=TEXT,
                     relief="flat", font=("Segoe UI", 9), width=width,
                     highlightthickness=1, highlightbackground=BORDER)
        e.insert(0, placeholder)
        return e

    def update_preview(pil_img):
        show = pil_img.copy()
        show.thumbnail((380, 380))
        photo = ImageTk.PhotoImage(show)
        prev_label.config(image=photo, text="")
        prev_label.image = photo

    def apply_brightness(val):
        if img == "":
            return
        matrix = np.array(img, dtype=np.int16)
        result = np.clip(matrix + int(float(val)), 0, 255).astype(np.uint8)
        update_preview(Image.fromarray(result))

    def apply_contrast(val):
        if img == "":
            return
        matrix = np.array(img, dtype=np.float32)
        result = np.clip((matrix - 128) * float(val) + 128, 0, 255).astype(np.uint8)
        update_preview(Image.fromarray(result))

    def apply_grayscale():
        if img == "":
            return
        matrix = np.array(img, dtype=np.float32)
        gray = np.dot(matrix[..., :3], [0.299, 0.587, 0.114])
        gray3 = np.stack([gray, gray, gray], axis=2).astype(np.uint8)
        update_preview(Image.fromarray(gray3))

    def apply_blur():
        if img == "":
            return
        update_preview(img.filter(ImageFilter.BoxBlur(3)))

    def apply_sharpen():
        if img == "":
            return
        update_preview(ImageEnhance.Sharpness(img).enhance(3.0))

    def apply_invert():
        if img == "":
            return
        update_preview(Image.fromarray(255 - np.array(img, dtype=np.uint8)))

    def apply_resize():
        if img == "":
            return
        result = img.resize((int(w_entry.get()), int(h_entry.get())))
        update_preview(result)

    def apply_crop():
        if img == "":
            return
        result = img.crop((int(x1.get()), int(y1.get()), int(x2.get()), int(y2.get())))
        update_preview(result)

    def apply_rotate(angle):
        if img == "":
            return
        update_preview(img.rotate(angle, expand=True))

    def apply_flip_h():
        if img == "":
            return
        update_preview(Image.fromarray(np.fliplr(np.array(img))))

    def apply_flip_v():
        if img == "":
            return
        update_preview(Image.fromarray(np.flipud(np.array(img))))

    def save_image():
        if img == "":
            return
        file = filedialog.asksaveasfilename(defaultextension=".png",
               filetypes=[("PNG", "*.png"), ("JPEG", "*.jpg")])
        if file:
            matrix = np.array(img, dtype=np.int16)
            result = np.clip(matrix + int(b_slider.get()), 0, 255).astype(np.float32)
            result = np.clip((result - 128) * float(c_slider.get()) + 128, 0, 255).astype(np.uint8)
            Image.fromarray(result).save(file)

    win = tk.Toplevel()
    win.title("Image Processing Toolkit - Editor")
    win.geometry("950x670")
    win.configure(bg=BG)
    win.resizable(False, False)

    top = tk.Canvas(win, height=4, bg=BG, highlightthickness=0)
    top.pack(fill="x")
    top.create_rectangle(0, 0, 475, 4, fill=ACCENT, outline="")
    top.create_rectangle(475, 0, 950, 4, fill=ACCENT2, outline="")

    tk.Label(win, text="Image Processing  T O O L K I T",
             font=("Segoe UI", 14, "bold"), bg=BG, fg=TEXT).pack(anchor="w", padx=16, pady=(8, 4))

    body = tk.Frame(win, bg=BG)
    body.pack(fill="both", expand=True, padx=10, pady=4)

    left = tk.Frame(body, bg=CARD, width=285,
                    highlightthickness=1, highlightbackground=BORDER)
    left.pack(side="left", fill="y", padx=(0, 8))
    left.pack_propagate(False)

    tk.Label(left, text="Filter & Effects", font=("Segoe UI", 11, "bold"),
             bg=CARD, fg=TEXT).pack(anchor="w", padx=10, pady=(12, 2))
    tk.Frame(left, bg=ACCENT, height=2).pack(fill="x", padx=10)

    tk.Label(left, text="Brightness", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 2))
    b_slider = tk.Scale(left, from_=-100, to=100, orient="horizontal",
                        command=apply_brightness, bg=CARD, fg=TEXT,
                        troughcolor=PREVIEW, highlightthickness=0,
                        length=255, sliderlength=16, width=11)
    b_slider.set(0)
    b_slider.pack(padx=10)

    tk.Label(left, text="Contrast", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(8, 2))
    c_slider = tk.Scale(left, from_=0.1, to=4.0, resolution=0.1, orient="horizontal",
                        command=apply_contrast, bg=CARD, fg=TEXT,
                        troughcolor=PREVIEW, highlightthickness=0,
                        length=255, sliderlength=16, width=11)
    c_slider.set(1.0)
    c_slider.pack(padx=10)

    tk.Label(left, text="Quick Effects", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 4))

    r1 = tk.Frame(left, bg=CARD)
    r1.pack(padx=10, pady=2, fill="x")
    make_btn(r1, "Grayscale", apply_grayscale, 11).pack(side="left", padx=(0, 4))
    make_btn(r1, "Invert",    apply_invert,    11).pack(side="left")

    r2 = tk.Frame(left, bg=CARD)
    r2.pack(padx=10, pady=2, fill="x")
    make_btn(r2, "Blur",    apply_blur,    11).pack(side="left", padx=(0, 4))
    make_btn(r2, "Sharpen", apply_sharpen, 11).pack(side="left")

    tk.Frame(left, bg=BORDER, height=1).pack(fill="x", padx=10, pady=(14, 4))

    tk.Label(left, text="Transformations", font=("Segoe UI", 11, "bold"),
             bg=CARD, fg=TEXT).pack(anchor="w", padx=10, pady=(4, 2))
    tk.Frame(left, bg=ACCENT2, height=2).pack(fill="x", padx=10)

    tk.Label(left, text="Resize", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 4))
    res_row = tk.Frame(left, bg=CARD)
    res_row.pack(padx=10, fill="x")
    tk.Label(res_row, text="W:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left")
    w_entry = make_entry(res_row, "800")
    w_entry.pack(side="left", padx=2)
    tk.Label(res_row, text="H:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left", padx=(6,0))
    h_entry = make_entry(res_row, "600")
    h_entry.pack(side="left", padx=2)
    make_btn(res_row, "Apply", apply_resize, 6).pack(side="left", padx=(6, 0))

    tk.Label(left, text="Crop  (x1 y1  x2 y2)", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 4))
    cr1 = tk.Frame(left, bg=CARD)
    cr1.pack(padx=10, fill="x")
    tk.Label(cr1, text="x1:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left")
    x1 = make_entry(cr1, "0", 5)
    x1.pack(side="left", padx=2)
    tk.Label(cr1, text="y1:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left", padx=(4,0))
    y1 = make_entry(cr1, "0", 5)
    y1.pack(side="left", padx=2)

    cr2 = tk.Frame(left, bg=CARD)
    cr2.pack(padx=10, pady=(3, 0), fill="x")
    tk.Label(cr2, text="x2:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left")
    x2 = make_entry(cr2, "500", 5)
    x2.pack(side="left", padx=2)
    tk.Label(cr2, text="y2:", bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(side="left", padx=(4,0))
    y2 = make_entry(cr2, "500", 5)
    y2.pack(side="left", padx=2)
    make_btn(cr2, "Crop", apply_crop, 6).pack(side="left", padx=(6, 0))

    tk.Label(left, text="Rotate", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 4))
    rot_row = tk.Frame(left, bg=CARD)
    rot_row.pack(padx=10, fill="x")
    make_btn(rot_row, "90°",  lambda: apply_rotate(90),  6).pack(side="left", padx=(0, 4))
    make_btn(rot_row, "180°", lambda: apply_rotate(180), 6).pack(side="left", padx=(0, 4))
    make_btn(rot_row, "270°", lambda: apply_rotate(270), 6).pack(side="left")

    tk.Label(left, text="Flip", bg=CARD, fg=ACCENT2,
             font=("Segoe UI", 9, "bold")).pack(anchor="w", padx=10, pady=(10, 4))
    flip_row = tk.Frame(left, bg=CARD)
    flip_row.pack(padx=10, fill="x")
    make_btn(flip_row, "Horizontal", apply_flip_h, 11).pack(side="left", padx=(0, 4))
    make_btn(flip_row, "Vertical",   apply_flip_v, 11).pack(side="left")

    right = tk.Frame(body, bg=CARD, highlightthickness=1, highlightbackground=BORDER)
    right.pack(side="left", fill="both", expand=True)

    prev_frame = tk.Frame(right, bg=PREVIEW)
    prev_frame.pack(fill="both", expand=True, padx=12, pady=12)

    prev_label = tk.Label(prev_frame, text="Image will appear here",
                          bg=PREVIEW, fg=TEXT_DIM, font=("Segoe UI", 10))
    prev_label.pack(expand=True)

    if img != "":
        update_preview(img)

    tk.Frame(right, bg=BORDER, height=1).pack(fill="x", padx=12)

    bot = tk.Frame(right, bg=CARD)
    bot.pack(fill="x", padx=12, pady=8)

    save_b = tk.Button(bot, text="Save Image", command=save_image,
                       bg=ACCENT, fg="white", activebackground=ACCENT2,
                       activeforeground="white", relief="flat", cursor="hand2",
                       font=("Segoe UI", 10, "bold"), padx=16, pady=6)
    save_b.pack(side="left", padx=(0, 8))
    save_b.bind("<Enter>", on_enter)
    save_b.bind("<Leave>", on_leave)

    exit_b = tk.Button(bot, text="Exit", command=win.destroy,
                       bg="#ef4444", fg="white", activebackground="#dc2626",
                       activeforeground="white", relief="flat", cursor="hand2",
                       font=("Segoe UI", 10, "bold"), padx=16, pady=6)
    exit_b.pack(side="left")

    tk.Frame(right, bg=BORDER, height=1).pack(fill="x", padx=12)
    tk.Label(right, text="© 2025 Eagle Head | Daksh Sharma",
             bg=CARD, fg=TEXT_DIM, font=("Segoe UI", 9)).pack(pady=6)


def open_editor():
    if img == "":
        file_label.config(text="  Please select an image first!", fg="#f87171")
        return

    file_label.config(text="  Opening editor...", fg="#22d3ee")
    root.withdraw()
    main_window()

root = tk.Tk()
root.title("Image Processing Toolkit")
root.geometry("520x680")
root.configure(bg=BG)
root.resizable(False, False)

top_bar = tk.Canvas(root, height=4, bg=BG, highlightthickness=0)
top_bar.pack(fill="x")
top_bar.create_rectangle(0, 0, 260, 4, fill=ACCENT, outline="")
top_bar.create_rectangle(260, 0, 520, 4, fill=ACCENT2, outline="")

tk.Label(root, text="Image Processing", font=("Segoe UI", 26, "bold"),
         bg=BG, fg=TEXT).pack(pady=(20, 0))

tk.Label(root, text="T O O L K I T", font=("Segoe UI", 11, "bold"),
         bg=BG, fg=ACCENT2).pack()

tk.Label(root, text="Edit  ·  Transform  ·  Enhance", font=("Segoe UI", 9),
         bg=BG, fg=TEXT_DIM).pack(pady=(4, 0))

card = tk.Frame(root, bg=CARD, highlightthickness=1, highlightbackground=BORDER)
card.pack(padx=28, pady=16, fill="both", expand=True)

preview_frame = tk.Frame(card, bg=PREVIEW, width=220, height=220,
                          highlightthickness=2, highlightbackground=ACCENT)
preview_frame.pack(pady=(24, 0))
preview_frame.pack_propagate(False)

preview_label = tk.Label(preview_frame, text="Open an image\nto preview it here",
                         bg=PREVIEW, fg=TEXT_DIM, font=("Segoe UI", 10), justify="center")
preview_label.pack(expand=True)

tk.Frame(card, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(18, 0))

file_label = tk.Label(card, text="  No image selected", bg=CARD, fg=TEXT_DIM,
                      font=("Segoe UI", 9), anchor="center")
file_label.pack(pady=(8, 4))

open_btn = tk.Button(card, text="Open Image", command=load_image, bg=ACCENT, fg="white",
                     activebackground=ACCENT2, activeforeground="white", relief="flat",
                     cursor="hand2", font=("Segoe UI", 11, "bold"), width=18, pady=10)
open_btn.pack(pady=8)
open_btn.bind("<Enter>", on_enter)
open_btn.bind("<Leave>", on_leave)

start_btn = tk.Button(card, text="Start Editing", command=open_editor, bg=ACCENT, fg="white",
                      activebackground=ACCENT2, activeforeground="white", relief="flat",
                      cursor="hand2", font=("Segoe UI", 11, "bold"), width=18, pady=10)
start_btn.pack(pady=8)
start_btn.bind("<Enter>", on_enter)
start_btn.bind("<Leave>", on_leave)

tk.Frame(card, bg=BORDER, height=1).pack(fill="x", padx=20, pady=(16, 0))

tk.Label(card, text="© 2025 Eagle Head | Daksh Sharma", font=("Segoe UI", 9),
         bg=CARD, fg=TEXT_DIM).pack(pady=12)

root.mainloop()


def Brightness(image_matrix, value):
    img_matrix1 = value - image_matrix
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Contrast(image_matrix, factor):
    img_matrix1 = np.clip((image_matrix - 128) * factor + 128, 0, 255)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Invert(image_matrix, value):
    img_matrix1 = value - image_matrix
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Grayscale(image_matrix):
    gray = np.dot(image_matrix[..., :3], [0.299, 0.587, 0.114])
    img_form = Image.fromarray(gray.astype(np.uint8))
    img_form.show()

def Blur(img, value):
    img_form = img.filter(ImageFilter.BoxBlur(value))
    img_form.show()

def Sharpen(img, factor):
    enhancer = ImageEnhance.Sharpness(img)
    img_form = enhancer.enhance(factor)
    img_form.show()

def Resize(img, width, height):
    img_form = img.resize((width, height))
    img_form.show()

def Crop(image_matrix, value_list):
    img_matrix1 = image_matrix[value_list[1]:value_list[0], value_list[3]:value_list[2]]
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Rotate(image_matrix, angle):
    if angle == 90:
        img_matrix1 = np.rot90(img, 1)
    elif angle == 180:
        img_matrix1 = np.rot90(img, 2)
    elif angle == 270:
        img_matrix1 = np.rot90(img, 3)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Flip_Horitontal(img):
    img_matrix1 = np.fliplr(img)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()

def Flip_Vertical(img):
    img_matrix1 = np.flipud(img)
    img_form = Image.fromarray(img_matrix1)
    img_form.show()
