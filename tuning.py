#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import os 
accuracy = os.system("cat /root/model.txt | grep accuracy")
ep = os.system("cat /root/model.txt | grep ep")
optx = os.system("cat /root/model.txt | grep optx")
if accuracy < 90:
    
while accuracy<90:
    x1 = os.popen("cat /root/mymodel.py | grep model.add | wc -l")
    x = x1.read()
    x = x.rstrip()
    x = int(x)
    optx_new='adam'
    if x==1:
        y = 'model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                       ))
            model.add(MaxPooling2D(pool_size=(2, 2)))"))'
    elif x==2:
        y = 'model.add(Convolution2D(filters=32, 
                        kernel_size=(3,3), 
                        activation='relu',
                       ))
            model.add(MaxPooling2D(pool_size=(2, 2)))"))'
    elif x==3:
        y = 'model.add(Dense(units=50, activation=\"relu\"))'
    elif x==4:
        y = 'model.add(Dense(units=25, activation=\"relu\"))'
    else:
        print("unable to add")
        
    os.system("sed -i '/n=0/{}}' /root/mymodel.py".format(y))
    os.system("sed -i '/{}/{}+1' /root/mymodel.py".format(ep))
    os.system("sed -i '/{}/{}' /root/mymodel.py".format(optx,optx_n))
    os.system("http://192.168.43.26:8080/job/Training_the_ML_code/build?token=moonwalker")
    accuracy = os.system("cat /root/mlops_ws/modeltuning.txt | grep accuracy")
    accuracy = float(accuracy)
    print(accuracy)
    
else:
    print("ACCURACY ABOVE 90%")


# In[ ]:




