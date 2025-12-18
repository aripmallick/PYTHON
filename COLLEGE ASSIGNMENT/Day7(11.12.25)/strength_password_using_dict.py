classes = {'class1': 45, 'class2': 30, 'class3': 60}
min_class = min(classes, key=classes.get)
print("Minimum strength:", min_class, classes[min_class])
max_class = max(classes, key=classes.get)
print("Maximum strength:", max_class, classes[max_class])