#!/usr/bin/env python
# -*- coding: utf-8 -*-

from gym_minigrid.minigrid import *
from gym_minigrid.register import register


class TwoRoomsEnvFixed_Vert(MiniGridEnv):
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

        self.grid.vert_wall(8, 0)

        self.grid.set(*(8, 4), None)
        self.grid.set(*(8, 12), None)

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

class TwoRoomsEnvFixed_Horz(MiniGridEnv):
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

        self.grid.horz_wall(0, 8)

        self.grid.set(*(4, 8), None)
        self.grid.set(*(12, 8), None)

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
    id='MiniGrid-TwoRoomsFixed_Vert-v0',
    entry_point='gym_minigrid.envs:TwoRoomsEnvFixed_Vert'
)

register(
    id='MiniGrid-TwoRoomsFixed_Horz-v0',
    entry_point='gym_minigrid.envs:TwoRoomsEnvFixed_Horz'
)