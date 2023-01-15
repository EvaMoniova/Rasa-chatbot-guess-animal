from typing import Any, Text, Dict, List
from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
from rasa_sdk.events import SlotSet
import random


class ActionGuessing(Action): 
    def name(self) -> Text:
        return "action_guessing"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        random_animal_check = tracker.get_slot("animal")
        if (random_animal_check not in ["snake", "shark", "tiger", "frog", "wasp"]):

            animal_list = ["snake", "shark", "tiger", "frog", "wasp"]

            random_animal = random.choice(animal_list)

            return [SlotSet(key="animal", value=random_animal)]
        else:
            pass


class ActionColourAsk(Action): 
    def name(self) -> Text:
        return "action_colour_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        colour_dict = {"snake": "brown",
                      "shark": "grey",
                      "tiger": "orange",
                      "frog": "green",
                      "wasp": "yellow"}

        asked_colour = tracker.get_slot("colour")  
        random_animal = tracker.get_slot("animal")

        dispatcher.utter_message(
            text=f"You wanted to know if the animal was {asked_colour}.")

        if asked_colour in colour_dict[random_animal]:
            dispatcher.utter_message(
                text=f"You were right, it is {asked_colour}.")
        else:
            dispatcher.utter_message(
                text=f"And my answer is: it is not {asked_colour}. Try again.")


class ActionBodypartsAsk(Action): 

    def name(self) -> Text:
        return "action_bodyparts_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        bodyparts_dict = {"snake": "scales",
                          "shark": "fin",
                          "tiger": "fur",
                          "frog": "legs",
                          "wasp": "sting"}
        asked_bodyparts = tracker.get_slot("bodyparts")  
        random_animal = tracker.get_slot("animal")

        dispatcher.utter_message(
            text=f"You wanted to know if the animal had {asked_bodyparts}.")
        if asked_bodyparts in bodyparts_dict[random_animal]:
            dispatcher.utter_message(
                text=f"And I say: yes, it has {asked_bodyparts}.")
        else:
            dispatcher.utter_message(
                text=f"It does not have {asked_bodyparts}. Try again")


class ActionBehaviourAsk(Action): 

    def name(self) -> Text:
        return "action_behaviour_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        behaviour_dict = {"snake": "crawl",
                         "shark": "swim",
                         "tiger": "roar",
                         "frog": "jump",
                         "wasp": "fly"}

        asked_behaviour = tracker.get_slot("behaviour")  
        random_animal = tracker.get_slot("animal")
        dispatcher.utter_message(
            text=f"You wanted to know if the animal {asked_behaviour}ed.")

        if asked_behaviour in behaviour_dict[random_animal]:
            dispatcher.utter_message(
                text=f"Yes, the animal does {asked_behaviour}.")
        else:
            dispatcher.utter_message(
                text=f"No, the animal does not {asked_behaviour}. Try again.")


class ActionAnimalAsk(Action): 

    def name(self) -> Text:
        return "action_animal_ask"

    def run(self,
            dispatcher: CollectingDispatcher,
            tracker: Tracker,
            domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:

        animal_name = tracker.get_slot("animal")
        guessed_animal_name = tracker.get_slot("guessed_animal")
        dispatcher.utter_message(
            text=f"You wanted to know if the animal was {guessed_animal_name}.")

        if guessed_animal_name == animal_name:
            dispatcher.utter_message(
                text=f"Hurray, you guessed it correctly, it is a {guessed_animal_name} indeed.")
            dispatcher.utter_message(text=f"Say 'Hey' to play again.")
            return [SlotSet(key="animal", value=" ")]
        else:
            dispatcher.utter_message(
                text=f"Unfortunately, the animal is not a {guessed_animal_name}. Try again.")