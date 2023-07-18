Graph Processing

To get the input for the Graph Processing Assignment the ConnectedComponents.java was run using Hadoop Map Reduce with the arguments seen below: 

	Hadoop jar /Users/pragatwagle/Desktop/Hadoop/CC/ccomps.jar ConnectedComponents /	hwtwo/CC/input /hwtwo/CC/output : ,

The only reason I bring this up is so show the delimiters used as these delimiters were hardcoded in the CCFinalRound.java file. Colon was used as a delimiter between the component id and the list of adjacent node id’s. A comma was used to separate the adjacent list of nodes. For example 

	6	0:5,7,8
	NodeId	CompId:AdjListOfNodeIds’

The colon and commands were directly hardcoded into the CCFinalRound.java file. I just wanted to point that out to explain how the line was parsed. The output from the mapper for the line above was 0\t6. The 0 represents the component id and 6 the node id. This was done for all lines in the input.txt file, which was the output from the ConnectedComponents.java. It is in the zip archive. Then the intermediary step sorted and grouped all lines by the key component id and put all the values or node ids into a Iterable<Text>. These values were used as the arguments for the reducer. In the reducer a HashSet was used to save only distinct node id values was then outputted by the reducer into an output file with an example line seen below.

	 0		0, 4, 5, 6, 7, 8, 9

0 represents the component id and the values after the tab are the node ids’ that belong in component 0.

The IMPROVEMENT I would make is to allow the delimiters’ to be passed in using the command line. 



