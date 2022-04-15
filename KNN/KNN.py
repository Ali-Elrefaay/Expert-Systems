# -*- coding: utf-8 -*-
"""
Created on Thu Apr 14 17:59:46 2022

@author: Emad Elshplangy
"""



"""
Dataset Attributes Description: 1. Age of patient at time of operation (numerical)
                                2. Patient's year of operation (year - 1900, numerical)
                                3. Number of positive nodes detected (numerical)
                                4. Survival status (class attribute)
                                     1 = the patient survived 5 years or longer
                                     2 = the patient died within 5 year
"""


# sample list
samples = []
with open('haberman.data', 'r') as f:
    for line in f.readlines():
        attributes = line.replace('\n', '').split(',')
        # converting items from the list of attributes (string to integer)
        samples.append([int(attribute) for attribute in attributes])

def dataset_info(samples, verbose=True):
    # Displaying number of samples
    if verbose:
        print("Number of samples: {}".format(len(samples)))
    
    # initializing the counting variables for each label
    label_1, label_2 = 0, 0
    for sample in samples:
        if sample[-1] == 1:
            label_1 += 1
        else:
            label_2 += 1
    
    # displaying the number of samples of each label
    if verbose:
        print('Number of Samples of Label 1: {}'.format(label_1))
        print('Number of Samples of Label 2: {}'.format(label_2))
    
    # return a tuple with the number of samples and the number of samples of each label
    return len(samples), label_1, label_2

# unpacking return tuple of dataset_info function
_, label_1, label_2 = dataset_info(samples, verbose=True)

# proportion of the dataset to include in the train split (60%)
p = 0.6
# Initializing the test and training samples list
train, test = [], []

# Calculating the maximum amount of training samples per label
max_label_1, max_label_2 = int(p * label_1), int(p * label_2)

# Total amount of training samples
total_of_train_samples = max_label_1 + max_label_2

# Initializing labels counters
count_label_1, count_label_2 = 0, 0

for sample in samples:
    # If the sum of the counters is less than the total amount of training samples
    if (count_label_1 + count_label_2) < (total_of_train_samples):
        # Adding sample to training set
        train.append(sample)
        if (sample[-1] == 1) and (count_label_1 < max_label_1):
            count_label_1 += 1
        else:
            count_label_2 += 1
    else:
        # Adding sample to list of test set
        test.append(sample)
        
        
        
# Displaying information about test and training samples
print('----------------------------------')
print('Train Samples')
dataset_info(train)
print('----------------------------------')
print('Test Samples')
dataset_info(test)
print('----------------------------------')



import math

def euclidian_distance(v1, v2):
    # Getting vector 1 size and initializing summing variable 
    length, summation = len(v1), 0

    # Adding the square of the difference of the values of the two vectors
    for i in range(length - 1):
        # Adding the square of the difference of the values of the two vectors
        summation += math.pow(v1[i] - v2[i], 2)

    # Returning the square root of the sum
    return math.sqrt(summation)



# testing euclidian_distance function
v1 = [1, 2, 3]
v2 = [2, 1, 5]
euclidian_distance(v1,v2)



def knn(train, new_sample, K):
    # Initializing dict of distances and variable with size of training set
    distances, train_length = {}, len(train)

    # Calculating the Euclidean distance between the new
    # sample and the values of the training sample
    for i in range(train_length):
        d = euclidian_distance(train[i], new_sample)
        distances[i] = d
    
    # Selecting the K nearest neighbors
    k_neighbors = sorted(distances, key=distances.get)[:]
    
    # Initializing labels counters
    label_1, label_2 = 0, 0
    for index in k_neighbors:
        if train[index][-1] == 1:
            label_1 += 1
        else:
            label_2 += 1
    if label_1 > label_2:
        return 1
    else:
        return 2    
    
    
# Testing kNN function
print("New sample \n{}".format(test[12]))
print("Label: %d" %(test[12][3]))
print('---------------------------')
print("kNN return ")
print('Label: {}'.format(knn(train, test[12], K=13)))

# Initializing hit counter
hit_counter = 0
# Performing kNN on all test samples
for sample in test:
    label = knn(train, sample, K=13)
    # Comparing method result with actual sample result
    if sample[-1] == label:
        hit_counter += 1
        
print('Number of train samples: %d' % len(train))
print('Number of test samples: %d' % len(test))
print('Total of hits: %d' % hit_counter)
print('Number of hits (Percentage): %.2f%%' % (100 * hit_counter / len(test)))






    




























    
