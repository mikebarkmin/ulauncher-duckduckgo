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
