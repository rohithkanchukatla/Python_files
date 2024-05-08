class Student:
    scores = [65, 75, 85, 95]

    def average_score(self):
        total = 0
        for score in self.scores:
            total += score
        return total / len(self.scores)

# Creating an instance of the Student class
student_instance = Student()

# Calling the average_score method on the instance
result = student_instance.average_score()

print(result)
