from PIL import Image, ImageEnhance

class DataUtil:
	def __init__(self):
		pass
	def darkenImage(image):
	  # Create an enhancer for contrast
	  enhancer = ImageEnhance.Contrast(image.convert("L"))

	  # Increase contrast, e.g., 1.5 times the original contrast
	  image_enhanced = enhancer.enhance(3.5).rotate(-2, expand=True)

	  # Save or show the enhanced image
	  image_enhanced.save('enhanced_image.jpg')

	  #img1 = np.array(image_enhanced.rotate(-2, expand=True))
	  return image_enhanced