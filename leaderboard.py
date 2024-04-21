# leaderboard.py
import json

class Leaderboard:
    def __init__(self, filename='leaderboard.json'):
        self.filename = filename
        self.leaderboard = self.load_leaderboard()

    def load_leaderboard(self):
        try:
            with open(self.filename, 'r') as file:
                return json.load(file)
        except FileNotFoundError:
            return []

    def update_leaderboard(self, new_score):
        self.leaderboard.append(new_score)
        self.leaderboard.sort(key=lambda x: x['score'], reverse=True)
        self.leaderboard = self.leaderboard[:10]  # Keep top 10 scores only
        self.save_leaderboard()

    def save_leaderboard(self):
        with open(self.filename, 'w') as file:
            json.dump(self.leaderboard, file, indent=4)

    def get_leaderboard(self):
        return self.leaderboard
