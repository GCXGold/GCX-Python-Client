# Copyright 2016 GCX LTD https://www.gcx.io
# 
# Python bindings for connecting to the GCX API
#


import requests
import json

class gcx:
	def signup(self,email,username,password):
		request = requests.post("https://api.gcx.io/signup",data={"email":email,"username":username,"password":password})
		return json.loads(request.text)

	def verify(self,email_verification):
		request = requests.post("https://api.gcx.io/verifyemail",data={"email_verification":email_verification})
		return json.loads(request.text)

	def login(self,username,password):
		request = requests.post("https://api.gcx.io/login",data={"username":username,"password":password})
		return json.loads(request.text)

	def getbalance(self,trader_id):
		request = requests.post("https://api.gcx.io/get_balancex",data={"trader_id":trader_id})
		return json.loads(request.text)

	def getbids(self):
		request = requests.get("https://api.gcx.io/orders/getbids")
		return json.loads(request.text)

	def getasks(self):
		request = requests.get("https://api.gcx.io/orders/getasks")
		return json.loads(request.text)

	def withdrawfiat(self,trader_id,amount):
		request = requests.post("https://api.gcx.io/withdrawfiat",data={"trader_id":trader_id,"amount":amount})
		return json.loads(request.text)

	def getorders(self,trader_id):
		request = requests.post("https://api.gcx.io/orders",data={"trader_id":trader_id})
		return json.loads(request.text)

	def cancelorder(self,trader_id,oid):
		request = requests.post("https://api.gcx.io/orders",data={"trader_id":trader_id,"oid":oid})
		return json.loads(request.text)

	def trade(self,trader_id,shares,price,bidask,order):
		request = requests.post("https://api.gcx.io/trade",data={"trader_id":trader_id,"shares":shares,"price":price,"bidask":bidask,"order":order})
		return json.loads(request.text)

	def emailgold(self,trader_id,recipient,amount):
		request = requests.post("https://gcx.io/emailgold.php",data={"trader_id":trader_id,"recipient":recipient,"amount":amount})
		return json.loads(request.text)

	def smsgold(self,trader_id,mobile,amount):
		request = requests.post("http://gcx.io/smsgold.php",data={"trader_id":trader_id,"mobile":mobile,"amount":amount})
		return json.loads(request.text)











