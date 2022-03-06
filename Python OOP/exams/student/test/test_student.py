from unittest import TestCase, main

from project.student import Student


class StudentTest(TestCase):
    def setUp(self):
        self.course_name = "Python"
        self.default_notes = ['n1', 'n2']
        self.student = Student('Pesho', {self.course_name: self.default_notes})

    def test_student_initialize_with_courses(self):
        self.assertEqual('Pesho', self.student.name)
        self.assertEqual({'Python': ['n1', 'n2']}, self.student.courses)

    def test_student_initialize_without_courses(self):
        student = Student('Pesho', None)
        self.assertEqual('Pesho', student.name)
        self.assertEqual({}, student.courses)

    def test_enroll_should_extend_notes_for_already_enrolled_course(self):
        new_courses = ['n3', 'n4']
        expected = self.default_notes + new_courses
        result = self.student.enroll(self.course_name, new_courses)

        self.assertEqual('Course already added. Notes have been updated.', str(result))
        self.assertTrue(self.course_name in self.student.courses)
        self.assertEqual(expected, self.student.courses[self.course_name])

    def test_enroll_should_add_course_and_its_notes_to_student(self):
        for idx, command in enumerate(['', "Y"]):
            course_name = f'JavaScript{idx}'
            result = self.student.enroll(course_name, ['Random Js', 'Explorer'], command)
            self.assertEqual('Course and course notes have been added.', result)
            self.assertTrue(course_name in self.student.courses)

    def test_enroll_without_add_course_notes_should_add_course_without_notes(self):
        course_name = "JavaScript"
        course_notes = ["random JS", "Explorer"]
        result = self.student.enroll(course_name, course_notes, 'N')
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course_name in self.student.courses)
        self.assertEqual([], self.student.courses[course_name])

    def test_add_notes_should_raise_error_when_student_is_not_enrolled_for_the_given_course(self):
        course_name = "JavaScript"

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course_name, ['JS1', "JS2"])

        self.assertEqual('Cannot add notes. Course not found.', str(ex.exception))

    def test_add_notes_should_raise_error_when_student_is_enrolled_for_the_given_course(self):
        new_note = 'random note'
        expected_notes = [x for x in self.default_notes]
        expected_notes.append(new_note)
        result = self.student.add_notes(self.course_name, new_note)

        self.assertEqual('Notes have been updated', result)
        self.assertEqual(expected_notes, self.student.courses[self.course_name])

    def test_leave_course_should_raise_error_when_student_is_not_in_the_the_given_course(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course("JavaScript")

        self.assertEqual('Cannot remove course. Course not found.', str(ex.exception))

    def test_leave_course_should_remove_given_course(self):
        self.student.enroll('JavaScript', [])
        expected_courses_count = len(self.student.courses) - 1
        result = self.student.leave_course(self.course_name)
        self.assertEqual('Course has been removed', result)
        self.assertTrue(self.course_name not in self.student.courses)
        self.assertEqual(expected_courses_count, len(self.student.courses))


if __name__ == '__main__':
    main()
