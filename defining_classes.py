class Spaceship:
    # Class attribute
    tractor_beam = 'off'

    # Instance attributes
    def __init__(self, name, kind):
        self.name = name
        self.kind = kind
        self.speed = None

    # Instance methods
    def warp(self, warp):
        self.speed = warp
        print(f'Warp {warp}, engage!')

    def tractor(self):
        if self.tractor_beam == 'off':
            self.tractor_beam = 'on'
            print('Tractor beam on.')
        else:
            self.tractor_beam = 'off'
            print('Tractor beam off')

            


# Create an instance of the Spaceship class (i.e. "instantiate")
ship = Spaceship('Mockingbird', 'rescue frigate')

# Check ship's name
print(ship.name)

# Check what kind of ship it is
print(ship.kind)

# Check tractor beam status
print(ship.tractor_beam)


# Set warp speed
ship.warp(7)

# Check speed
ship.speed

# Toggle tractor beam
ship.tractor()

# Check tractor beam status
print(ship.tractor_beam)


