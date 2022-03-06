from project.student_report_card import StudentReportCard

from unittest import TestCase, main


class StudentReportCardTest(TestCase):
    def setUp(self):
        self.student_card = StudentReportCard('Pesho', 10)

    def test_student_initialization(self):
        expected_grades = {}
        self.assertEqual('Pesho', self.student_card.student_name)
        self.assertEqual(10, self.student_card.school_year)
        self.assertEqual(expected_grades, self.student_card.grades_by_subject)

    def test_student_name_property_if_empty_should_raise_an_Exception(self):
        with self.assertRaises(ValueError) as ex:
            self.student_card.student_name = ''

        self.assertEqual("Student Name cannot be an empty string!", str(ex.exception))

    def test_student_name_property_with_valid_name_should_return_value(self):
        new_name = "Gosho"
        self.student_card.student_name = new_name
        self.assertEqual(new_name, self.student_card.student_name)

    def test_school_year_property_with_value_under_and_over_the_given_range_should_raise_Exception(self):
        for year in [0, 13]:
            with self.assertRaises(ValueError) as ex:
                self.student_card.school_year = year
            self.assertEqual("School Year must be between 1 and 12!", str(ex.exception))

    def test_school_year_with_proper_values_should_return_values(self):
        for year in range(1, 13):
            self.student_card.school_year = year
            self.assertEqual(year, self.student_card.school_year)


    def test_add_grade_to_grades_should_update_the_dict(self):
        new_subject = "Math"
        grade = 5.90
        grade2 = 3

        self.assertIsInstance(grade, float)
        expected_dict = {new_subject: [grade]}
        new_dict = {new_subject: [grade, grade2]}

        self.student_card.add_grade(new_subject, grade)
        self.assertEqual(expected_dict, self.student_card.grades_by_subject)
        self.student_card.add_grade(new_subject, grade2)
        self.assertEqual(new_dict, self.student_card.grades_by_subject)
        self.assertTrue(grade in self.student_card.grades_by_subject[new_subject])
        self.assertTrue(grade2 in self.student_card.grades_by_subject[new_subject])

    def test_average_grade_by_subject(self):
        new_subject = "Math"
        grade = 5.90
        expected_dict = {new_subject: [grade]}
        new_grade = 5.00

        self.student_card.add_grade(new_subject, grade)
        self.assertEqual(expected_dict, self.student_card.grades_by_subject)

        self.student_card.add_grade(new_subject, new_grade)

        new_dict = {new_subject: [grade, new_grade]}
        self.assertEqual(new_dict, self.student_card.grades_by_subject)

        subject2 = "Physics"
        grade2 = 5.20
        grade3 = 4.30

        self.student_card.add_grade(subject2, grade2)
        self.student_card.add_grade(subject2, grade3)
        expected_new_dict = {new_subject: [grade, new_grade], subject2: [grade2, grade3]}
        self.assertEqual(expected_new_dict, self.student_card.grades_by_subject)

        expected_report = f"{new_subject}: {(grade + new_grade) / 2:.2f}\n" \
                          f"{subject2}: {(grade2 + grade3) / 2:.2f}"

        result = self.student_card.average_grade_by_subject()
        self.assertEqual(expected_report, result)

    def test_average_grade_for_all_subjects(self):
        new_subject = "Math"
        grade = 5.90
        expected_dict = {new_subject: [grade]}
        new_grade = 5.00
        grades1 = [grade, new_grade]
        self.student_card.add_grade(new_subject, grade)
        self.assertEqual(expected_dict, self.student_card.grades_by_subject)

        self.student_card.add_grade(new_subject, new_grade)

        new_dict = {new_subject: [grade, new_grade]}
        self.assertEqual(new_dict, self.student_card.grades_by_subject)

        subject2 = "Physics"
        grade2 = 5.20
        grade3 = 4.30

        grades2 = [grade2, grade3]
        self.student_card.add_grade(subject2, grade2)
        self.student_card.add_grade(subject2, grade3)

        expected_count = len(grades1) + len(grades2)
        expected_sum = sum(grades1) + sum(grades2)
        expected_result = f"Average Grade: {expected_sum / expected_count :.2f}"
        result = self.student_card.average_grade_for_all_subjects()
        self.assertEqual(expected_result, result)

    def test_repr(self):
        new_subject = "Math"
        grade = 5.90
        new_grade = 5.00
        self.student_card.add_grade(new_subject, grade)
        self.student_card.add_grade(new_subject, new_grade)

        subject2 = "Physics"
        grade2 = 5.20
        grade3 = 4.30

        self.student_card.add_grade(subject2, grade2)
        self.student_card.add_grade(subject2, grade3)

        expected_count = 4
        expected_sum = grade + new_grade + grade2 + grade3
        expected_result = f"Average Grade: {expected_sum / expected_count :.2f}"
        expected_report = f"{new_subject}: {(grade + new_grade) / 2:.2f}\n"
        expected_report += f"{subject2}: {(grade2 + grade3) / 2:.2f}"

        report = f"Name: {'Pesho'}\n" \
                 f"Year: {10}\n" \
                 f"----------\n" \
                 f"{expected_report}\n" \
                 f"----------\n" \
                 f"{expected_result}"

        self.assertEqual(report, repr(self.student_card))


if __name__ == '__main__':
    main()
