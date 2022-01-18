# from abc import ABC, abstractmethod
from datetime import datetime


class OrchestrationRecoverableException(Exception):
	"""Retrying"""
	pass

class OrchestrationUnrecoverableException(Exception):
	"""Exceeded the orderItem limit"""
	pass

class FileNotFoundError(Exception):
	"""File Not Found"""
	pass

#OBJECTS

#Order object
class Order:
  def __init__(self, id):
    self.id = id
    self.itemCount = 0
    self.totalAmnt = 0

  def addOrderItem(self):
    self.itemCount += 1

  def get_itemCount(self):
  	return self.itemCount

#OrderItem object
class OrderItem:
  def __init__(self, id, orderId, qty, unitPrice, provDate):
    self.id = id
    self.orderId = orderId
    self.qty = qty
    self.unitPrice = unitPrice
    self.totalPrice = self.qty * self.unitPrice
    self.provDate = provDate
    





# #It suppose to be an abstract method(inferface), however it is not able to get the ABC attribute for some reason
# class OrchestrationTask(abc.ABC):
class OrchestrationTask:
	# @abc.abstractmethod
	def executeBach(self, orderList):
		pass

class AssetManagementTask(OrchestrationTask):

    def executeBach(self, orderList):
        #Checking each OrderItem 
        try:
        	#Going through all the orderitems
	        for x in orderItemObjs:
	        	#Going through the provided ID list
	        	for y in orderList:
	        		#Checking if the current orderItem orderId is matching with the provided one(do we need to perform the changes for it)
	        		if x.orderId == y:
			        	#Adjusting the ProvDate to the Current Date
			        	x.provDate=datetime.now().date()

			        	#Going through the OrderObjects and for the matching ones adjusting the totalAmnt + adding the +1 to the itemCount
			        	for z in orderObjs:
			        		if z.id == x.orderId:
			        			z.addOrderItem()
			        			z.totalAmnt = z.totalAmnt + x.totalPrice
			        		#If the itemcount exceeds the limit raising the exception
			        		if z.get_itemCount() > 20:
			        			raise OrchestrationUnrecoverableException()

        except OrchestrationUnrecoverableException:
        	print("Exceeded the orderItem limit")
        #Exception for all other uknown errors        	
        except OrchestrationRecoverableException:
        	print("Unknown error")

        

#Exporting the file with Orderitems
class ReadFile():
	def read(self):
		try:
			exportedItemList = []
			with open("file.txt") as file_in:
			    for line in file_in:
			    	lines = []
			        lst = line.split(', ')
			        lines.append(int(lst[0]))
			        lines.append(int(lst[1]))
			        lines.append(int(lst[2]))
			        lines.append(float(lst[3]))
			        #Converting string dates to date type
			        lines.append(datetime.strptime(lst[4], '%m-%d-%Y').date())
			        exportedItemList.append(lines)
			return exportedItemList
		except FileNotFoundError:
			print('Sorry, "file.txt" File Not Found')





exportedItemList = ReadFile().read()

#Making a list of orderitem objects
orderObjs = list()
orderItemObjs = list()
for i in exportedItemList:
    orderItemObjs.append(OrderItem(i[0],i[1],i[2],i[3],i[4]))

#Making a list of order objects
    orderExists = False
    for x in orderObjs:
    	if x.id == i[1]:
    		orderExists = True
    if orderExists == False:
    	orderObjs.append(Order(i[1]))



#Creating the test list of orderIds, passing it to system
orderIdsToTest=[0,1]
asset = AssetManagementTask()
run = asset.executeBach(orderIdsToTest)
