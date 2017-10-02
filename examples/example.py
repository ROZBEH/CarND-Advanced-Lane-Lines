def warper(img, src, dst):

    # Compute and apply perpective transform
    img_size = (img.shape[1], img.shape[0])
    M = cv2.getPerspectiveTransform(src, dst)
    warped = cv2.warpPerspective(img, M, img_size, flags=cv2.INTER_NEAREST)  # keep same size as input image

    return warped
class Test:
	def __init__(self, a, b):
		self.first = a
		self.second = b

test = Test(4,5)
test.first = 12
print (test.first)