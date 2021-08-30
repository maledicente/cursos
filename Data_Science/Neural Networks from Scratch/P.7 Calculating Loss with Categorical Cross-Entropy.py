import numpy as np
import math

soft = [0.7,0.1,0.2,0.5]
target = [0,1,0,0]

loss = -(math.log(soft[0]) * target[0]+
		 math.log(soft[1]) * target[1]+ 
		 math.log(soft[2]) * target[2]+
		 math.log(soft[3]) * target[3])

print(loss)