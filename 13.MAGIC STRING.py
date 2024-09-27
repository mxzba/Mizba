from datetime import datetime
import unittest

class RecyclingData:
    def _init_(self, recycling_id: int, material_type: str, amount: float, date=None):
        self.recycling_id = recycling_id
        self.material_type = material_type
        self.amount = amount  # Amount in kg or units
        self.date = date if date else datetime.now()

    def _repr_(self):
        return f"RecyclingData(ID={self.recycling_id}, Material={self.material_type}, Amount={self.amount}, Date={self.date})"


class RecyclingTracker:
    def _init_(self):
        self.data = {}

    def add_recycling_data(self, recycling_data: RecyclingData):
        if not isinstance(recycling_data, RecyclingData):
            raise TypeError("Expected a RecyclingData object.")
        # Add the recycling data to the dictionary with recycling_id as the key
        self.data[recycling_data.recycling_id] = recycling_data

    def get_recycling_data(self, recycling_id: int):
        return self.data.get(recycling_id)

    def get_all_recycling_data(self):
        return list(self.data.values())


# Unit tests
class TestRecyclingTracker(unittest.TestCase):
    def setUp(self):
        self.tracker = RecyclingTracker()

    def test_add_recycling_data(self):
        data = RecyclingData(1, 'Plastic', 10.5)
        self.tracker.add_recycling_data(data)
        self.assertEqual(self.tracker.get_recycling_data(1), data)

    def test_add_invalid_data(self):
        with self.assertRaises(TypeError):
            self.tracker.add_recycling_data("Not a RecyclingData object")

    def test_get_all_recycling_data(self):
        data1 = RecyclingData(1, 'Plastic', 10.5)
        data2 = RecyclingData(2, 'Glass', 5.0)
        self.tracker.add_recycling_data(data1)
        self.tracker.add_recycling_data(data2)
        all_data = self.tracker.get_all_recycling_data()
        self.assertEqual(len(all_data), 2)
        self.assertIn(data1, all_data)
        self.assertIn(data2, all_data)

if _name_ == "_main_":
    unittest.main()