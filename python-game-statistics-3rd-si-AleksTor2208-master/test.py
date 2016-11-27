import reports
import unittest


def get_sorted():
    return ['Age of Empires',
            'Command & Conquer',
            'Counter-Strike',
            'Counter-Strike: Condition Zero',
            'Crysis',
            'Diablo II',
            'Diablo III',
            'Doom 3',
            'EverQuest',
            "Garry's Mod",
            'Guild Wars',
            'Half-Life',
            'Half-Life 2',
            'Minecraft',
            'Populous',
            'StarCraft',
            'StarCraft II: Wings of Liberty',
            'Terraria',
            'The Sims',
            'The Sims 2',
            'The Sims 3',
            'Warcraft III: Reign of Chaos',
            'Warhammer 40,000: Dawn of War (including expansions)',
            'World of Warcraft']


class Tester(unittest.TestCase):
    points = 0
    input_file = "game_stat.txt"

    def test_1_count_games(self):
        result = reports.count_games(self.input_file)
        self.assertEqual(result, 24)
        if result == 24:
            self.points += 2
            print("Function 'count_games' is passed. 2 points.")

    def test_2_decide(self):
        correct = True

        game_found = reports.decide(self.input_file, 2000)
        self.assertTrue(game_found)
        if not game_found:
            correct = False

        game_not_found = reports.decide(self.input_file, 2016)
        self.assertFalse(game_not_found)
        if game_not_found:
            correct = False

        if correct:
            self.points += 2
            print("Function 'decide' is passed. 2 points.")

    def test_3_get_latest(self):
        result = reports.get_latest(self.input_file)
        expected = "Diablo III"
        self.assertEqual(result, expected)
        if result == expected:
            self.points += 2
            print("Function 'get_latest' is passed. 2 points.")

    def test_4_count_by_genre(self):
        result = reports.count_by_genre(self.input_file, "First-person shooter")
        self.assertEqual(result, 6)
        if result == 6:
            self.points += 2
            print("Function 'count_by_genre' is passed. 2 points.")

    def test_5_get_line_number_by_title(self):
        result = reports.get_line_number_by_title(self.input_file, "Counter-Strike")
        self.assertEqual(result, 6)
        if result == 6:
            self.points += 2
            print("Function 'get_line_number_by_title' is passed. 2 points.")

    def test_bonus_1_sort_abc(self):
        result = reports.sort_abc(self.input_file)
        expected_result = get_sorted()

        correct = True
        self.assertEqual(len(result), len(expected_result))
        if len(result) != len(expected_result):
            correct = False

        for i in range(0, min(len(result), len(expected_result))):
            self.assertEqual(result[i], expected_result[i])
            if result[i] != expected_result[i]:
                correct = False

        if correct:
            self.points += 1
            print("Bonus function 'sort_abc' is passed. 1 points.")

    def test_bonus_2_get_genres(self):
        result = reports.get_genres(self.input_file)
        expected_result = ["Action-adventure", "First-person shooter", "Real-time strategy", "RPG", "Sandbox",
                           "Simulation", "Survival game"]

        correct = True
        self.assertEqual(len(result), len(expected_result))
        if len(result) != len(expected_result):
            correct = False

        for i in range(0, min(len(result), len(expected_result))):
            self.assertEqual(result[i], expected_result[i])
            if result[i] != expected_result[i]:
                correct = False

        if correct:
            self.points += 1
            print("Bonus function 'get_genres' is passed. 1 points.")

    def test_bonus_3_when_was_top_sold_fps(self):
        result = reports.when_was_top_sold_fps(self.input_file)
        self.assertEqual(result, 1999)
        if result == 1999:
            self.points += 1
            print("Bonus function 'when_was_top_sold_fps' is passed. 1 points.")


def main():
    unittest.main()

if __name__ == '__main__':
    main()
