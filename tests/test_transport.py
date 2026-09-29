import unittest

from src.transport import Student
from src.transport import Bus
from src.transport import TransportAllocation


class TestStudent(unittest.TestCase):

    def test_student_creation(self):
        student = Student("S001", "Rahul")

        self.assertEqual(student.student_id, "S001")
        self.assertEqual(student.name, "Rahul")


class TestBus(unittest.TestCase):

    def test_add_student(self):
        bus = Bus("B01", 2)

        student = Student("S001", "Rahul")

        result = bus.add_student(student)

        self.assertTrue(result)
        self.assertEqual(len(bus.students), 1)


    def test_bus_capacity(self):
        bus = Bus("B02", 1)

        student1 = Student("S001", "Rahul")
        student2 = Student("S002", "Arun")

        self.assertTrue(bus.add_student(student1))
        self.assertFalse(bus.add_student(student2))
    def test_has_available_seat(self):
        bus = Bus("B04", 2)

        student = Student("S004", "Kavin")

        bus.add_student(student)

        self.assertTrue(bus.has_available_seat())


class TestTransportAllocation(unittest.TestCase):

    def test_allocate_student(self):
        bus = Bus("B03", 2)

        student = Student("S003", "Priya")

        allocation = TransportAllocation()

        result = allocation.allocate_student(student, bus)

        self.assertTrue(result)


if __name__ == "__main__":
    unittest.main()