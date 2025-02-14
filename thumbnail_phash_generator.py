from pymupdf import pymupdf
from PIL import Image
import io
import imagehash

class ThumbnailPerceptualHashGenerator:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def generate_thumnail_image(self):
        self.uploaded_file.seek(0)

        # Create the pdf document from uploaded file data stream
        pdf_document = pymupdf.open(stream=self.uploaded_file.read(), filetype="pdf")
        page = pdf_document[0]

        # Convert to pixmap
        pix = page.get_pixmap(colorspace=pymupdf.csRGB)

        # Convert Pixmap to PIL Image
        img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

        # Resize proportionally to a width of 200 pixels
        img.thumbnail((200, img.height * 200 // img.width))

        # Save image to a memory buffer
        img_buffer = io.BytesIO()
        img.save(img_buffer, format="PNG")
        img_buffer.seek(0)  # Reset buffer position
        return img_buffer

    def generate_perceptual_hash(self, image_buffer):
         # Load image from buffer for pHash calculation
        image_buffer.seek(0)  # Reset buffer position
        image_for_hash = Image.open(image_buffer)

        # Compute perceptual hash (pHash)
        phash_value = imagehash.phash(image_for_hash)
        return phash_value