
# coding: utf-8

# In[31]:


class HebbRule:
    def __init__(self):
        self.b = 0
        self.w = {}
        self.score = 0
    
    def inisialisasi(self,inputs):
        for x in range(len(inputs[0])):
            self.w['w'+str(x)] = 0
    
    def train(self,inputs,label):
        self.inisialisasi(inputs)
        
        for input, target in zip(inputs,label):
            for index, x in enumerate(input):
                self.w['w'+str(index)] = self.w['w'+str(index)] + (x*target)
            self.b = self.b + target
        
        aktivasi = lambda x : 1 if x >= 0 else -1 #aktivasi bipolar
        benar = 0
        for input,target in zip(inputs,label):
            y_in = 0
            for index, x in enumerate(input):
                y_in = self.w['w'+str(index)]*x
            
            y_in = y_in + self.b
            
            if aktivasi(y_in) == target:
                benar = benar + 1
        
        self.score = benar / len(inputs)
    
    def predict(self,inputs):
        y_in = 0
        for index, x in enumerate(inputs):
            y_in = self.w['w'+str(index)]*x

        y_in = y_in + self.b
        aktivasi = lambda x : 1 if x >= 0 else -1 #aktivasi bipolar
        return aktivasi(y_in)
    
    def akurasi(self):
        return self.score


# In[1]:


X = [[-1,-1],[1,-1],[-1,1],[1,1]]
y = [-1,1,1,1]


# In[32]:


H = HebbRule()
H.train(X,y)
H.akurasi()
H.predict([-1,-1])

