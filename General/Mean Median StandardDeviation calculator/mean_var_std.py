import numpy as np

def calculate(list):
  if len(list)!=9:
    raise ValueError('List must contain nine numbers.')
  else:
    list1=np.array(list)
    matrix=list1.reshape(3,3)
    
    mean_axis1=np.mean(matrix,axis=1).tolist()
    mean_axis0=np.mean(matrix,axis=0).tolist()
    mean_flat=np.mean(list)
    

    var_axis1=np.var(matrix,axis=1).tolist()
    var_axis0=np.var(matrix,axis=0).tolist()
    var_flat=np.var(list)

    stddev_axis1=np.std(matrix,axis=1).tolist()
    stddev_axis0=np.std(matrix,axis=0).tolist()
    stddev_flat=np.std(list)

    max_axis1=np.max(matrix,axis=1).tolist()
    max_axis0=np.max(matrix,axis=0).tolist()
    max_flat=np.max(list)

    min_axis1=np.min(matrix,axis=1).tolist()
    min_axis0=np.min(matrix,axis=0).tolist()
    min_flat=np.min(list)

    sum_axis1=np.sum(matrix,axis=1).tolist()
    sum_axis0=np.sum(matrix,axis=0).tolist()
    sum_flat=np.sum(list)

    calculations={
      'mean':[mean_axis0,mean_axis1,mean_flat],
      'variance':[var_axis0,var_axis1,var_flat],
      'standard deviation':[stddev_axis0,stddev_axis1,stddev_flat],
      'max':[max_axis0,max_axis1,max_flat],
      'min':[min_axis0,min_axis1,min_flat],
      'sum':[sum_axis0,sum_axis1,sum_flat]
    }
  
    return calculations