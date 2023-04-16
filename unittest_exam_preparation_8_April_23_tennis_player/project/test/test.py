from project.tennis_player import TennisPlayer

from unittest import TestCase, main


class TennisPlayerTests(TestCase):

    def test_correct_init(self):
        tennis_player = TennisPlayer("Grisho", 30, 100)

        self.assertEqual("Grisho", tennis_player.name)
        self.assertEqual(30, tennis_player.age)
        self.assertEqual(100, tennis_player.points)
        self.assertEqual([], tennis_player.wins)

    def test_name_if_len_name_is_less_than_or_equal_to_2_rises(self):

        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Gr", 30, 100)
        self.assertEqual("Name should be more than 2 symbols!", str(ve.exception))

    def test_age_if_is_less_then_18_rises(self):

        with self.assertRaises(ValueError) as ve:
            TennisPlayer("Grisho", 17, 100)
        self.assertEqual("Players must be at least 18 years of age!", str(ve.exception))

    def test_add_new_win_if_already_added(self):
        tennis_player = TennisPlayer("Grisho", 30, 100)
        tennis_player.wins.append("wins1")
        tennis_player.wins.append("wins2")

        result = tennis_player.add_new_win("wins2")

        self.assertEqual(f"wins2 has been already added to the list of wins!", result)

    def test_add_new_win(self):
        tennis_player = TennisPlayer("Grisho", 30, 100)
        tennis_player.wins = ['wins1', "wins2"]
        result = tennis_player.add_new_win("wins3")
        expected = ["wins1", "wins2", "wins3"]

        self.assertEqual(expected, str(result))


    def test_lt_points(self):
        tennis_player = TennisPlayer("Grisho", 30, 100)
        tennis_player1 = TennisPlayer("Nole", 20, 110)

        self.assertTrue('Nole is a top seeded player and he/she is better than Grisho', tennis_player.points < tennis_player1.points)
        self.assertTrue('Grisho is a better player than Nole', tennis_player.points > tennis_player1.points)

    def test_str(self):
        tennis_player = TennisPlayer("Grisho", 30, 100)
        tennis_player.wins.append("win1")
        tennis_player.wins.append("win2")
        tennis_player.wins.append("win3")

        result= str(tennis_player)
        expected = f"Tennis Player: {tennis_player.name}\n" + \
                   f"Age: {tennis_player.age}\n" + \
                   f"Points: {tennis_player.points:.1f}\n" + \
                   f"Tournaments won: {', '.join(tennis_player.wins)}"
        self.assertEqual(expected, result)

        # def test_str_return_members_sorted_in_descending_order_by_age(self):
        # self.team.members["member3"] = 40
        # self.team.members["member1"] = 20
        # self.team.members["member2"] = 30
        #
        # result = str(self.team)
        # expected = f"Team name: CSKA\n" + \
        #            f"Member: member3 - 40-years old\n" + \
        #            f"Member: member2 - 30-years old\n" + \
        #            f"Member: member1 - 20-years old"
        # self.assertEqual(expected, result)




if __name__ == "__main__":
    main()