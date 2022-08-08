#  Створіть клас робота пилососа
# Робот пилосос має класові атрибути - обєм баку для сміття, обєм баку води
# self атрибути - заповненість баку для сміття, заповненість баку для води, заряд батареї, серія/номер (ідентифікатор)
# Заряд батареї у відсотках
# заповнення баків для води і сміття - число
# наприклад
# Обєм баку для сміття - 1500
# заповнений обєм - 340
#  Реалізувати проперті - info, яке повертає інформацію про поточний стан робота
# Приклад
# "VR-1234183; power - 95%; water tank - 35%; trash tank - 76%
# де VR-1234183 - серія/номер
import logging
import random
from unittest import TestCase
import self


class LowBattery(BaseException):
    pass


class FullWasteTank(BaseException):
    pass


class EmptyWaterTank(BaseException):
    pass


class RobotVacuumCleaner:
    """Робот пилосос має класові атрибути - об`єм баку для сміття, об`єм баку води"""
    volume_waste_tank = 200
    volume_water_tank = 200

    def __init__(self, filling_waste_tank, filling_water_tank, battery_charge, identifier):
        self.v_filling_waste_tank = None
        self.filling_waste_tank = int(filling_waste_tank)
        self.filling_water_tank = int(filling_water_tank)
        self.battery_charge = battery_charge
        self.identifier = str(identifier)
        if self.battery_charge > 100 or self.battery_charge < 0:
            raise ValueError('battery_charge  must be between 0 and 100')
        if self.filling_waste_tank > self.volume_waste_tank or self.filling_waste_tank < 0:
            raise ValueError('filling_waste_tank must be between 0 and 200')
        if self.filling_water_tank > self.volume_water_tank or self.filling_water_tank < 0:
            raise ValueError('filling_water_tank must be between 0 and 200')

    @property
    def info(self):
        filling_waste_tank_percentage = (
                                                self.volume_waste_tank - self.filling_waste_tank) * 100 / self.volume_waste_tank
        filling_water_tank_percentage = (
                                                self.volume_water_tank - self.filling_water_tank) * 100 / self.volume_water_tank

        return (f"{self.identifier}, left {self.battery_charge}% battery charge, "
                f"left {filling_water_tank_percentage}% water tank,"
                f" left {filling_waste_tank_percentage}% waste tank")

    def reducing_charge(self):
        """робить перевірку якщо 5% і менше - кидає ексепшн LowBattery
        якщо більше 5% - зменшує відсоток батареї на 2%
"""
        if self.battery_charge < 5:
            raise LowBattery
            print('LowBattery')
        else:
            self.battery_charge -= 2
            print('Hahaha')

    def filling_wt(self, volume_waste_tank):
        additional_waste_volume = random.randint(0, 20)
        if self.filling_waste_tank == volume_waste_tank:
            raise FullWasteTank
        elif self.filling_waste_tank + additional_waste_volume >= self.volume_waste_tank:
            self.filling_waste_tank = self.volume_waste_tank
        else:
            self.filling_waste_tank += additional_waste_volume

    def wet_cleaning(self):
        if self.filling_water_tank == 0:
            raise EmptyWaterTank
        elif self.filling_water_tank:
            self.filling_water_tank -= 20
            if self.filling_water_tank < 0:
                self.filling_water_tank = 0
                raise EmptyWaterTank

    def start_cleaning(self, time, wet_cleaning):
        logging.info(f"{self.info} STARTED CLEANING")
        for x in range(time):
            try:
                self.battery_charge()
                self.filling_wt()
            except LowBattery:
                logging.error("LowBattery")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            except FullWasteTank:
                logging.error("FullWasteTank")
                logging.info(f"{self.info} FINISHED CLEANING")
                return False
            if wet_cleaning:
                try:
                    self.wet_cleaning()
                except EmptyWaterTank:
                    logging.error("EmptyWaterTank")
                    return False
        logging.info(f"{self.info} FINISHED CLEANING")
        return True


robot = RobotVacuumCleaner(50, 100, 80, 'Xiaomy 360')
print(robot.info)
print(robot.filling_wt(200))
print(robot.wet_cleaning())
# використовуючи бібліотеки unittest або pytest треба перевірити:
# 1. повне прибирання на яке вистачає ресурсів
# 2.прибирання без вологого прибирання на яке вистачає ресурсів
# 3. прибирання під час якого не вистачило заряду батареї
# (перевірити що start_cleaning повернула False і що заряд батареї 0%)
# 4. прибирання під час якого заповнився сміттє бак (перевірити що start_cleaning повернула False і що сміттєбак повний)
# 5. прибирання під час якого не вистачило води (перевірити що start_cleaning повернула False і що бак з водою пустий)
# 6. проперті info повертає правильне значення



class TestRobotVacuumCleaner(TestCase):

    def setUp(self) -> None:
        self.test_cleaner = RobotVacuumCleaner(0, 100, 100, "test_series")
        print(self.test_cleaner.info)

    def test_tearDown(self) -> None:
        self.test_cleaner = None

    def test_full_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(True, 20))

    def test_dry_cleaning(self):
        self.assertTrue(self.test_cleaner.start_cleaning(False, 20))

    def test_battery_low(self):
        self.test_cleaner.battery_charge = 20
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.battery_charge, 0)

    def test_full_waster(self):
        self.test_cleaner.filling_waste_tank = self.test_cleaner.volume_waste_tank - 100
        self.assertFalse(self.test_cleaner.start_cleaning(False, 25))
        self.assertEqual(self.test_cleaner.filling_waste_tank, self.test_cleaner.volume_waste_tank)

    def test_no_water(self):
        self.test_cleaner.filling_water_tank = 50
        self.assertFalse(self.test_cleaner.start_cleaning(True, 25))
        self.assertEqual(self.test_cleaner.filling_water_tank, 0)

    def test_info(self):
        info = "identifier; power - 100%; water tank - 100%; waste tank - 0%"
        self.assertEqual(self.test_cleaner.info, info)
