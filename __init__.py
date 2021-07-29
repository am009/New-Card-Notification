from anki.cards import Card
from aqt import gui_hooks
from anki.consts import *
import aqt.utils

def notifier(card: Card) -> None:
    if card.queue == QUEUE_TYPE_NEW:
        aqt.utils.tooltip("New Card")
    return

gui_hooks.reviewer_did_show_question.append(notifier)