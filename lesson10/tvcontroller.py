CHANNELS = ["BBC", "Discovery", "TV1000"]


class TVController:

    def __init__(self, fool_list_of_channel=CHANNELS):
        self.fool_list_of_channel = fool_list_of_channel
        self.current_channel = fool_list_of_channel[0]

    def switch_to_first_channel(self):
        self.current_channel = self.fool_list_of_channel[0]
        return self.current_channel

    def switch_to_last_channel(self):
        self.current_channel = self.fool_list_of_channel[-1]
        return self.current_channel

    def switch_to_turn_channel(self):
        self.turn_channel = int(input('Enter channel number: '))
        if self.turn_channel == 0:
            self.turn_channel = 1
        try:
            self.current_channel = self.fool_list_of_channel[self.turn_channel - 1]
        except IndexError:
            return 'You Enter wrong number of channel'
        else:
            return self.current_channel

    def switch_to_next_channel(self):
        self.leng_of_channel = len(self.fool_list_of_channel)
        self.index_of_valide_channel = self.fool_list_of_channel.index(self.current_channel)
        self.index_of_valide_channel += 1
        if self.index_of_valide_channel == self.leng_of_channel:
            self.index_of_valide_channel = 0
        self.current_channel = self.fool_list_of_channel[self.index_of_valide_channel]
        return self.current_channel

    def switch_to_previous_channel(self):
        self.leng_of_channel = len(CHANNELS) - 1
        self.index_of_valide_channel = CHANNELS.index(self.current_channel)
        if self.index_of_valide_channel == -1:
            self.index_of_valide_channel = self.leng_of_channel - 1
        self.index_of_valide_channel -= 1
        self.current_channel = CHANNELS[self.index_of_valide_channel]
        return self.current_channel

    def current_channel_(self):
        return self.current_channel

    def is_exist(self):
        self.exist_channel = input('Ведите интересующий канал: ')
        self.leng_of_channel = len(self.fool_list_of_channel)
        self.s = []
        for i in range(1, self.leng_of_channel + 1):
            self.s.append(str(i))

        if self.exist_channel in self.s or self.exist_channel in CHANNELS:
            return 'Yes'
        else:
            return 'NO'


x = TVController()

print(x.switch_to_first_channel())
print(x.switch_to_last_channel())
print(x.switch_to_first_channel())
print(x.switch_to_turn_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_next_channel())
print(x.switch_to_previous_channel())
print(x.switch_to_previous_channel())
print(x.switch_to_previous_channel())
print(x.is_exist())
print(x.current_channel_())