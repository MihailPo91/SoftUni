# import unittest


class Time:
    max_hours = 23
    max_minutes = 59
    max_seconds = 59

    def __init__(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def set_time(self, hours, minutes, seconds):
        self.hours = hours
        self.minutes = minutes
        self.seconds = seconds

    def get_time(self):
        # if self.seconds < 10:
        #     self.seconds = f'0{self.seconds}'
        # if self.minutes < 10:
        #     self.minutes = f'0{self.minutes}'
        # if self.hours < 10:
        #     self.hours = f'0{self.hours}'

        return f'{self.hours:02d}:{self.minutes:02d}:{self.seconds:02d}'

    def next_second(self):
        self.seconds += 1
        if self.seconds > self.max_seconds:
            self.seconds = 0
            self.minutes += 1
            if self.minutes > self.max_minutes:
                self.minutes = 0
                self.hours += 1
                if self.hours > self.max_hours:
                    self.hours = 0
        return Time.get_time(self)


time = Time(9, 30, 59)
print(time.next_second())
time = Time(10, 59, 59)
print(time.next_second())
time = Time(23, 59, 59)
print(time.next_second())


# class Tests(unittest.TestCase):
#     def test_init(self):
#         t = Time(16, 35, 54)
#         self.assertEqual(t.hours, 16)
#         self.assertEqual(t.minutes, 35)
#         self.assertEqual(t.seconds, 54)
#
#     def test_class_attributes(self):
#         self.assertEqual(Time.max_hours, 23)
#         self.assertEqual(Time.max_minutes, 59)
#         self.assertEqual(Time.max_seconds, 59)
#
#     def test_set_time(self):
#         t = Time(1, 2, 3)
#         t.set_time(3, 2, 1)
#         self.assertEqual(t.hours, 3)
#         self.assertEqual(t.minutes, 2)
#         self.assertEqual(t.seconds, 1)
#
#     def test_get_time(self):
#         t = Time(1, 20, 30)
#         res = t.get_time()
#         self.assertEqual(res, "01:20:30")
#
#     def test_next_second_no_overflow(self):
#         t = Time(1, 20, 30)
#         res = t.next_second()
#         self.assertEqual(res, "01:20:31")
#
#     def test_next_second_minutes_overflow(self):
#         t = Time(1, 59, 59)
#         res = t.next_second()
#         self.assertEqual(res, "02:00:00")
#
#     def test_next_second_hours_overflow(self):
#         t = Time(23, 59, 59)
#         res = t.next_second()
#         self.assertEqual(res, "00:00:00")
#
#     def test_next_second(self):
#         t = Time(0, 0, 0)
#         res = t.next_second()
#         self.assertEqual(res, "00:00:01")
#
#
# if __name__ == "__main__":
#     unittest.main()