from unittest import TestCase, main

from project.team import Team


class TeamTests(TestCase):
    def setUp(self) -> None:
        self.team = Team("CSKA")

    def test_correct_init(self):
        team = Team("CSKA")

        self.assertEqual("CSKA",  team.name)
        self.assertEqual({}, team.members)

    def test_name_setter_rises_when_name_is_contains_non_alpha_letters(self):
        with self.assertRaises(ValueError) as ve:
            team = Team("123CSKA7898")
        self.assertEqual("Team Name can contain only letters!", str(ve.exception))

    def test_ad_member_adds_only_new_players_to_the_team(self):
        self.team.members["ivan"] = 18

        result = self.team.add_member(ivan=18, pesho=21, gosho=19, josh=16)

        self.assertEqual("Successfully added: pesho, gosho, josh", result)
        self.assertEqual(21, self.team.members["pesho"])
        self.assertEqual(19, self.team.members["gosho"])
        self.assertEqual(16, self.team.members["josh"])

    def test_remove_member_return_error_when_player_not_exist(self):
        member_name = "Vladi"
        result = self.team.remove_member(member_name)

        self.assertEqual(f"Member with name {member_name} does not exist", result)

    def test_remove_member_removes_member_fro_team(self):
        member_to_remove = "gosho"
        self.team.members["pesho"] = 21
        self.team.members[member_to_remove] = 31

        result = self.team.remove_member(member_to_remove)

        self.assertEqual(f"Member {member_to_remove} removed", result)
        self.assertEqual(21, self.team.members["pesho"])
        self.assertTrue(member_to_remove not in self.team.members)


    def test_gt_compares_team_by_members_count(self):
        self.team.members["member1"] = 20
        self.team.members["member2"] = 30

        another_team = Team("Levski")
        another_team.members["member1"] = 10
        another_team.members["member2"] = 20
        another_team.members["member3"] = 30

        self.assertEqual(True, another_team > self.team)
        self.assertEqual(False, another_team < self.team)

    def test_len_returns_member_count(self):
        self.team.members["member1"] = 20
        self.team.members["member2"] = 30

        self.assertEqual(2, len(self.team))

    def test_add_returns_new_team_combined_members(self):
        self.team.members["member1"] = 20
        self.team.members["member2"] = 30

        another_team = Team("Levski")
        another_team.members["member3"] = 10
        another_team.members["member4"] = 20
        another_team.members["member5"] = 30

        result = self.team + another_team
        expected_result = {
            "member1": 20,
            "member2": 30,
            "member3": 10,
            "member4": 20,
            "member5": 30
        }
        self.assertEqual("CSKALevski", result.name)
        self.assertEqual(expected_result, result.members)

    def test_str_return_members_sorted_in_descending_order_by_age(self):
        self.team.members["member3"] = 40
        self.team.members["member1"] = 20
        self.team.members["member2"] = 30

        result = str(self.team)
        expected = f"Team name: CSKA\n" + \
            f"Member: member3 - 40-years old\n" + \
            f"Member: member2 - 30-years old\n" + \
            f"Member: member1 - 20-years old"
        self.assertEqual(expected, result)


if __name__ == "__main__":
    main()
