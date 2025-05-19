# Lab Work 4: Task 1
# Version: 1.0
# Developer: Belavusau Anton
# Date: May 10, 2025

import csv
import pickle

class Subscriber:
    """Class to represent a phone book subscriber."""
    def __init__(self, name: str, phone: str):
        self._name = name
        self._phone = phone

    @property
    def name(self) -> str:
        """Get subscriber's name."""
        return self._name

    @property
    def phone(self) -> str:
        """Get subscriber's phone number."""
        return self._phone

    def __str__(self) -> str:
        """String representation of the subscriber."""
        return f"Name: {self._name}, Phone: {self._phone}"

class PhoneBook:
    """Class to manage a phone book."""
    def __init__(self):
        self.subscribers = []

    def add_subscriber(self, subscriber: Subscriber):
        """Add a subscriber to the phone book."""
        self.subscribers.append(subscriber)

    def save_to_csv(self, filename: str):
        """Save phone book to CSV file."""
        try:
            with open(filename, 'w', newline='', encoding='utf-8') as f:
                writer = csv.writer(f)
                writer.writerow(['Name', 'Phone'])
                for sub in self.subscribers:
                    writer.writerow([sub.name, sub.phone])
        except IOError as e:
            print(f"Error saving to CSV: {e}")

    def save_to_pickle(self, filename: str):
        """Save phone book to pickle file."""
        try:
            with open(filename, 'wb') as f:
                pickle.dump(self.subscribers, f)
        except IOError as e:
            print(f"Error saving to pickle: {e}")

    def load_from_csv(self, filename: str):
        """Load phone book from CSV file."""
        try:
            with open(filename, 'r', encoding='utf-8') as f:
                reader = csv.reader(f)
                next(reader) 
                self.subscribers = [Subscriber(row[0], row[1]) for row in reader]
        except IOError as e:
            print(f"Error loading from CSV: {e}")

    def load_from_pickle(self, filename: str):
        """Load phone book from pickle file."""
        try:
            with open(filename, 'rb') as f:
                self.subscribers = pickle.load(f)
        except IOError as e:
            print(f"Error loading from pickle: {e}")

    def search_by_phone_prefix(self, prefix: str) -> list:
        """Search subscribers by phone number prefix."""
        return [sub for sub in self.subscribers if sub.phone.startswith(prefix)]