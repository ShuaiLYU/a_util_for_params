#!/usr/bin/env python3
# -*- coding: utf-8 -*-
# @Time    : 2019/12/12 8:31
# @Author  : Wslsdx
# @FileName: param.py
# @Software: PyCharm
# @Github  ：https://github.com/Wslsdx
class Param(object):
	def __init__(self,**kargs):
		self._name="param"
		self.regist_from_dict(kargs)

	def regist_from_parser(self,parser):
		for key,val in parser.__dict__.items():
			self.__setitem__(key, val)

	def regist_from_dict(self,_dict):
		assert isinstance(_dict,dict)
		for key,val in _dict.items():
			self.__setitem__(key, val)

	def regist(self, key, val):
		self.__setitem__(key, val)

	def update_name(self,last_name,key):
		self._name=last_name+"."+key
		for key,val in self.__dict__.items():
			if isinstance(val,Param):
				val.update_name(self._name,key)
	# 功能 A["a"]
	def __setitem__(self, key, value):
		super(Param,self).__setattr__( key, value)
		if isinstance(value,Param):
			value.update_name(self._name,key)
		#self.__dict__[key] = value
	def __getitem__(self, attr):
		return super(Param, self).__getattribute__(attr)
	def __delitem__(self, key):
		try:
			del self.__dict__[key]
		except KeyError as k:
			return None

	# 功能  A.a
	def __setattr__(self, key, value):
		super(Param,self).__setattr__( key, value)
		if isinstance(value,Param):
			value.update_name(self._name,key)
		#self.__dict__[key] = value
	def __getattribute__(self, attr):
		return super(Param, self).__getattribute__(attr)
	def __getattr__(self, attr):
		"""
		重载此函数防止属性不存在时__getattribute__报错，而是返回None
		那“_ getattribute_”与“_ getattr_”的最大差异在于：
		1. 无论调用对象的什么属性，包括不存在的属性，都会首先调用“_ getattribute_”方法；
		2. 只有找不到对象的属性时，才会调用“_ getattr_”方法；
		:param attr:
		:return:
		"""
		return None
	def __delattr__(self, key):
		try:
			del self.__dict__[key]
		except KeyError as k:
			return None
	# def __str__(self):
	# 	string=""
	# 	for key,val in self.__dict__.items():
	# 		if key is "_name": continue
	# 		if isinstance(val,Param):
	# 			string += self._name + "{}=Param()\n".format(key)
	# 			string +="{}".format(val)
	# 		else:
	# 			string +=self._name+"{}={}\n".format(key,val)
	# 	return string
	def __str__(self):
		string=self._name + "=Param()\n"
		for key,val in self.__dict__.items():
			if key is "_name": continue
			if isinstance(val,Param):
				string +=str(val)
			else:
				if isinstance(val,str): val='''"{}"'''.format(val)
				string +=self._name+".{}={}\n".format(key,val)
		return string
	def __len__(self):
		return len(self.__dict__)


	def keys(self):
		return self.__dict__.keys()

	def values(self):
		return self.__dict__.values()
	def items(self):
		return self.__dict__.items()

	def get(self,key,default):
		if key in self.keys():
			return self[key]
		else:
			return default

if __name__=="__main__":


	#
	param=Param()
	param["is_train"]=True
	param.load_weight=True
	param.regist("data_name","ImageNet")

	param.dataset=Param()
	param.dataset.image_size=[224,224]
	param.dataset.channels =3

	param.model=Param(name="resnet18",checkpoint="./checkpoint",nomal="GN")

	param.train=Param()
	param.train.regist_from_dict({"batch_size":64,"epoch":1})

	param.train.regist("optim",Param(name="SGD",lr=0.001))

	#打印参数
	print (param)
	#
	print(param.get('''123''',123))

