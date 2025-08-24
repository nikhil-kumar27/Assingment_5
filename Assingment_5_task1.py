marks={
    'nikhil':85,
    'jhon':78,
    'gyan':89,
    'doraemon':82
}
student=(input('Enter the student name:')).lower()
if(student in marks):
    print(f"{student}'s marks : {marks[student]}")
else:
    print('Student not found!')    
            