import class_TV


class TestProgram:
    def test_check_the_TV_is_off(self):
        My_TV = class_TV.TV()
        assert My_TV.find_state_TV() is False

    def test_check_the_status_TV(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        assert My_TV.find_state_TV()


    def test_check_the_channel_on_TV(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        assert My_TV.find_channel() == 1

    def test_check_the_channel_on_TV_when_TV_on_and_off(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.turn_off()
        assert My_TV.find_channel() == 0

    def test_check_the_select_channel_operation(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(10)
        assert My_TV.find_channel() == 10

    def test_check_the_select_previous_channel_operation(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(5)
        My_TV.select_channel(90)
        assert My_TV.find_channel() == 90
        My_TV.select_previous_channel()
        assert My_TV.find_channel() == 5

    def test_check_the_select_channel_operation_then_TV_is_off(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(99)
        My_TV.turn_off()
        assert My_TV.find_channel() == 0


    def test_check_the_select_channel_then_no_channel_in_this_number(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(0)
        assert My_TV.find_channel() == 1

        My_TV.select_channel(100)
        assert My_TV.find_channel() == 1


    def test_check_the_select_previous_channel_operation_then_TV_is_off(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(99)
        My_TV.select_channel(56)
        My_TV.select_previous_channel()
        My_TV.turn_off()
        assert My_TV.find_channel() == 0


    def test_check_the_select_previous_channel_operation_then_select_channel_only_1(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(1)
        My_TV.select_previous_channel()
        assert My_TV.find_channel() == 1

    def test_check_the_select_channel_operation_then_TV_is_on_off_and_on(self):
        My_TV = class_TV.TV()
        My_TV.turn_on()
        My_TV.select_channel(33)
        My_TV.select_channel(38)
        My_TV.turn_off()
        My_TV.turn_on()
        assert My_TV.find_channel() == 38
        My_TV.select_previous_channel()
        assert My_TV.find_channel() == 38

    def test_check_the_select_channel_operation_then_TV_is_off_2(self):
        My_TV = class_TV.TV()
        My_TV.select_channel(50)
        assert My_TV.find_state_TV() is False
        assert My_TV.find_channel() == 0

        My_TV.turn_on()
        My_TV.select_channel(2)
        My_TV.turn_off()
        My_TV.select_channel(88)
        assert My_TV.find_channel() == 0

        My_TV.turn_on()
        assert My_TV.find_channel() == 2

        My_TV.select_channel(97)
        My_TV.turn_off()
        My_TV.select_previous_channel()
        assert My_TV.find_channel() == 0
        My_TV.turn_on()
        assert My_TV.find_channel() == 97
