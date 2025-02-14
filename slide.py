from slide_content_extractor import SlideContentExtractor
from thumbnail_phash_generator import ThumbnailPerceptualHashGenerator

class Slide:
    def __init__(self, uploaded_file):
        self.uploaded_file = uploaded_file

    def process(self):
        content_extractor = SlideContentExtractor(self.uploaded_file)
        self.content = content_extractor.extract()

        thumnail_phash_generator = ThumbnailPerceptualHashGenerator(self.uploaded_file)
        self.image_buffer = thumnail_phash_generator.generate_thumnail_image()
        self.phash = thumnail_phash_generator.generate_perceptual_hash(self.image_buffer)