import math
import numpy as np
import h5py
import tensorflow as tf

def load_datasets():
    train_dataset=h5py.File('train_signs.h5',"r")
    test_dataset=h5py.File('test_signs.h5',"r")
    train_set_x_orig=np.array(train_dataset["train_set_x"][:])
    train_set_y_orig=np.array(train_dataset["train_set_y"][:])
    test_set_x_orig=np.array(test_dataset["test_set_x"][:])
    test_set_y_orig=np.array(test_dataset["test_set_y"][:])
    classes=np.array(test_dataset["list_classes"][:])
    train_set_y_orig=train_set_y_orig.reshape(1,train_set_y_orig.shape[0])
    test_set_y_orig=test_set_y_orig.reshape(1,test_set_y_orig.shape[0])
    return train_set_x_orig,test_set_x_orig,train_set_y_orig,test_set_y_orig,classes
def random_minibatchs(X,Y,minibatch=64,seed=0):
    np.random.seed(seed)
    m=X.shape[0]
    random_batch=[]
    permutation=list(np.random.permutation(m))
    shuffle_X=X[permutation,:,:,:]
    shuffle_Y=Y[permutation,:]
    net_batch=math.floor(m/minibatch)
    for k in range(net_batch):
        shuffle1_X=shuffle_X[k*minibatch:k*minibatch+minibatch,:,:,:]
        shuffle1_Y=shuffle_Y[k*minibatch:k*minibatch+minibatch,:]
        mini_batch=(shuffle1_X,shuffle1_Y)
        random_batch.append(mini_batch)
    if m%minibatch!=0:
        shuffle1_X=shuffle_X[minibatch*net_batch:m,:,:,:]
        shuffle1_Y=shuffle_Y[minibatch*net_batch:m,:]
        mini_batch=(shuffle1_X,shuffle1_Y)
        random_batch.append(mini_batch)
    return random_batch
def one_h_encoding(Y,C):
    Y=np.eye(C)[Y.reshape(-1)].T
    return Y
def forward_pass(X,parameters):
    W1=parameters["W1"]
    W2=parameters["W2"]
    W3=parameters["W3"]
    b1=parameters["b1"]
    b2=parameters["b2"]
    b3=parameters["b3"]
    
    Z1=tf.add(tf.matmul(W1,X),b1)
    A1=tf.nn.relu(Z1)
    Z2=tf.add(tf.matmul(W2,A1),b2)
    A2=tf.nn.relu(Z2)
    Z3=tf.add(tf.matmul(W3,A2),b3)
    return Z3
def predict(X, parameters):
    
    W1 = tf.convert_to_tensor(parameters["W1"])
    b1 = tf.convert_to_tensor(parameters["b1"])
    W2 = tf.convert_to_tensor(parameters["W2"])
    b2 = tf.convert_to_tensor(parameters["b2"])
    W3 = tf.convert_to_tensor(parameters["W3"])
    b3 = tf.convert_to_tensor(parameters["b3"])
    
    params = {"W1": W1,
              "b1": b1,
              "W2": W2,
              "b2": b2,
              "W3": W3,
              "b3": b3}
    
    x = tf.placeholder("float", [12288, 1])
    
    z3 = forward_pass(x, params)
    p = tf.argmax(z3)
    
    sess = tf.Session()
    prediction = sess.run(p, feed_dict = {x: X})
        
    return prediction
    
    
    