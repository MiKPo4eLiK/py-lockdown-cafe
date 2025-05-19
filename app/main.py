from errors import VaccineError, NotWearingMaskError
from cafe import Cafe

def go_to_cafe(friends: list, cafe: Cafe):
    masks_needed = 0

    for friend in friends:
        try:
            cafe.visit_cafe(friend)
        except VaccineError:
            return "All friends should be vaccinated"
        except NotWearingMaskError:
            masks_needed += 1

    if masks_needed:
        return f"Friends should buy {masks_needed} masks"

    return f"Friends can go to {cafe.name}"


import datetime

friends = [
    {
        "name": "Alice",
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": True
    },
    {
        "name": "Bob",
        "vaccine": {"expiration_date": datetime.date.today()},
        "wearing_a_mask": False
    }
]

cafe = Cafe("KFC")
print(go_to_cafe(friends, cafe))
