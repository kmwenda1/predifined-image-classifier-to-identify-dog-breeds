#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/classify_images.py
#
# PROGRAMMER: baraka koome
# DATE CREATED:  1st september                               
# REVISED DATE: 
# PURPOSE: Create a function classify_images that uses the classifier function 
#          to create the classifier labels and then compares the classifier 
#          labels to the pet image labels.
##
# Imports classifier function for using CNN to classify images 
from classifier import classifier 
from label_matching import is_label_match

def classify_images(images_dir, results_dic, model):
    """
    Creates classifier labels with classifier function, compares pet labels to 
    the classifier labels, and adds the classifier label and the comparison of 
    the labels to the results dictionary using the extend function.
    Parameters: 
      images_dir - The (full) path to the folder of images that are to be
                   classified by the classifier function (string)
      results_dic - Results Dictionary with 'key' as image filename and 'value'
                    as a List. Where the list will contain the following items: 
                  index 0 = pet image label (string)
                --- where index 1 & index 2 are added by this function ---
                  NEW - index 1 = classifier label (string)
                  NEW - index 2 = 1/0 (int)  where 1 = match between pet image
                    and classifer labels and 0 = no match between labels
      model - Indicates which CNN model architecture will be used by the 
              classifier function to classify the pet images,
              values must be either: resnet alexnet vgg (string)
     Returns:
           None - results_dic is mutable data type so no return needed.         
    """
    # Process each key (filename) in results_dic
    for key in results_dic:

        # Build full path to the image: images_dir + filename
        # (images_dir already ends with '/' when passed from check_images.py,
        # but adding it explicitly here guards against that not being the case)
        image_path = images_dir + key

        # Runs the classifier function on the image, returns raw classifier label
        model_label = classifier(image_path, model)

        # Formats classifier label: strip whitespace, lowercase
        model_label = model_label.lower()
        model_label = model_label.strip()

        # Gets pet image label already stored at index 0
        truth = results_dic[key][0]

        # Checks whether pet label matches as a whole word/phrase within the
        # classifier label string (which may be comma-separated synonyms)
        if is_label_match(truth, model_label):
            # Match found - add classifier label and match=1 to results_dic
            results_dic[key].extend((model_label, 1))
        else:
            # No match - add classifier label and match=0 to results_dic
            results_dic[key].extend((model_label, 0))