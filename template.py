"""
    This is the python sample code for evaluation of the Daejeon520 dataset. In this dataset, we provide 259040 
    database images and 4000 queries. You can use any algorithm for extracting global features of images and then 
    retrieving. What we expected from you before using this template is:
    
    1. You have the retrieval result, i.e. an a rank list for each query with element of rank list is names of images 
    in the database
    
    2. The length of the rank list is not restricted, but I recommend 20-50 (i.e. only first 50 images with highest 
    similarity score)
    
    Please note that the main purpose of this template code is just for understanding the dataset. You can use it as the
    vanila code in your experiment and optimize (or re-implement) it later after certainly understanding the convention
    of the dataset. 

    We also remind that the format of images name is "panoramaid_X" with X from 0 to 7. Images with same panorama ID are
    at the same location
"""


"""
    This function is for loading the annotation file
    @Input: annotation file (csv) as described in readme
    @Output: dictionary with key is panorama id of query and value is set  of correct panorama id in the database
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

"""
    This function is for creating true-false array from the rank list 
    @Input: query name
            rank list of the query
            groundtruth dictionary
    @Output: A array with same size of the rank list with 1 indicates correct image and 0 indicate wrong image
"""

def judge_prediction(query_name, rank_list, ref):
    result = []
    index = query_name[:-2] # e.x. the query is _YThQHzjAXlJsFVGbbYrOpA_0 -> panoramaid is _YThQHzjAXlJsFVGbbYrOpA
    for item in rank_list:
        if item[:-2] in ref[index]:
            result.append(1)
        else:
            result.append(0)
    return np.array(result)

"""
    This function is for calcualating the recall
    @Input: preds - 2D array with:
                - number of row is the number of query
                - each row is the prediction after being judged of the query (0-1 array)
    @Output: recall - recall of the retrieval alogrimth w.r.t. the dataset
"""
def compute_recall(preds)
    recall_preds = []
    for pred in preds:
        recall_pred = []
        first_correct = 0
        for item in pred:
            if item == 1:
                for i in range(first_correct, len(pred)):
                    recall_pred.append(1)
                break
            else:
                recall_pred.append(0)
                first_correct += 1
        recall_preds.append(np.array(recall_pred))
    top_retrieval = preds.shape[1]
    num_query = pred.shape[0]
    recall = np.array([0]*top_retrieval)
    for recall_pred in recall_pred:
        recall += recall_pred
    recall = recall/float(num_query)
    print(recall)
    return recall