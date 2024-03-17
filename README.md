<h1> Project Description

This project simulates a robot fleet management system. The goal is to accumulate points over a series of rounds. 
Key components include:

> Robots: Autonomous units that become active within a designated round window. They generate points while healthy but can cause penalties when unhealthy.
> Controllers: Manage a subset of robots. Controllers monitor robot status and can perform repairs but are limited in the number of actions per round.
> Command Center: Oversees the simulation, initializes robots and controllers, and tracks overall score.


<h1> Design & Algorithm choices </h1>
<section> 
The core of the design is built using OOP, around three central classes:
- Robot: Encapsulates all the properties of an individual robot, including the state transition logic ( work ).
- Controller: Manages a subset of robots, monitoring robot status and performing repairs.
- CommandCenter: Acts as the coordinator, setting up the environment and running the simulation loop.



During problem designing phase, I figured out that using a dictionary for robots provides central access to all Robot objects by their serial number, enabling efficient lookup by controllers in O(1) time complexity.
</section>



<h1> Model </h1>
<h2> Robots </h2>

Properties:
> serial_number (string): Unique identifier for each robot.
> activation_round (int): The round in which the robot becomes active.
> deactivation_round (int): The round in which the robot becomes inactive.
> is_active (bool): Indicates whether the robot is currently active.
> is_healthy (bool): Indicates whether the robot is in a healthy state.
> points_generated (int): Cumulative points generated or lost by the robot.

Behavior
> work(current_round): Simulates the robot's task for the round.
> Checks activation_round and deactivation_round to determine activity status.
> Generates 1 point if is healthy, active and workload <90; otherwise, loses 10 points if workload>=90.
> Calculates a random workload value. If 90 or greater, sets is_healthy to False.



<h2> Controllers </h2>

Properties:
> robots_serial_numbers (list): List of serial numbers for robots under management.
> robots_managed (list): List of Robot objects under management.
> active_robots (list): Subset of robots_managed that are currently active.
> points (int): Represents the controller's own point consumption for effort (doesn't directly impact robot operation).
> moves_left (int): Available actions for the current round (resets to 100 each round).

Behavior
> get_robot(serial_number): Retrieves the Robot object corresponding to a serial number using the robots dictionary.
> add_robots(): Populates the robots_managed list with Robot objects.
> read_active_status(robot): Checks if a robot is active, costs 1 move.
> read_healthy_status(robot): Checks if a robot is healthy, costs 1 move.
> repair_robot(robot): Resets a robot health to True, costs 1 move.
> work(current_round): Orchestrates controller actions within action limits.
> Prioritizes repair of unhealthy robots.
> Deducts 20 points if any actions were performed during a round.


<h2> Command Center </h2>

Properties:
> no_of_rounds (int): Total rounds for the simulation.
> no_of_controllers (int): Number of controllers in the simulation.
> no_of_robots (int): Number of robots in the simulation.
> total_points (int): Aggregate point score.
> points_per_round (list): Stores point totals after each round.
> robots_serial_numbers (list): Serial numbers of all robots.
> controller_list (list): List of Controller objects.

Behavior
> create_robots(): Initializes the robots dictionary.
> create_controllers(): Creates controllers and distributes Robot objects to them.
> run_simulation(): Executes the main round loop, calling work() on robots and controllers, and updates scores.
> display_plot(): Generates an animated plot of points_per_round.


