def scan(input):

	directions =['north', 'south', 'east', 'west']
	verbs = ['go', 'kill', 'eat', 'punch', 'open']
	stops = ['the', 'in', 'of','through']
	nouns = ['bear', 'princess','face']
	
	split_up = input.split() 
	
	result = []
	
	for i in range(len(split_up)):

		if split_up[i].lower() in directions:
			result.append(("direction", split_up[i]))
			
		elif split_up[i].lower() in verbs:
			result.append(("verb", split_up[i]))
			
		elif split_up[i].lower() in stops:
			result.append(("stop", split_up[i]))
			
		elif split_up[i].lower() in nouns:
			result.append(("noun", split_up[i]))
	
		else:
			try:
				num = int(split_up[i])
				result.append(('number', num))
			except ValueError:
				result.append(('error', split_up[i]))

	return result