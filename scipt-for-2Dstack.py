#!/usr/bin/env python
# coding: utf-8

# In[1]:


get_ipython().system('pip install tifffile')


# In[ ]:


# script that uses the NumPy and Pillow libraries 
# It helps to unstack 3D images to 2D and save all the images separately in .tif format


# In[2]:


import tifffile
import numpy as np
from PIL import Image
import matplotlib.pyplot as plt
import os


# In[3]:


# Load the .lsm image as a NumPy array
image_dr = "./3D-image/"
file_name = "20140425_LOT20140421_Matrigel_#3_Day5_MCF10A.lsm"
input_image = image_dr + file_name
image_3d = tifffile.imread(input_image)
print(input_image)


# In[4]:


# Check the shape and data type of the NumPy array (62, 848, 848) (68, 260, 289)

print("Shape of the NumPy array:", image_3d.shape)


# In[5]:


np.save("./np_array_output_one/array1.npy", image_3d)


# In[6]:


# load the 3D image as a NumPy array
image_3d_np = np.load("./np_array_output_one/array1.npy")


# In[7]:


image_3d_np.shape


# In[8]:


file_name


# In[9]:


# Create a new folder in the current working directory
file_name_without_ext = '.'.join(file_name.split('.')[:-1])

folder_path = "./sliced-individial-folder/" + file_name_without_ext
if not os.path.exists(folder_path):
    os.makedirs(folder_path)
print(folder_path)


# In[14]:


cnt = 0
# loop over each slice in the 3D image and save it as a separate 2D image
for i in range(image_3d.shape[0]):
    # extract the i-th slice from the 3D image
    image_2d = image_3d[i, :, :]
    threshold = 2000
    
    if np.max(image_2d) > threshold :
        print("higher intensity", i, np.max(image_2d))
        cnt = cnt + 1
        # convert the 2D NumPy array to a Pillow image
        image_pil = Image.fromarray(image_2d)
                    
        # save the image as a .tif file with a unique name
        filename = "./sliced-individial-folder/" + file_name_without_ext + "/slice{}.tif".format(i)
        image_pil.save(filename)
print("cnt", cnt)


# In[12]:


# Read the image

img = tifffile.imread( "./data_sliced/sliced_image_output_three/slice11.tif")


# In[13]:



# Display the MIP image
plt.imshow(img
           , cmap='gray')
plt.show()


# In[98]:


start_num = 1
dir_path = "./sliced-individial-folder/" + file_name_without_ext   # Replace with the actual directory path
print(dir_path)

extension = ".tif"

file_list = os.listdir(dir_path)
tif_list = [filename for filename in file_list if filename.endswith(extension)]

for i, filename in enumerate(tif_list):
    old_name = os.path.join(dir_path, filename)
    new_name = os.path.join(dir_path, f"img{start_num+i}{extension}")
    os.rename(old_name, new_name)


