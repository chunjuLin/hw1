# hw1
 how to setup and run your program:
 
	First of all we input the csv file into the python. While we are reading it row by row, 
	we input each row into a list called "data". Also, we judge that if the value of TEMP in 
	that row is -99 or -999.If is, we clear it by assign that blank as ''.I create another 
	list called "maximun" this list store the maximun value of TEMP of each assigned station.
	The initial value of the datas in "maximum" are all -999.So, while we are reading the 
	file, we also update the newest maximum value. Thus, after we finish reading the file, 
	we will get the maximum value of each assigned station.
	After reading the file, we have to out put our result. Because the number of assign station
	is 5, so I manually decide the output order. I create a function to print out the station 
	name and  the maximum value in correct format. If the maximum value is -999 we output None.
	Then we call the function for five times in lexicographical order. Finaly we will get the
	proper output as we want.
what are the results:

	for sample_input.csv:
	[['C0A880', 27.0], ['C0F9A0', 22.0], ['C0G640', 28.0], ['C0R190', 'None'], ['C0X260', 27.0]]
	for 108000216.csv:
	[['C0A880', 20.5], ['C0F9A0', 24.0], ['C0G640', 24.8], ['C0R190', 27.8], ['C0X260', 25.5]]
