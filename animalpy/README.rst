Animals.py
==========

*Created by Cesiyi and KsIsCute*

Animals.py is a Python library that provides animal-related functionalities, specifically for fetching random pictures and interesting facts.

Currently supported animals: "dog", "cat".

API
---

**animals.picture(animal_name: str) -> str**
  Returns a URL string for a picture of the specified animal.

  - Supported animals: "dog", "cat".
  - Raises `NotImplementedError` for other animals.

**animals.fact(animal_name: str) -> str**
  Returns a string containing a fact about the specified animal.

  - Supported animals for facts: "cat".
  - For "dog", it returns the string: "Dog facts are currently unavailable."
  - Raises `NotImplementedError` for other animals.


Examples
--------

First, import the `animals` class:

.. code:: py

   from animalpy import animals

**Get a dog picture URL:**

.. code:: py

   # Get a dog picture URL
   dog_pic_url = animals.picture("dog")
   print(dog_pic_url)

**Get a cat fact:**

.. code:: py

   # Get a cat fact
   cat_fact_text = animals.fact("cat")
   print(cat_fact_text)

**Get a dog fact (currently unavailable):**

.. code:: py

   # Get a dog fact (currently unavailable)
   dog_fact_status = animals.fact("dog")
   print(dog_fact_status) # Output: Dog facts are currently unavailable.

======= ==================
Version Support
======= ==================
>3.8.X  ✅
3.0+    ✅
2.7+    ❎
>2.6.X  ❎
======= ==================
