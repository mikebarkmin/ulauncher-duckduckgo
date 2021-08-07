from ulauncher.api.shared.item.ExtensionResultItem import ExtensionResultItem
from ulauncher.api.shared.action.CopyToClipboardAction import CopyToClipboardAction
from ulauncher.api.shared.action.HideWindowAction import HideWindowAction
from ulauncher.api.shared.action.DoNothingAction import DoNothingAction
from ulauncher.api.shared.action.OpenUrlAction import OpenUrlAction

from src.functions import generate_url


ICON_FILE = "images/icon.png"


def no_input_item():
    return [
        ExtensionResultItem(icon=ICON_FILE, name="No input", on_enter=DoNothingAction())
    ]


def show_suggestion_items(suggestions):
    return [
        ExtensionResultItem(
            icon=ICON_FILE,
            name=suggestion,
            on_enter=OpenUrlAction(generate_url(suggestion)),
        )
        for suggestion in suggestions
    ]


def show_instant_answer(instant_item, instant_answer, instant_url):
    if instant_item == "" or instant_answer == "" or instant_url == "":
        return None

    # add line breaks to answer
    max_chars = 75
    answer_chunk = []
    words = instant_answer.split(" ")
    index, anchor = 1, 0
    while anchor <= len(words):
        partial = " ".join(words[anchor : anchor + index])
        if len(partial) > max_chars:
            answer_chunk.append(" ".join(words[anchor : anchor + index - 1]))
            anchor += index - 1
            index = 1
            continue
        if anchor + index == len(words):
            answer_chunk.append(partial)
            break
        index += 1

    return ExtensionResultItem(
        icon=ICON_FILE,
        name=instant_item,
        description="\n".join(answer_chunk),
        on_enter=OpenUrlAction(instant_url),
    )
