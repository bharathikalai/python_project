class TreasureChest:
    def __init__(self):
        self._gold_coin = 100
        self._gems = 5

    #method to add gold coins
    def add_gold_coins(self,amount):
        self._gold_coin += amount
        return self._gold_coin

    #method to remove gold coins

    def remove_gold_coins(self,amount):
        if self._gold_coin >= amount:
            self._gold_coin -=amount
            return self._gold_coin

        else:
            print("not enough gold coins !")
    
    def add_gems(self,amount):
        self._gems += amount

    def remove_gems(self,amount):
        if self._gems >= amount:
            self._gems +=amount
        else:
            print("not enough gems")

    def display_treasure(self):
        print(f"Gold Coins: {self._gold_coin}")
        print(f"gems: {self._gems}")




my_treasure = TreasureChest()

a = my_treasure.add_gold_coins(50)
print(a)
 
b =  my_treasure.remove_gold_coins(30)
print(b)


my_treasure.display_treasure()