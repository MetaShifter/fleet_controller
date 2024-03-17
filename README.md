<h1> Project Description </h1>

<p>
This project simulates a robot fleet management system. The goal is to accumulate points over a series of rounds.
</p> 

<h3> Key components include: </h3>

<ul>
    <li>Robots: Autonomous units that become active within a designated round window. They generate points while healthy but can cause penalties when unhealthy. </li>
    <li> Controllers: Manage a subset of robots. Controllers monitor robot status and can perform repairs but are limited in the number of actions per round. </li>
    <li> Command Center: Oversees the simulation, initializes robots and controllers, and tracks overall score. </li>
</ul>

<h1> Design & Algorithm choices </h1>
<section> 
The core of the design is built using OOP, around three central classes:
<ul>
    <li> Robot: Encapsulates all the properties of an individual robot, including the state transition logic ( work ). </li>
    <li> Controller: Manages a subset of robots, monitoring robot status and performing repairs. </li>
    <li> CommandCenter: Acts as the coordinator, setting up the environment and running the simulation loop. </li>
</ul>

<br>
During problem designing phase, I figured out that using a dictionary for robots provides central access to all Robot objects by their serial number, enabling efficient lookup by controllers in O(1) time complexity.
</section>



<h1> Model </h1>
<h2> Robots </h2>

<h3> Properties:</h3>
<ul>
    <li> serial_number (string): Unique identifier for each robot.</li>
    <li> activation_round (int): The round in which the robot becomes active.</li>
    <li> deactivation_round (int): The round in which the robot becomes inactive.</li>
    <li> is_active (bool): Indicates whether the robot is currently active.</li>
    <li> is_healthy (bool): Indicates whether the robot is in a healthy state.</li>
    <li> points_generated (int): Cumulative points generated or lost by the robot.</li>
</ul>

<h3> Behavior</h3>
<ul>
    <li> work(current_round): Simulates the robot's task for the round.</li>
    <li> Checks activation_round and deactivation_round to determine activity status.</li>
    <li> Generates 1 point if is healthy, active and workload <90; otherwise, loses 10 points if workload>=90.</li>
    <li> Calculates a random workload value. If 90 or greater, sets is_healthy to False.</li>
</ul>


<h2> Controllers </h2>

<h3> Properties:</h3>
<ul>
    <li> robots_serial_numbers (list): List of serial numbers for robots under management.</li>
    <li> robots_managed (list): List of Robot objects under management.</li>
    <li> active_robots (list): Subset of robots_managed that are currently active.</li>
    <li> points (int): Represents the controller's own point consumption for effort (doesn't directly impact robot operation).</li>
    <li> moves_left (int): Available actions for the current round (resets to 100 each round).</li>
</ul>

<h3> Behavior</h3>
<ul>
    <li> get_robot(serial_number): Retrieves the Robot object corresponding to a serial number using the robots dictionary.</li>
    <li> add_robots(): Populates the robots_managed list with Robot objects.</li>
    <li> read_active_status(robot): Checks if a robot is active, costs 1 move.</li>
    <li> read_healthy_status(robot): Checks if a robot is healthy, costs 1 move.</li>
    <li> repair_robot(robot): Resets a robot health to True, costs 1 move.</li>
    <li> work(current_round): Orchestrates controller actions within action limits.</li>
    <li> Prioritizes repair of unhealthy robots.</li>
    <li> Deducts 20 points if any actions were performed during a round.</li>
</ul>

<h2> Command Center </h2>

<h3> Properties:</h3>
<ul>
    <li> no_of_rounds (int): Total rounds for the simulation.</li>
    <li> no_of_controllers (int): Number of controllers in the simulation.</li>
    <li> no_of_robots (int): Number of robots in the simulation.</li>
    <li> total_points (int): Aggregate point score.</li>
    <li> points_per_round (list): Stores point totals after each round.</li>
    <li> robots_serial_numbers (list): Serial numbers of all robots.</li>
    <li> controller_list (list): List of Controller objects.</li>
</ul>

<h3> Behavior </h3>
<ul>
<li> create_robots(): Initializes the robots dictionary.</li>
<li> create_controllers(): Creates controllers and distributes Robot objects to them.</li>
<li> run_simulation(): Executes the main round loop, calling work() on robots and controllers, and updates scores.</li>
<li> display_plot(): Generates an animated plot of points_per_round.</li>
</ul>

