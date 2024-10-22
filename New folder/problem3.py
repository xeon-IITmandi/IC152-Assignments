from matplotlib import pyplot as plt
plt.rcParams.update({'font.size': 22})


# install pillow using:
# pip3 install pillow
# if above does not work and you are on windows, try:-
# py -m pip3 install pillow

# importing Image and ImageOps from PIL
from PIL import Image, ImageOps

# creating image object:
imInp = Image.open('problem3Input.jpg')

# converting imInp to grayscale:
imGrayscale = ImageOps.grayscale(imInp)

# converting image to numpy array
import numpy as np
pixels2D = np.array(imGrayscale)
# print(pixels2D.shape)

# showing/saving image
# imGrayscale.show()
#imGrayscale.save('problem1cOutput.jpg')

# Write code for finding histogram here:
plt.subplot(1,1,1)
plt.title("Grayscale Histogram")
plt.xlabel("grayscale value")
plt.ylabel("pixel count")
plt.grid(True)
plt.xlim([0.0,255.0])
plt.hist(pixels2D.flatten(), bins = 128//2+1,color='#0504aa',
                                alpha=0.7, rwidth=0.6, align='mid', density=True)
plt.tight_layout()

figure = plt.gcf() # get current figure
figure.set_size_inches(16, 12)

plt.savefig('problem1ci.png', bbox_inches='tight')



    


# Write code for finding histogram of difference of pixel's intensity
# with its left neighbour here:

pixels2D_diff=[]
# pixels2D = pixels2D.astype(np.int16)  # Convert to int16

for i in range(0, pixels2D.shape[0]):  # Iterate over rows
    for j in range(1, pixels2D.shape[1]):  # Start from column 1
        diff = (pixels2D[i, j] - pixels2D[i, j - 1])  # Difference with the left neighbor
        pixels2D_diff.append(diff)

pixels2D_diff=np.array(pixels2D_diff)


plt.subplot(1,1,1)
plt.title("Histogram of Pixel Intensity Differences")
plt.xlabel("Difference in Grayscale Value")
plt.ylabel("Pixel Count")
plt.grid(True)
plt.xlim([-255.0,255.0])
plt.hist(pixels2D_diff.flatten(), bins = 128//2+1,color='#0504aa',
                                alpha=0.7, rwidth=0.6, align='mid', density=True)
plt.tight_layout()

figure = plt.gcf() # get current figure
figure.set_size_inches(16, 12)

plt.savefig('problem1cii.png', bbox_inches='tight')



