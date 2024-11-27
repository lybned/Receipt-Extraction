from datasets import load_dataset
from PIL import Image, ImageEnhance
class DataUtil:
	def __init__(self):
		self.dataset = load_dataset("naver-clova-ix/cord-v1")
		
	def get_train_data(self):
		return self.dataset['train']#.copy()
		
	def darken_image(self,image):
		# Create an enhancer for contrast
		enhancer = ImageEnhance.Contrast(image.convert("L"))

		# Increase contrast, e.g., 1.5 times the original contrast
		image_enhanced = enhancer.enhance(3.5).rotate(-2, expand=True)

		# Save or show the enhanced image
		image_enhanced.save('enhanced_image.jpg')

		#img1 = np.array(image_enhanced.rotate(-2, expand=True))
		return image_enhanced