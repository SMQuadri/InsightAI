class TrackableObject:
    
	def __init__(self, objectID, centroid):

		self.objectID = objectID
		self.centroids = [centroid]

		self.counted = False