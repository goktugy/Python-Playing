class Record:
    """Hold a record of data."""

john = {
    "name": "John Doe",
    "position": "Python Developer",
    "department": "Engineering",
    "salary": 80000,
    "hire_date": "2020-01-01",
     "is_manager": False,
}

if __name__ == "__main__":
    john_record = Record()
    for field, value in john.items():
        setattr(john_record, field, value)


    print(f"John's name is: {john_record.name}")
    print(f"John's department is: {john_record.department}")


