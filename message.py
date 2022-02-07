SHORT_LIMIT = 10
LONG_LIMIT = 25

TOKENS_BY_TYPE = {
    "question_mark": ["?"],
    "dialog_end": ["goodbye", "see you later"],
    "relation": ["like", "hate", "love"],
    "family_members": ["mother", "father", "brother", "sister"]
}


class Message():

    def __init__(self, line) -> None:
        self.text = line.lower()
        self.empty = False
        self.is_short = False
        self.is_long = False
        self.dialog_end = False
        self.question_mark = False
        self.to_remember = {
            "relation": [],
            "family_members": []
        }

    def analyze(self):
        if not self.text.split():
            self.empty = True
            return
        for token in TOKENS_BY_TYPE["dialog_end"]:
            if token in self.text:
                self.dialog_end = True
        if "?" in self.text:
            self.question_mark = True
        if len(self.text) <= SHORT_LIMIT:
            self.is_short = True
        elif len(self.text) >= LONG_LIMIT:
            self.is_long = True

        for type in ["relation", "family_members"]:
            for token in TOKENS_BY_TYPE[type]:
                if token in self.text:
                    self.to_remember[type].append({
                        "main_token": token,
                        "ending": Message.get_ending(self.text, token)
                    })

    @staticmethod
    def get_ending(text, token):
        return text.split(token)[1]
