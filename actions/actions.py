# This files contains your custom actions which can be used to run
# custom Python code.
#
# See this guide on how to implement these action:
# https://rasa.com/docs/rasa/custom-actions


# This is a simple example for a custom action which utters "Hello World!"

from typing import Any, Text, Dict, List

from rasa_sdk import Action, Tracker
from rasa_sdk.executor import CollectingDispatcher
import csv

class ActionHelloWorld(Action):

     def name(self) -> Text:
         return "action_do_sth"

     def run(self, dispatcher: CollectingDispatcher,
             tracker: Tracker,
             domain: Dict[Text, Any]) -> List[Dict[Text, Any]]:
         with open('addresses.csv', newline='', encoding="cp437") as csvfile:
             spamreader = csv.reader(csvfile, delimiter='.', quotechar='|')
             for row in spamreader:
                 print(row)
                 msg = ''.join(row)
                 dispatcher.utter_message(text=msg)


         return []
