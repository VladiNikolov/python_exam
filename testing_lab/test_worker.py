class Worker:

    def __init__(self, name, salary, energy):
        self.name = name
        self.salary = salary
        self.energy = energy
        self.money = 0

    def work(self):
        if self.energy <= 0:
            raise Exception('Not enough energy.')

        self.money += self.salary
        self.energy -= 1

    def rest(self):
        self.energy += 1

    def get_info(self):
        return f'{self.name} has saved {self.money} money.'

# --------------------------------------------------------------------------------------


from unittest import TestCase, main


class WorkerTest(TestCase):

    def test_init_correct(self):
        worker = Worker("test_name", 500, 100)
        self.assertEqual("test_name", worker.name)
        self.assertEqual(500, worker.salary)
        self.assertEqual(100, worker.energy)
        self.assertEqual(0, worker.money)

    def test_worker_work_whit_zero_energy_raises(self):
        worker = Worker("test_name", 500, 0)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_work_whit_negative_energy_raises(self):
        worker = Worker("test_name", 500, -1)

        with self.assertRaises(Exception) as ex:
            worker.work()
        self.assertEqual('Not enough energy.', str(ex.exception))

    def test_worker_increase_money_by_his_salary_correctly(self):
        worker = Worker("test_name", 500, 100)

        # Before
        self.assertEqual(0, worker.money)
        worker.work()
        # After
        self.assertEqual(500, worker.money)

    def test_worker_decrease_energy_after_work(self):
        worker = Worker("test_name", 500, 100)

        # Before
        self.assertEqual(100, worker.energy)
        worker.work()
        # After
        self.assertEqual(99, worker.energy)

    def test_energy_is_increased_after_rest(self):
        worker = Worker("test_name", 500, 100)

        # Before
        self.assertEqual(100, worker.energy)
        worker.rest()
        # After
        self.assertEqual(101, worker.energy)

    def test_prop_string_return_correct_value(self):
        worker = Worker("test_name", 500, 100)
        worker.money = 10

        result = worker.get_info()
        self.assertEqual('test_name has saved 10 money.', result)


if __name__ == '__main__':
    main()