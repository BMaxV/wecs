from panda3d.core import Point3
from panda3d.core import Vec2, Vec3
from panda3d.core import CollisionCapsule

from wecs.core import Component
from wecs.aspects import Aspect
from wecs.aspects import factory
from wecs import panda3d
from wecs import mechanics
from wecs.panda3d import aspects



# Each frame, run these systems. This defines the game itself.
system_types = [
    panda3d.DetermineTimestep,  # How long is this frame? Update all clocks.
    # What movement do the characters intend to do?
    panda3d.AcceptFlipperInput,
    panda3d.AcceptInput,  # Input from player, ranges ([-1; 1]), not scaled for time.
    panda3d.Bumping,  # Bump into things (and out again).
    panda3d.ExecuteMovement,  # Turn intention into actual movement
    # We're done with character movement, now adjust the cameras.
    panda3d.UpdateCameras,
]

# Ignore this for the moment please; It means "This entity's model can be collided into".
@Component()
class Map:
    pass

game_map = Aspect([panda3d.Position, panda3d.Model, panda3d.Scene, Map,ThirdPersonCamera],
                  overrides={
                      panda3d.Position: dict(value=factory(lambda:Point3(0, 0, 0))),
                      panda3d.Model: dict(model_name='Board.bam'),
                      panda3d.Scene: dict(node=base.render),
                  },)

game_map.add(base.ecs_world.create_entity())

ball = Aspect([panda3d.Position, panda3d.Model, panda3d.Scene, ],
                  overrides={
                      panda3d.Position: dict(value=factory(lambda:Point3(0, 0, 0))),
                      panda3d.Model: dict(model_name='Board.bam'),
                      panda3d.Scene: dict(node=base.render),
                  },)

ball.add(base.ecs_world.create_entity())

right_flipper = Aspect([panda3d.Position, panda3d.Model, panda3d.Scene, panda3d.Flipper],
                  overrides={
                      panda3d.Position: dict(value=factory(lambda:Point3(0, 0, 0))),
                      panda3d.Model: dict(model_name='RightFlipper.bam'),
                      panda3d.Scene: dict(node=base.render),
                  },)
                  

right_flipper.right=True
right_flipper.add(base.ecs_world.create_entity())

left_flipper = Aspect([panda3d.Position, panda3d.Model, panda3d.Scene, panda3d.Flipper],
                  overrides={
                      panda3d.Position: dict(value=factory(lambda:Point3(0, 0, 0))),
                      panda3d.Model: dict(model_name='LeftFlipper.bam'),
                      panda3d.Scene: dict(node=base.render),
                  },)

left_flipper.left=True
left_flipper.add(base.ecs_world.create_entity())

