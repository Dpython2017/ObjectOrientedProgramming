#!/usr/bin/env python
class Oven:
    def __init__(self, timer):
        self.timer = timer
    @staticmethod
    def pre_heat():
        print("Pre-Heating the oven")
    @staticmethod
    def bake():
        print("Baking the cake")

    def set_time(self):
        return self.timer


class Mixer:
    def __init__(self, rounds):
        self.rounds = rounds

    def mix(self):
        print("Mixing content")

    def rounds_mix(self):
        return self.rounds

class Pan:
    def add(self):
        print(" Content added to pan")


class BakeCake(Oven, Mixer, Pan):


    def __init__(self):
        timer=200
        rounds = 50
        Oven.__init__(self,timer)
        Mixer.__init__(self,rounds)

    def cake_bake(self):
        set_timer = self.set_time()
        print("Timer set to: {} C".format(set_timer))
        self.pre_heat()
        rounds = self.rounds_mix()
        print("Rounds for mixing :{}".format(rounds))
        self.mix()
        self.bake()

vanilla_cake = BakeCake()
vanilla_cake.cake_bake()




