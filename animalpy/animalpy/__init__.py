
import requests

__version__ = "0.1.5-1"
animallist = ["dog", "cat"] # Updated list

class animals:
    # __check_animal static method removed

    @staticmethod
    def _get_dog_picture_url():
        """
        Fetches a random dog picture URL from the dog.ceo API.
        """
        try:
            response = requests.get("https://dog.ceo/api/breeds/image/random")
            response.raise_for_status()  # Raise an exception for bad status codes
            data = response.json()
            if data.get("status") != "success" or "message" not in data:
                raise ValueError("Dog API did not return a successful response or 'message' key is missing.")
            return data['message']
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch dog picture: {e}")
        except (KeyError, ValueError) as e:
            raise Exception(f"Failed to parse dog picture API response: {e}")

    @staticmethod
    def _get_cat_picture_url():
        """
        Fetches a random cat picture URL from thecatapi.com API.
        """
        try:
            response = requests.get("https://api.thecatapi.com/v1/images/search")
            response.raise_for_status()
            data = response.json()
            if not data or not isinstance(data, list) or 'url' not in data[0]:
                raise ValueError("Invalid cat picture API response format.")
            return data[0]['url']
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch cat picture: {e}")
        except (ValueError, IndexError, KeyError) as e:
            raise Exception(f"Failed to parse cat picture API response: {e}")

    @staticmethod
    def _get_cat_fact_text():
        """
        Fetches a random cat fact from meowfacts.herokuapp.com.
        """
        try:
            response = requests.get("https://meowfacts.herokuapp.com/")
            response.raise_for_status()
            data = response.json()
            if not data or 'data' not in data or not isinstance(data['data'], list) or not data['data']:
                raise ValueError("Invalid cat fact API response format.")
            return data['data'][0]
        except requests.exceptions.RequestException as e:
            raise Exception(f"Failed to fetch cat fact: {e}")
        except (ValueError, IndexError, KeyError) as e:
            raise Exception(f"Failed to parse cat fact API response: {e}")

    @staticmethod
    def picture(animal: str):
        """
        Returns a picture URL of the animal.
        """
        animal_lower = animal.lower()
        # __check_animal is removed, so no call to it here.

        if animal_lower == "dog":
            return animals._get_dog_picture_url()
        elif animal_lower == "cat":
            return animals._get_cat_picture_url()
        else:
            # Since animallist is now only ["dog", "cat"], any animal reaching this else
            # is not supported. The previous distinction for animals in the broader list
            # is no longer applicable.
            raise NotImplementedError(f"Pictures for '{animal}' are not supported yet.")

    @staticmethod
    def fact(animal: str):
        """
        Returns a fact about the animal.
        """
        animal_lower = animal.lower()
        # __check_animal is removed, so no call to it here.

        if animal_lower == "cat":
            return animals._get_cat_fact_text()
        elif animal_lower == "dog":
            return "Dog facts are currently unavailable."
        else:
            # Similar to picture(), any animal reaching this else is not "dog" or "cat".
            raise NotImplementedError(f"Facts for '{animal}' are not supported yet.")
