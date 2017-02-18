"""
Assignment 3: Classes and objects

You will implement a set of classes that model a restaurant menu.
"""
class Menu(object):
    """A menu of available items and some associated information.

    This class must have 2 class attributes drink_tax and food_tax
    that are used for the tax amount on drink and food. The value
    should be 0.18 (18%) for drink, and 0.10 (10%) for food.

    """
    drink_tax = 0.18
    food_tax = 0.10

    def __init__(self):
        # TODO: Implement
        self.item_list = []

    def add_item(self, item):
        """Add an item to this menu and set it's menu attribute to this menu.

        Items should not be allowed to be added to more than one menu
        so check if the item is already in another menu.

        Return: True if the item was added, and False it was not (because it had already been assigned a menu).
        """
        # TODO: Implement
        if item.menu is None:
            self.item_list.append(item)
            item.menu = self
            return True
        return False

    # TODO: Add a read-only property named items that returns a COPY
    # of the set of items in this menu
    @property
    def items(self):
        return_list = tuple(self.item_list)
        return return_list


class Order(object):
    """A list of items that will be purchased together.

    This provides properties that compute prices with tax and tip for
    the whole order.

    """
    def __init__(self):
        self.item_list = []

    def add_item(self, item):
        """Add an item to this order.

        Items are required to all be part of one menu. You will need
        to check for this.

        Return True if the item was added, False otherwise (mainly if
        it was not part of the same menu as previous items).

        """
        # TODO: Implement
        if hasattr(item, "menu") and (not self.item_list or item.menu is self.item_list[0].menu):
            self.item_list.append(item)
            return True
        return False

    def price_plus_tax(self):
        """A function that returns the sum of all the item prices
        including their tax.

        """
        # TODO: Implement
        sum_price = 0
        for index in self.item_list:
            sum_price += index.price * (1 + index._applicable_tax())
        return sum_price

    def price_plus_tax_and_tip(self, amount):
        """A method returns the sum of all the item prices with
        tax and a specified tip.

        amount is given as a proportion of the cost including tax.

        """
        # TODO: Implement (Make sure not to duplicate any code in
        # price_plus_tax).
        return self.price_plus_tax() * (1 + amount)

class GroupOrder(Order):
    """An order than is made by a large ground and forces the tip to be at least
    20% (0.20).

    If a price with a tip less than 20% is requested return a price with a 20%
    tip instead.
    """

    # TODO: Override price_plus_tax_and_tip to force a tip of at least
    # 20% (0.20). Do not duplicate any code (incl. the implementation of
    # price_plus_tax_and_tip from Order)

    def price_plus_tax_and_tip(self, amount):
        if amount < 0.2:
            return self.price_plus_tax() * 1.2
        else:
            return self.price_plus_tax() * (amount + 1)

class Item(object):
    """An item that can be bought.

    It has a name and a price attribute, and can compute its price with
    tax. This also has a menu property that stores the menu this has
    been added to.

    """
    def __init__(self, name, price):
        # TODO: Implement
        self.name = name
        self.price = price
        self.real_menu = None

    # TODO: Add a property (not just an attribute) called "menu" that
    # returns the menu this item is part of. It should only be
    # possible to set it once.

    @property
    def menu(self):
        return self.real_menu

    @menu.setter
    def menu(self, value):
        if self.real_menu is None:
            self.real_menu = value

    def price_plus_tax(self):
        """Return the price of this item with tax added.

        Make sure you could support additional Item types, other than
        what you have in this file (meaning isinstance checks will not
        work). Imagine that I might have a Dessert class that derives
        from Item in another file.

        """
        # TODO: Implement
        return self.price * (1 + self._applicable_tax())

    def _applicable_tax(self):
        """Return the amount of tax applicable to this item as a proportion
        (eg. 0.2 if the tax is 20%).
        """
        # This is an abstract method. It should not be implemented in
        # this class.
        pass

# DO NOT change the classes below. Your code in Item should work with
# these implementation as is.

class Food(Item):
    """An Item subclass which uses the food tax rate."""

    def _applicable_tax(self):
        return self.menu.food_tax

class Drink(Item):
    """An Item subclass which uses the drink tax rate."""

    def _applicable_tax(self):
        return self.menu.drink_tax
