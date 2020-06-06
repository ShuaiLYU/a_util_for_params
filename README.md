# a_util_for_params

**自己写的一个工具类，方便管理和使用深度学习的各种超参数**

##  一些可用的初始化方法
```
	param=Param()
param.is_train=True
param.load_weight=True
param.data_name="ImageNet"
param.dataset=Param()
param.dataset.image_size=[224, 224]
param.dataset.channels=3
param.model=Param()
param.model.name="resnet18"
param.model.checkpoint="./checkpoint"
param.model.nomal="GN"
param.train=Param()
param.train.batch_size=64
param.train.epoch=1
param.train.optim=Param()
param.train.optim.name="SGD"
param.train.optim.lr=0.001
123
```

## 把参数打印出来看看
```
print (param)
```
***打印结果保存后，稍作修改就可以直接作为下次初始化的代码使用***  
param=Param()  
param.is_train=True  
param.load_weight=True  
param.data_name=ImageNet  
param.dataset=Param()  
param.dataset.image_size=[224, 224]  
param.dataset.channels=3  
param.model=Param()  
param.model.name=resnet18  
param.model.checkpoint=./checkpoint  
param.model.nomal=GN  
param.train=Param()  
param.train.batch_size=64  
param.train.epoch=1  
param.train.optim=Param()  
param.train.optim.name=SGD  
param.train.optim.lr=0.001  
