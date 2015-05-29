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

	>+ ClassValue   //the class value 0R predicts
	>+ Counts array  //the number of instances in each class

	1. Nominal (mode)

		classValue = max(Sum(classValue1.Weight), Sum(classValue2.Weight), ... , Sum(classValueN.Weight))

		nomalize counts to 0-1

	2. Numeric (mean)

		classValue = Sum(classValue * Weight) / Sum(Weight)

2. [OneR](http://www.saedsayad.com/oner.htm)

	*"generate one rule for each predictor in the data, then selects the rule with the smallest total error as its 'one rule'."*

	+ OneRRule  ***for storing a oneR rule***

		>+ Class Attribute
		>+ Instances Number
		>+ Rule Attribute
		>+ Correct Number ***(get the oneRRule which has max correct number as the Rule)***
		>+ Classifications  *(prediected class for each value of attr)*
		>+ MissingValueClass  *(the classValue when the attributeValue is missing)*
		>+ BreakPoints *(numeric attributes only, intervalUpperBound)*  

	+ ZeroR *(only class attribute)*
	+ Minimum bucket size  *default is 6*

	1. Nominal Rule

		+ count classValue missing count for the rule attribute  
		+ count per attributeValue per classAttribute  
		+ class of the attributeValue is the max count of the classAttribute

	2. Numeric Rule

		+ count classValue missing count for the rule attribute
		+ order by attributeValue
		+ gather intervals and count classValue for every interval. {intervalUpperBound | intervalUpperBound = (lastAttributeValue + curAttributeValue) / 2.0 or intervalUpperBound = MAX_VALUE}   //split the range
		+ should we merge adjacent intervals ? if same class(max classValue count) || classValueCount in the interval < Minimum bucket size
		+ scan again, if same class, merge adjacent intervals
		+ create rule: the class of one interval is the max classValue count, BreakPoint is the upper bound of the interval



	