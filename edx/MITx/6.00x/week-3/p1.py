def myRange(start, stop, step):
	l = []
	s = start
	while s < stop:
		l.append(s)
		s += step
	return l

def radiationExposure(start, stop, step):
	exposure = 0

	for i in myRange(start, stop, step):
		exposure += step * f(i)
	return exposure


## test cases
import math
# Cobalt-60
def f(x): return 10*math.e**(math.log(0.5)/5.27 * x)
assert radiationExposure(0, 5, 1) == 39.10318784326239
assert radiationExposure(5, 11, 1) == 22.94241041057671
assert radiationExposure(12, 16, 1) == 6.848645835538622
# Radium-224
def f(x): return 400*math.e**(math.log(0.5)/3.66 * x)
assert radiationExposure(0, 4, 0.25) == 1148.6783342153556
assert radiationExposure(5, 10, 0.25) == 513.4662018628549
# Uranium-240
def f(x): return 200*math.e**(math.log(0.5)/14.1 * x)
assert radiationExposure(0, 3, 0.1) == 559.2259707824549
assert radiationExposure(14, 20, 0.1) == 523.4527522388149
assert radiationExposure(48, 72, 0.4) == 268.79947333082856
assert radiationExposure(72, 96, 0.4) == 82.61081970598813
# Cesium-138
def f(x): return 150*math.e**(math.log(0.5)/32.2 * x)
assert radiationExposure(0, 40, 1) == 4066.0849302266774
assert radiationExposure(100, 400, 4) == 843.5828023451531
assert radiationExposure(1000, 4000, 15) == 3.6525375905841067e-06
# Radon-220
def f(x): return 60*math.e**(math.log(0.5)/55.6 * x)
assert radiationExposure(0, 60, 0.5) == 2542.768831286683
assert radiationExposure(60, 120, 0.5) == 1203.5229215597114
assert radiationExposure(600, 1200, 5) == 2.799597134148232