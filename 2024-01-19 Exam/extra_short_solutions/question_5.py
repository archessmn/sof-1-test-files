import copy


class GameObject:
    _shape: str
    _colour: str

    @property
    def shape(self):
        return self._shape

    @property
    def colour(self):
        return self._colour

    def __init__(self, shape: str, colour: str) -> None:
        self._shape, self._colour = (shape, colour)

    def __eq__(self, value: object) -> bool:
        return False if not isinstance(value, GameObject) else self._shape == value.shape and self._colour == value.colour

    def __hash__(self) -> int:
        return hash((self._shape, self._colour))


class GameCard:
    _content: list[GameObject]

    @property
    def content(self):
        return copy.deepcopy(self._content)

    def __init__(self, game_object1: GameObject, game_object2: GameObject):
        self._content = [game_object1, game_object2]

    def __contains__(self, item) -> bool:
        return False if not isinstance(item, GameObject) else item in self._content

    def __eq__(self, value: object) -> bool:

        return False if not isinstance(value, GameCard) else all(game_object in value for game_object in self._content)

    def __hash__(self) -> int:
        return hash((list(game_object.colour for game_object in self. _content).sort(), list(game_object.shape for game_object in self._content).sort()))


class CardDeck:
    _objects: set[GameObject]
    _colours: set[str] = {}
    _shapes: set[str] = {}

    def __init__(self, objects: list[GameObject]) -> None:
        self._objects, self._colours, self._shapes = exec('raise ValueError("Must have 3, 4 or 5 objects")') if len(objects) not in {3, 4, 5} else (lambda colours, shapes: (set(objects), colours, shapes) if len(set(colours)) == len(colours) and len(set(shapes)) == len(shapes) else exec('raise ValueError("Duplicate colours or shapes found")'))(set(map(lambda g_o: g_o.colour, objects)), set(map(lambda g_o: g_o.shape, objects)))

    def generate_deck(self) -> list[GameCard]:
        return set().union(*map(lambda game_object: set().union(*map(lambda card_obj1: {GameCard(game_object, card_obj1)}.union(map(lambda card_obj2: GameCard(card_obj1, card_obj2), set().union(*(lambda shapes, colours: map((lambda shape: set(filter(lambda card_obj2: all(map(lambda check_obj: (False if check_obj.colour not in [card_obj1.colour, card_obj2.colour] and check_obj.shape not in [card_obj1.shape, card_obj2.shape] else True) if check_obj != game_object else True, self._objects)), map(lambda valid_colour: GameObject(shape, valid_colour), set(filter(lambda colour: True if GameObject(shape, colour) not in self._objects else False, colours)))))), shapes))(list(filter(lambda shape: shape not in [card_obj1.shape, game_object.shape], self._shapes)), list(filter(lambda colour: colour not in [card_obj1.colour, game_object.colour], self._colours)))))), set().union(*(lambda shapes, colours: map((lambda shape: set(map(lambda valid_colour: GameObject(shape, valid_colour), set(filter(lambda colour: True if GameObject(shape, colour) not in self._objects else False, colours))))), shapes))(list(filter(lambda shape: shape != game_object.shape, self._shapes)), list(filter(lambda colour: colour != game_object.colour, self._colours)))))), self._objects))


deck = CardDeck([GameObject("bottle", "green"), GameObject(
    "chair", "red"), GameObject("book", "blue")])

print(len(deck.generate_deck()))

deck = CardDeck([GameObject("bottle", "green"), GameObject(
    "chair", "red"), GameObject("book", "blue"), GameObject("ghost", "white")])

print(len(deck.generate_deck()))

deck = CardDeck([GameObject("bottle", "green"), GameObject(
    "chair", "red"), GameObject("book", "blue"), GameObject("ghost", "white"), GameObject("mouse", "grey")])

print(len(deck.generate_deck()))
