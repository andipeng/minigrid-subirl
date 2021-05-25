#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register


class ThreeRoomsEnvFixed_Vert(MiniGridEnv):
    """
    Classic 2 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, agent_pos=(1,1), goal_pos=(17,17)):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        super().__init__(grid_size=19, max_steps=100)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        self.grid.vert_wall(5, 0)
        self.grid.vert_wall(10, 0)

        self.grid.set(*(5, 12), None)
        self.grid.set(*(5, 5), None)
        self.grid.set(*(10, 5), None)
        self.grid.set(*(10, 12), None)

        self.agent_pos = self._agent_default_pos
        self.grid.set(*self._agent_default_pos, None)
        self.agent_dir = 0

        goal = Goal()
        self.put_obj(goal, *self._goal_default_pos)
        goal.init_pos, goal.cur_pos = self._goal_default_pos

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info

class ThreeRoomsEnvFixed_Horz(MiniGridEnv):
    """
    Classic 2 rooms gridworld environment.
    Can specify agent and goal position, if not it set at random.
    """

    def __init__(self, agent_pos=(1,1), goal_pos=(17,17)):
        self._agent_default_pos = agent_pos
        self._goal_default_pos = goal_pos
        super().__init__(grid_size=19, max_steps=100)

    def _gen_grid(self, width, height):
        # Create the grid
        self.grid = Grid(width, height)

        # Generate the surrounding walls
        self.grid.horz_wall(0, 0)
        self.grid.horz_wall(0, height - 1)
        self.grid.vert_wall(0, 0)
        self.grid.vert_wall(width - 1, 0)

        self.grid.horz_wall(0, 5)
        self.grid.horz_wall(0, 10)

        self.grid.set(*(5, 5), None)
        self.grid.set(*(12, 5), None)
        self.grid.set(*(5, 10), None)
        self.grid.set(*(12, 10), None)

        self.agent_pos = self._agent_default_pos
        self.grid.set(*self._agent_default_pos, None)
        self.agent_dir = 0

        goal = Goal()
        self.put_obj(goal, *self._goal_default_pos)
        goal.init_pos, goal.cur_pos = self._goal_default_pos

        self.mission = 'Reach the goal'

    def step(self, action):
        obs, reward, done, info = MiniGridEnv.step(self, action)
        return obs, reward, done, info
   
register(
    id='MiniGrid-ThreeRoomsFixed_Vert-v0',
    entry_point='gym_minigrid.envs:ThreeRoomsEnvFixed_Vert'
)

register(
    id='MiniGrid-ThreeRoomsFixed_Horz-v0',
    entry_point='gym_minigrid.envs:ThreeRoomsEnvFixed_Horz'
)