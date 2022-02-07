import numpy as np

ANSWER_TEMPLATES = {
    "question_mark": ["Good question, but I am not compitent enough to answer."],
    "dialog_end": ["Bye!", "Goodbye!", "See you later!"],
    "short": ["Don't be so short, tell me more about you."],
    "long": ["Wow, so much intresting things."],
    "empty_message": ["Don't be silent...", "Do you want to talk?"],
    "default_endings": ["What else?", "Tell me something.", "Nice weather, innit?"]
}


class MessageProcessor():
    memory = {
        "relation": [],
        "family_members": []
    }

    def __init__(self):
        self.continue_dialog = True

    def generate_answer(self, message):
        # add onfo to memory
        for key, value in message.to_remember.items():
            MessageProcessor.memory[key] += value

        # generate answer
        answer = ""
        if message.empty:
            return np.random.choice(
                ANSWER_TEMPLATES["empty_message"], 1)[0]

        if message.dialog_end:
            self.continue_dialog = False
            return np.random.choice(
                ANSWER_TEMPLATES["dialog_end"], 1)[0]

        elif message.question_mark:
            answer += np.random.choice(
                ANSWER_TEMPLATES["question_mark"], 1)[0]
            return answer + self.randomize_answer

        elif message.is_short:
            return np.random.choice(ANSWER_TEMPLATES["short"], 1)[0]

        elif message.is_long:
            answer += np.random.choice(ANSWER_TEMPLATES["long"], 1)[0]
            return answer + self.randomize_answer

        else:
            return self.randomize_answer()

    def randomize_answer(self):
        res = ""
        if len(MessageProcessor.memory["relation"]) > 0:
            relation = MessageProcessor.memory["relation"].pop(0)
            type_ = relation["main_token"]
            ending = relation["ending"]
            res += f"Previously you mentioned that you {type_}{ending}, what else do you {type_}?"
        elif len(MessageProcessor.memory["family_members"]) > 0:
            relation = MessageProcessor.memory["family_members"].pop(0)
            person = relation["main_token"]
            res += f"Previously you mentioned your {person}, please tell me more about your {person}."
        else:
            res += np.random.choice(
                ANSWER_TEMPLATES["default_endings"], 1)[0]

        return res
