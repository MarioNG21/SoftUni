from project.team import Team

from unittest import TestCase, main


class TeamTest(TestCase):
    def setUp(self):
        self.team = Team('Mario')

    def test_team_initialization(self):
        self.assertEqual("Mario", self.team.name)
        self.assertEqual({}, self.team.members)

    def test_team_name_property_value_with_nonalphach_should_raise_Exception(self):
        expected_error = "Team Name can contain only letters!"
        with self.assertRaises(ValueError) as ex:
            self.team.name = "Mario12"

        self.assertEqual(expected_error, str(ex.exception))

    def test_team_name_accurate_name_should_change_it(self):
        new_name = "Bees"
        self.team.name = new_name
        self.assertEqual(new_name, self.team.name)

    def test_add_member_should_return_message(self):
        member_name = "Mario"
        member_age = 12
        member_name2 = "Alex"
        member_age2 = 12

        expected_message = f"Successfully added: {', '.join([member_name, member_name2])}"
        expected_members = {member_name: member_age, member_name2: member_age2}
        result = self.team.add_member(Mario=member_age, Alex=member_age2)
        self.assertEqual(expected_message, result)
        self.assertEqual(expected_members, self.team.members)

    def test_remove_member_when_member_with_such_name_does_not_exist(self):
        member_name = "Mario"
        expected_message = f"Member with name {member_name} does not exist"
        result = self.team.remove_member(member_name)
        self.assertEqual(expected_message, result)

    def test_remove_member_with_existing_name(self):
        member_name = "Mario"
        member_age = 12
        expected_message = f"Member {member_name} removed"
        self.team.add_member(Mario=12)
        self.assertEqual({member_name: member_age}, self.team.members)
        result = self.team.remove_member(member_name)
        self.assertEqual({}, self.team.members)
        self.assertEqual(expected_message, result)

    def test_gt_method_should_return_true_when_self_is_bigger_than_other(self):
        member_name = "Mario"
        member_age = 12
        member_name2 = "Alex"
        member_age2 = 11
        self.team.add_member(Mario=12)
        self.team.add_member(Alex=11)
        our_members = {member_name: member_age, member_name2: member_age2}
        self.assertEqual({member_name: member_age, member_name2: member_age2}, self.team.members)
        self.assertEqual(2, len(self.team.members))

        opponent = Team('Gosho')
        opponent.add_member(Emo=11)
        len_of_other = 1
        opponent_members = {"Emo": 11}
        self.assertEqual("Gosho", opponent.name)
        self.assertEqual({"Emo": 11}, opponent.members)
        self.assertEqual(len_of_other, len(opponent.members))
        self.assertEqual(len(our_members) > len(opponent_members), self.team > opponent)

    def test_gt_method_should_return_false_when_self_is_less_than_other(self):
        member_name = "Mario"
        member_age = 12
        our_members = {member_name: member_age}
        self.team.add_member(Mario=12)
        self.assertEqual({member_name: member_age}, self.team.members)
        len_of_self = 1

        opponent = Team('Gosho')
        opponent_member_name1 = "Emo"
        opponent_member_age1 = 11
        opponent_member_name2 = "Alex"
        opponent_member_age2 = 11
        opponent_members = {opponent_member_name1: opponent_member_age1, opponent_member_name2: opponent_member_age2}
        opponent.add_member(Emo=11, Alex=11)
        self.assertEqual({opponent_member_name1: opponent_member_age1, opponent_member_name2: opponent_member_age2},
                         opponent.members)

        self.assertEqual(len(our_members) > len(opponent_members), self.team > opponent)

    def test_len_method_should_return_int(self):
        member_name = "Mario"
        member_age = 12
        our_members = {member_name: member_age}
        self.team.add_member(Mario=12)
        self.assertEqual(len(our_members), len(self.team))

    def test_add_method(self):
        member_name = "Mario"
        member_age = 12
        self.team.add_member(Mario=12)

        opponent_name = "Pesho"
        opponent_age = 12
        opponent = Team("Gosho")
        opponent.add_member(Pesho=12)

        new_name_expected = f"{'Mario'}{'Gosho'}"
        new_team = Team(new_name_expected)
        expected_new_members = {member_name: member_age, opponent_name: opponent_age}
        new_team.add_member(Mario=12, Pesho=12)
        self.assertEqual(new_name_expected, (self.team + opponent).name)
        self.assertEqual(expected_new_members, (self.team + opponent).members)

    def test_str_method(self):
        self.team.add_member(Mario=12, Alex=12, Emo=11)
        expected_result = f'''Team name: {self.team.name}
Member: {"Alex"} - {12}-years old
Member: {"Mario"} - {12}-years old
Member: {"Emo"} - {11}-years old
'''.strip()
        self.assertEqual(expected_result, str(self.team))


if __name__ == '__main__':
    main()
