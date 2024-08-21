# Dissertation 

This repository contains the code and some sample data related to the research project titled:

**"Can We Obtain Urban Land Use Data for Small Cities Using Limited Data Sources? An Exploratory Workflow Combining Semantic Segmentation and Unsupervised Clustering."**

Due to the large size of the image data used in this study, we are unable to store the entire dataset in this repository. However, we provide links to all datasets and other relevant GitHub projects that were helpful in our research. This README will guide you through the structure of the repository and the content of each directory.

## Repository Structure

### 1. Data Preparation

- **Folder:** `1_data_prepation`
- **Scripts:**
  - `1_image_format.ipynb`
  - `1_label_encoding.ipynb`
  - `1_training_validation.ipynb`

This section contains the code used to format and prepare the image data for training the semantic segmentation model. It also includes a few sample images to help users understand the directory structure. You can download the original dataset `WHU Building Dataset` from http://gpcv.whu.edu.cn/data/building_dataset.html.

### 2. Model Training Configuration

- **Folder:** `2_model_training/mmsegmentation`

This folder contains configuration files used during the training of the semantic segmentation model. The entire training process was conducted on a cloud platform: https://featurize.cn. 

And references the following projects:

https://mmsegmentation.readthedocs.io/en/latest/

https://github.com/TommyZihao/MMSegmentation_Tutorials

https://github.com/TommyZihao/Label2Everything

The actual training code is not included in this repository, but you can find the complete code in the linked projects. To replicate the experiments, simply copy the provided configuration files into the respective training code directories. 

Specifically, `MMSegmentation` is the semantic segmentation toolbox, `MMSegmentation_Tutorials` is the tutorial for using this toolbox, and `Label2Everything` is the dataset-related tools provided by the author of MMSegmentation_Tutorials. By applying the tutorial of MMSegmentation_Tutorials to the WHU Building Dataset and directly overwriting it with the file we provide when setting the corresponding configuration file, you can approximately reproduce the model training process.

### 3. Semantic Segmentation and Preprocessing for Clustering

- **Folder:** `3_semantic_segmentation`
- **Scripts:**
  - `3_combine.ipynb`
  - `3_crop.ipynb`

This folder includes the code and satellite imagery used for clustering analysis. The original satellite images were in TIF format and were too large to be included in this repository. Instead, we provide JPG versions for easier viewing. The provided scripts allow you to recreate the dataset used for the clustering analysis.

You can view these impacts directly in the Google Earth web version by visiting the link below:

https://earth.google.com/web/@40.4076213,118.96195672,223.8218898a,8213.85492339d,35y,-0h,0t,0r/data=OgMKATA

https://earth.google.com/web/@32.60503166,114.37261101,80.72503209a,5132.0452391d,35y,0h,0t,0r/data=OgMKATA

https://earth.google.com/web/@22.26569014,109.98470065,67.90108299a,4635.81617438d,35y,0h,0t,0r/data=OgMKATA

### 4. Unsupervised Clustering Analysis

- **Folder:** `4_unsupervised_clustering/bobai`
- **Script:**
  - `4_clustering.ipynb`

This folder contains the code for performing the unsupervised clustering analysis on the dataset created in the previous step. Applying this code to the prepared dataset will yield clustering results similar to those discussed in our paper. Due to the large size of the output images, we have only provided the full set of images from one experiment to help you understand the workflow.

## Data and External Resources

- **Training Dataset:**
- http://gpcv.whu.edu.cn/data/building_dataset.html


- **Satellite imagery:**
- [Google Earth](https://www.google.com/intl/en_uk/earth/about/)


- **Cloud Platform:**
- https://featurize.cn


- **Referenced Projects:**
- https://mmsegmentation.readthedocs.io/en/latest/
- https://github.com/TommyZihao/MMSegmentation_Tutorials
- https://github.com/TommyZihao/Label2Everything

## Acknowledgments

This research was greatly facilitated by the data and code made available by the above resources. We extend our thanks to the contributors of these projects.
