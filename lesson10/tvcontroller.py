class TVController:
    CHANNELS = ["BBC", "Discovery", "TV1000"]

    def __init__(self, valid_channel=CHANNELS[0]):
        self.valid_channel = valid_channel

    def switch_to_first_channel(self):
        self.valid_channel = TVController.CHANNELS[0]
        return self.valid_channel

    def switch_to_last_channel(self):
        self.valid_channel = TVController.CHANNELS[-1]
        return self.valid_channel

    def switch_to_turn_channel(self):
        self.turn_channel = int(input('Enter channel number: '))
        if self.turn_channel == 0:
            self.turn_channel = 1
        try:
            self.valid_channel = TVController.CHANNELS[self.turn_channel - 1]
        except IndexError:
            return 'You Enter wrong number of channel'
        else:
            return self.valid_channel

    def switch_to_next_channel(self):
        self.leng_of_channel = len(TVController.CHANNELS)
        self.index_of_valide_channel = TVController.CHANNELS.index(self.valid_channel)
        self.index_of_valide_channel += 1
        if self.index_of_valide_channel == self.leng_of_channel:
            self.index_of_valide_channel = 0
        self.valid_channel = TVController.CHANNELS[self.index_of_valide_channel]
        return self.valid_channel

    def switch_to_previous_channel(self):
        self.leng_of_channel = len(TVController.CHANNELS) - 1
        self.index_of_valide_channel = TVController.CHANNELS.index(self.valid_channel)
        if self.index_of_valide_channel == -1:
            self.index_of_valide_channel = self.leng_of_channel - 1
        self.index_of_valide_channel -= 1
        self.valid_channel = TVController.CHANNELS[self.index_of_valide_channel]
        return self.valid_channel

    def current_channel(self):
        return self.valid_channel

    def is_exist(self):
        self.exist_channel = input('Ведите интересующий канал: ')
        self.list_of_channel = len(TVController.CHANNELS)
        self.s = []
        for i in range(1, self.list_of_channel + 1):
            self.s.append(str(i))

        if self.exist_channel in self.s or self.exist_channel in TVController.CHANNELS:
            return 'Yes'
        else:
            return 'NO'


x = TVController()

# print(x.switch_to_first_channel())
# print(x.switch_to_last_channel())
# print(x.switch_to_turn_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_next_channel())
# print(x.switch_to_previous_channel())
# print(x.switch_to_previous_channel())
# print(x.switch_to_previous_channel())
# print(x.current_channel())
# print(x.is_exist())
