
import random
import numpy as np



class LinearRegressionSingleVariable:

	def __init__(self): #constructor
		# initializing random weights
		self.w0 = random.random()
		self.w1 = random.random()
		# setting learning rate to 0.01
		self.learning_rate = 0.01

	def difference(self,y_pred,y): #this function returns the arithmetic difference between two numbers
		return (y_pred - y)

	def hypothesis_function(self,x): #this function predicts the outcome by using current weight values
		return self.w0 + (self.w1*x)



	def train(self,X,y): #this function takes as input an input array(Single variable) and actual outputs
		epochs = 1000
		for j in range(epochs):
			for i in range(len(X)):
				y_pred = self.hypothesis_function(X[i])
				self.w0 = self.w0 - self.learning_rate*2* self.difference(y_pred,y[i])
				self.w1 = self.w1 - self.learning_rate*X[i]*2* self.difference(y_pred,y[i])*X[i]
		pass
 	
	def set_learning_rate(self,lr): #this function sets the learning rate to the value passed as a parameter
		learnin_rate = lr

	
	def predict(self,X): #predict function takes as input an array and predicts the outcomes from those inputs
		
		results = []
		
		for x in X:
			results.append(int(self.hypothesis_function(x)))

		return results


X = [1,2,3,4,5]
y = [2,4,6,8,10] 

model = LinearRegressionSingleVariable() 

#training the model
model.train(X,y)

# predicting
print(model.predict([45,60,22,75]))
