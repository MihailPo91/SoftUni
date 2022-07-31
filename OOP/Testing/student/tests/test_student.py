import unittest

from project.student import Student


class TestStudent(unittest.TestCase):
    STUDENT_NAME = 'Pesho'

    def setUp(self) -> None:
        self.student = Student(self.STUDENT_NAME)

    def test_student_init_without_courses(self):
        self.assertEqual(self.STUDENT_NAME, self.student.name)
        self.assertEqual({}, self.student.courses)

    def test_student_init_with_courses(self):
        courses = {'Python OOP': ['note1', 'note2']}
        student = Student(self.STUDENT_NAME, courses)
        self.assertEqual(self.STUDENT_NAME, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll__student_updates_course_notes_when_course_is_enrolled(self):
        course_name = 'Python OOP'
        courses = {course_name: ['note1', 'note2']}

        student = Student(self.STUDENT_NAME, courses)

        result = student.enroll(course_name, ['note3', 'note4'])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(['note1', 'note2', 'note3', 'note4'], student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_and_notes_when_add_course_notes_is_passed(self):
        course_name = 'Python Advanced'
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes)
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_and_notes_when_add_course_notes_is_Y(self):
        course_name = 'Python Advanced'
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes, 'Y')
        expected = "Course and course notes have been added."

        self.assertEqual(expected, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual(course_notes, self.student.courses[course_name])

    def test_enroll__student_extends_courses_with_course_without_notes_when_invalid_add_notes_arg_passed(self):
        course_name = 'Python Advanced'
        course_notes = ['note1', 'note2']
        result = self.student.enroll(course_name, course_notes, 'N')
        expected = "Course has been added."

        self.assertEqual(expected, result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes__raises_error_when_course_does_not_exist(self):
        with self.assertRaises(Exception) as error:
            self.student.add_notes('Python OOP', 'note123')

        self.assertEqual("Cannot add notes. Course not found.", str(error.exception))

    def test_add_notes__when_course_exists__expect_to_add_note_correctly(self):
        course_name = 'Python OOP'
        student = Student(self.STUDENT_NAME, {course_name: ['n1', 'n2']})

        result = student.add_notes(course_name, 'n3')

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(['n1', 'n2', 'n3'], student.courses[course_name])

    def test_leave_course__when_course_not_existing__expect_to_raise(self):
        with self.assertRaises(Exception) as error:
            self.student.leave_course('Python OOP')

        self.assertEqual("Cannot remove course. Course not found.", str(error.exception))

    def test_leave_course__when_course_exists__expect_to_pop_course_from_data(self):
        course_name = 'Python OOP'
        student = Student(self.STUDENT_NAME, {course_name: ['n1', 'n2']})

        result = student.leave_course(course_name)
        self.assertEqual("Course has been removed", result)
        self.assertEqual({}, student.courses)







