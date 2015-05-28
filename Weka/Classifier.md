# Classifier Interface
+ Build Classifier
+ Classify Instance

	*classifies the given test instance*


+ Distribution For Instance

	*Predicts the class memberships for a given instance*

+ Get Capatibilies


# Rules
1. [ZeroR](http://www.saedsayad.com/zeror.htm)

	*"it is useful for determining a baseline performance as a benchmark for other classification methods."*

		+ ClassValue   //the class value 0R predicts
		+ Counts array  //the number of instances in each class

	1. Nominal (mode)

		classValue = max(Sum(classValue1.Weight), Sum(classValue2.Weight), ... , Sum(classValueN.Weight))

		nomalize counts to 0-1

	2. Numeric (mean)

		classValue = Sum(classValue * Weight) / Sum(Weight)