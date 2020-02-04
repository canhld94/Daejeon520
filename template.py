"""
    This is the python sample code for evaluation of the Daejeon520 dataset. In this dataset, we provide 259040 
    database images and 4000 queries. You can use any algorithm for extracting global features of images and then 
    retrieving. What we expected from you before using this template is:
    
    1. You have the retrieval result, i.e. an a rank list for each query with element of rank list is names of images 
    in the database
    
    2. The length of the rank list is not restricted, but I recommend 50 (i.e. only first 50 images with highest 
    similarity score)
    
    We also remind that the format of images name is "panoramaid_X" with X from 0 to 7. Images with same panorama ID are
    at the same location
"""


"""
    This function is for loading the annotation file
    @Input: the annotation file (csv) as described in readme
    @Output: a dictionary with key is panorama id of query and value is set  of correct panorama id in the database
"""

def load_annotation_file(ref_file):
    with open(ref_file) as f:
        contents = f.readlines()
    lines = [x.strip('\n') for x in contents]
    ref = dict()
    for line in lines:
        tup = line.split(',')
        ref[tup[0]] = set(tup[1:])
    return ref

This function is for creating true-false array from the rank list 
@Input:
@Output:

def judge_prediction(query_name, rank_list, ref):
    result = []
    index = query_name[:-2]
    for item in rank_list:
        if item[:-2] in ref[index]:
            result.append(1)
        else:
            result.append(0)
    return result

This function is for 