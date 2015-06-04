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


# Classifier Tree

+ Model Selection (C45, NBTree, ...) 
	>get all possible models and return the best model
+ is leaf or not
+ is empty or not
+ training set
+ pruing instances

## Build Tree
1. **Select Model** (key step)
2. If subsets number > 1  
	2.1 Split instances  
	2.2 Create New Classifier Tree Nodes for every subset instance.
3. If subsets number == 1  
	3.1 It's a leaf node

## Classify Instance
	Get the most prob class of the instance on the classifier tree

## Classifier Split Model   
(split to models on the parent model on an attribute)

+ Classify Instance

	get the max class of the subset which the instance belong to

+ Class Probability  (get class probability for instance)
+ Class Laplace Probability (relative frequency of class for given bag or over all bags)

## C45 Model Selection 
1. If the destribution all belong to one class or the number is too small, not enough to split    
	1.1 return no split model.
2. else for all attribute  
	2.1 build the split model. 
3. select the best split model  *(model.infoGain >= averageInfoGain - 1E-3  and the best gainRatio)*

## C45 Split Model
(implement a C45-type split on *an attribute*)
### Build Classifier
1. nominal attribute
2. numeric attribute  
	+ sort instance by attribute 
	+ by default, there are **2 distributions**
	+ get the mininum number of instances required in each subset (MIN(MAX(0.1 * instances / class number, minNoObj), 25) => minSplit
	+ find the split point which has the greatest info gain

## C45 Purneable Classifier Tree

#### Prune  (Post Prune)
> From down to top, recursive
estimated errors of current model <= estimated errors of all leaves node of current node

#### Collapse  (collapses a tree to a node(leaf) if training error doesn't increase)
> From top to down

incorrect number of current model - 1E-3 <= incorrect number of all leaves node of current node


# Random Forest
+ number of trees
+ number of features
+ max depth of the tree
+ number of execution slots
+ Bagger  
	+ classifiers
	+ votes:   
		+ numeric  
			sum all pred number for all classifiers / votes count
		+ nominal  
			sum all prob of class value for all classifier, select the max


# Ada Boost
+ UseResampling  (sample training data to build classifier)
+ Number of IterationsPerformed
+ Weight threshold
+ Train Data  (update every iteration by weight)

### iteration performed build and evaluate classifier
1. build classifier
2. evaluate classifier  
	+ if error too big or 0, return false, stop iteration
3. reweight  
	+ reweight = (1 - errorRate) / errorRate
	+ instance.weight = weight * reweight


# Naive Bayes
+ estimator  
  + numeric: KernelEstimator(Gaussian Kernel)/NormalEstimator
  + nominal: DiscreteEstimator
+ precision used for numeric attributes = sum of intervals / count of intervals, default = 0.01
+ discretize
+ P(c|X) = P(c) * P(X|c) <= P(c) * P(x1|c) * P(x2|c) * ... * P(x3|c)