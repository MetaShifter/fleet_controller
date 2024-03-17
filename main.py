import random

import matplotlib.pyplot as plt
import matplotlib.animation as animation

robots = {}

class Robot:
    def __init__(self, serial_number, activation_round, deactivation_round) -> None:
        self.serial_number = serial_number
        self.activation_round = activation_round
        self.deactivation_round = deactivation_round
        self.is_active = False
        self.is_healthy = True
        self.points_generated = 0

    def work(self, current_round):
        if  self.activation_round <= current_round and current_round <= self.deactivation_round: # if the current round is between the activation and deactivation rounds, the robot will be active
            self.is_active = True
        else:
            self.is_active = False 
            return

        if self.is_healthy: # if the robot is healthy, it will generate 1 point
            self.points_generated += 1
        elif not self.is_healthy: # if the robot is not healthy, it will consume 10 points
            self.points_generated = self.points_generated -10

        workload = random.randint(1, 100)
        if workload >= 90 and self.is_healthy: # if the workload is greater than 90, the robot will get damaged and will not be healthy anymore
            self.is_healthy = False

    def __repr__(self) -> str:
        return f'{self.serial_number = } - {self.activation_round = } - {self.deactivation_round = } - {self.points_generated = } - {self.is_active = } - {self.is_healthy = }' # useful representation of the robot object

class Controller:
    def __init__(self, robots_serial_numbers) -> None:
        self.robots_serial_numbers = robots_serial_numbers
        self.robots_managed = []
        self.active_robots = []

        self.points = 0
        self.moves_left = 100

    def get_robot(self, serial_number):
        return robots.get(serial_number)
    
    def add_robots(self): # function to add the robots to the robots_managed list, based on the serial numbers given to the controller by the CommandCenter
        for serial_number in self.robots_serial_numbers:
            robot = self.get_robot(serial_number)
            self.robots_managed.append(robot)

    def read_active_status(self, robot):
        if self.moves_left == 0:
            return
        self.moves_left -= 1
        return robot.is_active
    
    def read_healthy_status(self, robot):
        if self.moves_left == 0:
            return
        self.moves_left -= 1
        return robot.is_healthy
    
    def repair_robot(self, robot):
        if self.moves_left == 0:
            return
        self.moves_left -= 1
        robot.is_healthy = True

    def work(self, current_round): # function to work for each round.   if moves are used during the round, the points will be decreased by 20

        if current_round <= 2:
            return
     
        for robot in self.robots_managed:
            if robot not in self.active_robots:
                if self.read_active_status(robot): # if the robot is active during this current round, it will be added to the active_robots list and removed from the robots_managed list to keep track of which robot is active and which isn't.
                    self.active_robots.append(robot)
                    self.robots_managed.remove(robot)

        for active_robot in self.active_robots:
            if current_round >30:
                if not self.read_active_status(active_robot): # after we reach the "deactivation zone" of >30, we check if the robot has been deactivated and if so, it will be removed from the active_robots list
                    self.active_robots.remove(active_robot)
                    continue
            if not self.read_healthy_status(active_robot): # if the robot is not healthy, it will be repaired 
                self.repair_robot(active_robot)
        

        if self.moves_left != 100: # consume 20 points if the controller did any moves
            self.points-=20        

        self.moves_left = 100 # reset the moves_left for the next round


class CommandCenter:
    def __init__(self, no_of_rounds, no_of_controllers, no_of_robots ) -> None:
        self.no_of_rounds = no_of_rounds
        self.no_of_controllers = no_of_controllers
        self.no_of_robots = no_of_robots

        self.total_points = 0
        self.points_per_round = []
        self.robots_serial_numbers = []
        self.controller_list = []
        
    def create_robots(self): # function to create the robots based on the number of robots given
        for i in range(self.no_of_robots):
            serial_number = f'robot_{i}'
            activation_round = random.randint(0, self.no_of_rounds//2-1) # activation round is a random number between 0 and half of the number of rounds ( in our case, [0-29])
            deactivation_round = random.randint(self.no_of_rounds//2-1, self.no_of_rounds-1) # deactivation round is a random number between half of the number of rounds and the number of rounds ( in our case, [29-59])
            robot = Robot(serial_number, activation_round, deactivation_round)
            robots[serial_number] = robot
            self.robots_serial_numbers.append(serial_number)

    def create_controllers(self): # function to create the controllers and attribute the robots to them
        robots_per_controller = len(self.robots_serial_numbers) // self.no_of_controllers
        for i in range(self.no_of_controllers):
            attributed_robots = self.robots_serial_numbers[i*robots_per_controller:(i+1)*robots_per_controller]
            controller = Controller(attributed_robots)
            controller.add_robots()
            self.controller_list.append(controller)

    def run_simulation(self): # function to run the simulation. for each round, each robot and controller will work - and the points will be summed up
        self.create_robots()
        self.create_controllers()
        for i in range(self.no_of_rounds):
            for robot in robots.values():
                robot.work(i)
            for controller in self.controller_list:
                controller.work(i)
            self.total_points = sum(robot.points_generated for robot in robots.values()) + sum(controller.points for controller in self.controller_list)
            self.points_per_round.append(self.total_points)
            
    def display_plot(self): # function to display a plot of the points evolution
        fig, ax = plt.subplots()
        fig.canvas.manager.set_window_title('Points Evolution')

        def animate(round_num):
            data = self.points_per_round[:round_num + 1]
            ax.clear()
            ax.plot(data)
            ax.set_xlabel('Round')
            ax.set_ylabel('Points')
            ax.set_title(f'Points Evolution (Round {round_num + 1})')

        ani = animation.FuncAnimation(fig, animate, frames=self.no_of_rounds, interval=50, repeat=False) # animation of the points evolution
        
        plt.show()
        plt.close()
        


def main():
    no_of_rounds = 60
    no_of_robots = 10000
    no_of_controllers = 200
    
    command_center = CommandCenter(no_of_rounds, no_of_controllers, no_of_robots)
    command_center.run_simulation()
    command_center.display_plot()

    print(f'{command_center.total_points = }')


if __name__ == "__main__":
    main()