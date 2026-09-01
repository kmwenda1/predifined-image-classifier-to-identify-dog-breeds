#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# */AIPND-revision/intropyproject-classify-pet-images/get_pet_labels.py
#
# PROGRAMMER: baraka koome
# DATE CREATED:      1st september                            
# REVISED DATE: 
# PURPOSE: Create the function get_pet_labels that creates the pet labels from 
#          the image's filename.
##
# Imports python modules
from os import listdir

def get_pet_labels(image_dir):
    """
    Creates a dictionary of pet labels (results_dic) based upon the filenames 
    of the image files. These pet image labels are used to check the accuracy 
    of the labels that are returned by the classifier function, since the 
    filenames of the images contain the true identity of the pet in the image.
    Be sure to format the pet labels so that they are in all lower case letters
    and with leading and trailing whitespace characters stripped from them.
    (ex. filename = 'Boston_terrier_02259.jpg' Pet label = 'boston terrier')
    Parameters:
     image_dir - The (full) path to the folder of images that are to be
                 classified by the classifier function (string)
    Returns:
      results_dic - Dictionary with 'key' as image filename and 'value' as a 
      List. The list contains for following item:
         index 0 = pet image label (string)
    """
    # Retrieves list of filenames in the image folder
    in_files = listdir(image_dir)

    # Creates empty dictionary for the results_dic dictionary
    results_dic = dict()

    # Processes each filename in the image folder
    for idx in range(0, len(in_files), 1):

        # Skips hidden files (e.g. .DS_Store on Mac) that start with a dot
        if in_files[idx][0] != ".":

            # Splits filename on underscores; each word becomes a list item
            # e.g. 'Boston_terrier_02259.jpg' -> ['Boston', 'terrier', '02259.jpg']
            word_list_pet_image = in_files[idx].split("_")

            # Creates temporary label from all list items except the last one
            # (the last item is the numeric image ID + file extension)
            pet_label = ""
            for word in word_list_pet_image:
                if word.isalpha():
                    pet_label += word.lower() + " "

            # Strips trailing whitespace left over from the loop above
            pet_label = pet_label.strip()

            # If filename doesn't already exist in dictionary, add filename as 
            # 'key' and the pet_label as 'value' in a one-element list
            if in_files[idx] not in results_dic:
                results_dic[in_files[idx]] = [pet_label]
            else:
                print("** Warning: Key =", in_files[idx],
                      "already exists in results_dic with value =",
                      results_dic[in_files[idx]])

    # Replace None with the results_dic dictionary that you created with this
    # function
    return results_dic