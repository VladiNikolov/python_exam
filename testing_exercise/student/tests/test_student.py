from unittest import TestCase, main

from project.student import Student


class StudentTests(TestCase):
    def setUp(self) -> None:
        self.student = Student("Vladimir", {
            "Python_Basic": ["note1", "note2"],
            "Python_Fundamentals": ["note3", "note4"]
        })

    def test_correct_init(self):
        student = Student("Vladimir")
        self.assertEqual("Vladimir", student.name)
        self.assertEqual({}, student.courses)

    def test_correct_init_with_courses(self):
        name = "Vladimir"
        courses = {
            "Python_Basic": ["note1", "note2"],
            "Python_Fundamentals": ["note3", "note4"]
        }

        student = Student(name, courses)
        self.assertEqual(name, student.name)
        self.assertEqual(courses, student.courses)

    def test_enroll_with_already_enrolled_course_add_note_to_the_course(self):
        result = self.student.enroll("Python_Basic", ["new_note"])

        self.assertEqual("Course already added. Notes have been updated.", result)
        self.assertEqual(["note1", "note2", "new_note"], self.student.courses["Python_Basic"])

    def test_enrol_add_new_courses_whit_new_notes(self):
        course = "Python_Advance"
        notes = ["note5", "note6"]

        result = self.student.enroll(course, notes, "Y")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enrol_add_new_courses_whit_new_notes_and_empty_string(self):
        course = "Python_Advance"
        notes = ["note5", "note6"]

        result = self.student.enroll(course, notes, "")
        self.assertEqual("Course and course notes have been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual(notes, self.student.courses[course])

    def test_enrol_add_new_course_without_notes(self):
        course = "Python_Advance"

        result = self.student.enroll(course, ["note5", "note6"], "N")
        self.assertEqual("Course has been added.", result)
        self.assertTrue(course in self.student.courses)
        self.assertEqual([], self.student.courses[course])

    def test_add_notes_to_existing_course(self):
        course = "Python_Basic"
        result = self.student.add_notes(course, "extra_note")

        self.assertEqual("Notes have been updated", result)
        self.assertEqual(["note1", "note2", "extra_note"], self.student.courses[course])

    def test_add_notes_to_missing_course_rises(self):
        course = "Python_OOP"

        with self.assertRaises(Exception) as ex:
            self.student.add_notes(course, "notes")
        self.assertEqual("Cannot add notes. Course not found.", str(ex.exception))

    def test_leave_course(self):
        course = "Python_Basic"
        result = self.student.leave_course(course)

        self.assertEqual("Course has been removed", result)
        self.assertTrue(course not in self.student.courses)

    def test_remove_course_if_course_not_existing(self):
        course = "Python_OOP"

        with self.assertRaises(Exception) as ex:
            self.student.leave_course(course)
        self.assertEqual("Cannot remove course. Course not found.", str(ex.exception))


if __name__ == "__main__":
    main()