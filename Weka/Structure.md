#Instances#
>*an ordered set of weighted instances*


	+ dataset name   //relation name
	+ attribute array
	+ instance array
	+ class attribute's index //indicate which attribute is class attribute, type could be nominal, numeric, date

numClasses:  the number of class labels. if nominal, is label number, otherwise, 1


#Instance#
>*interface*



#Attribute#
+ Attribute type:

	+ numeric  //default, no attribute info
	+ nominal  //fixed set of nominal values
	+ string   //dynamically expanding set of nominal values
	+ date
	+ relational //this type of attribute can contain other attributes and is used for representing Multi-Instance data

+ Attribute Weight   //default 1.0
+ Attribute Index    //default -1
+ Attribute Info 
	+ NominalAttributeInfo    //for nominal and string type
	+ DateAttributeInfo       //for date type
	+ RelationAttributeInfo   //for relational type,   **information is Instances(header and list)**
+ Attribute MetaInfo
	+ Ordering(symbolic, ordered, modulo-ordered), IsRegular, IsAveragable, HasZeropoint, LowerBound, LowerBoundIsOpen, UpperBound, UpperBoundIsOpen, MetaData