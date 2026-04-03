import fitz
import numpy as np
import easyocr
import cv2
from PIL import Image

reader = easyocr.Reader(['en'])

def pdf_to_images(pdf_file):

    images = []

    pdf = fitz.open(stream=pdf_file.read(), filetype="pdf")

    for page in pdf:
        pix = page.get_pixmap()
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)
        images.append(img)

    return images


def extract_text(images):

    full_text = ""

    for img in images:

        img_np = np.array(img)

        # convert to grayscale
        gray = cv2.cvtColor(img_np, cv2.COLOR_BGR2GRAY)

        # increase contrast
        gray = cv2.adaptiveThreshold(
            gray, 255,
            cv2.ADAPTIVE_THRESH_GAUSSIAN_C,
            cv2.THRESH_BINARY,
            11, 2
        )

        results = reader.readtext(gray)

        for (_, text, _) in results:
            full_text += text + "\n"

    return full_text