>>I have came across the concept of functions, classes, error handling in python.
>>I have a small doubt in when to use the logging.

---

## 📝 Mini Practice

Try this small exercise:

Write a function that cleans a list of names.

Use a list comprehension to remove empty names.

Put the logic inside a class called NameCleaner.

Add exception handling for bad input.
--

>>import logging

logging.basicConfig(level=logging.INFO)
logger = logging.getLogger(__name__)

class NameCleaner:
    def __init__(self, names):
        self.names = names

    def clean_names(self):
        try:
            if not isinstance(self.names, list):
                raise TypeError("Input must be a list")

            cleaned = [name.strip().title() for name in self.names if isinstance(name, str) and name.strip()]
            logger.info("Names cleaned successfully")
            return cleaned

        except Exception as e:
            logger.exception(f"Error while cleaning names: {e}")
            return []

names = ["  rahul ", "", "sita", "  anil", None, "pRiYa  "]
cleaner = NameCleaner(names)
print(cleaner.clean_names())

--


>>- Task 2 .
Today goal is to how the api connnects and send the request  and receives the response.                                                                                                                                                  
Learning:-
while sending the api requet in header we need to who you are it verified by our api key and also what we are sending . is it json or html or what else.



---