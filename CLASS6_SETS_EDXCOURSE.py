import sys
# Create a set

set1 = {"pop", "rock", "soul", "hard rock", "rock", "R&B", "rock", "disco"}
print(type(set1))
# Convert list to set

album_list = [ "Michael Jackson", "Thriller", 1982, "00:42:19",
              "Pop, Rock, R&B", 46.0, 65, "30-Nov-82", None, 10.0]
album_set = set(album_list)             #here you are converting the  list to a set
print(album_set)
# Convert list to set

music_genres = set(["pop", "pop", "rock", "folk rock", "hard rock", "soul",
                    "progressive rock", "soft rock", "R&B", "disco"])
# Sample set

A = set(["Thriller", "Back in Black", "AC/DC"])
#Add an elemnet
A.add("NSYNC")
print(A)

# Try to add duplicate element to the set

A.add("NSYNC")#you cant since its already there inside the set

#Remove element from the set
A.remove("NSYNC")
print(A)

# Verify if the element is in the set
print("AC/DC" in A)

# Sample Sets

album_set1 = set(["Thriller", 'AC/DC', 'Back in Black'])
album_set2 = set([ "AC/DC", "Back in Black", "The Dark Side of the Moon"])
# Find the intersections BETWEEN BOTH SETS

intersection = album_set1 & album_set2
print(intersection)
# Find the difference in set1 but not set2

print(album_set1.difference(album_set2) )#aqui daria thriller porque no esta en en 1
print(album_set2.difference(album_set1) )#aqui daria the dark side of the moon porque no esta en en 2 con respecto ao 1
# Use intersection method to find the intersection of album_list1 and album_list2

print(album_set1.intersection(album_set2))
# Find the union of two sets

print('este',album_set1.union(album_set2))

# Check if superset

set(album_set1).issuperset(album_set2)  #this will check if album_set1 is a superset of albumset2, since is not will
#return False

print(set(album_set2).issuperset(album_set1)) #this will check if album_set2 is a superset of albumset1, since is not will
#return False
# Check if subset

print(set({"Back in Black", "AC/DC"}).issubset(album_set1))
# Check if superset

print(album_set1.issuperset({"Back in Black", "AC/DC"}))