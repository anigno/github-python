import cv2

def calculate_ssim(image1, image2):
    """Calculates the Structural Similarity Index (SSIM) between two images."""
    # Convert the images to grayscale.
    image1 = cv2.cvtColor(image1, cv2.COLOR_BGR2GRAY)
    image2 = cv2.cvtColor(image2, cv2.COLOR_BGR2GRAY)
    # Calculate the SSIM between the two images.
    ssim = cv2.compareHist(image1, image2, cv2.HISTCMP_SSIM)
    return ssim

def compare_images(image_file1, image_file2, threshold_ssim=0.95):
    image1 = cv2.imread(image_file1)
    image2 = cv2.imread(image_file2)
    calculated_ssim = calculate_ssim(image1, image2)
    if calculated_ssim > threshold_ssim:
        return True
    return False
