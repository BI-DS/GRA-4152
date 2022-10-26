#######################################
## EXAMPLE: Exceptions and lists
#######################################
def get_stats(class_list):
    new_stats = []
    for person in class_list:
        new_stats.append([person[0], person[1], avg(person[1])])
    return new_stats 

# avg function: version without an exception
def avg(grades):
    return (sum(grades))/len(grades)
    
test_grades = [[['peter', 'parker'], [80.0, 70.0, 85.0]], 
              [['bruce', 'wayne'], [100.0, 80.0, 74.0]],
              [['captain', 'america'], [80.0, 70.0, 96.0]],
              [['deadpool'], []]]

print(get_stats(test_grades))
