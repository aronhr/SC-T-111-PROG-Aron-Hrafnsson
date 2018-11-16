s1 = {1, 2, 3, 4, 5, 6, 7, 8, 9, 10}
s2 = {1, 3, 5, 7, 9}
s3 = {2, 4, 6, 8, 10}

print("Union s1 s2: ", s1.union(s2))
print("Union s2 s3:", s2.union(s3))
print("Intersection s1 s2:", s1.intersection(s2))
print("Intersection s2 s3:", s2.intersection(s3))
print("difference", s1.difference(s2))
print("difference", s2.difference(s3))
print("difference_update", s1.difference_update(s2))
print("difference_update", s2.difference_update(s3))
print("issubset", s3.issubset(s2))
print("issubset", s2.issubset(s3))

