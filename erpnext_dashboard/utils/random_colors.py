'''
'''

from randomcolor import RandomColor

def update_random_colors(results):
	
	'''
		results should be dict items
		for eg. : [{"item": 1}, ...]
	'''
	color = RandomColor()

	for res in results:
		res.update({"color": color.generate()[0]})

	return results
	
