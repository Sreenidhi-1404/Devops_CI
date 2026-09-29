class Student:
    def __init__(self, student_id, name):
        self.student_id = student_id
        self.name = name


class Bus:
    def __init__(self, bus_number, capacity):
        self.bus_number = bus_number
        self.capacity = capacity
        self.students = []

    def add_student(self, student):
        if len(self.students) < self.capacity:
            self.students.append(student)
            return True

        return False

    def is_full(self):
        return len(self.students) >= self.capacity
    
    def get_available_seats(self):
        return self.capacity - len(self.students)
    def get_student_count(self):
        return len(self.students)

class TransportAllocation:

    def allocate_student(self, student, bus):
        return bus.add_student(student)