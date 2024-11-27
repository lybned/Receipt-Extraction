from PIL import Image, ImageEnhance

# from src.config import *
class ImageUtil:
	def __init__(self):
		self.a = 1
		
	def darken_image(self,image):
		# Create an enhancer for contrast
		enhancer = ImageEnhance.Contrast(image.convert("L"))

		# Increase contrast, e.g., 1.5 times the original contrast
		image_enhanced = enhancer.enhance(3.5).rotate(-2, expand=True)

		# Save or show the enhanced image
		image_enhanced.save('enhanced_image.jpg')

		#img1 = np.array(image_enhanced.rotate(-2, expand=True))
		return image_enhanced