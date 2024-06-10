## What is Robot Control?
* In simple words, its the connection between **limbs(mechanics)** of the bot to its **brain(software)**.

* In technial terms - A system that can command, direct or regulate itself or another system to achieve a certain goal.

## Before diving in, here are some terms

* **System**: A combination or arrangement of a number of different physical components to form a whole unit such that that combining unit performs to achieve a certain goal.

* **Plant or process**: The part or component of a system that is required to be controlled.

* **Input**: It is the signal or excitation supplied to a control system.

* **Output**: It is the actual response obtained from the control system.

* **Disturbances**: The signal that has adverse effect on the performance of a control
system.

* Basically, there are two types of systems
    - Open loop systems
        - A control system in which the control action is totally independent of the output of the system.
        - Manually controlled systems are also categorised as open loop systems.
        - Such systems can been seen as in microwaves, washing machines etc, where we set the timer and that action takes place for that certain amount of time.
        
    <p align="center">
    <img width = "600" height = "150" src = "eqns/ol.jpeg">
    <p align = "center">
    <i>open loop control</i>
    </p>  

    - Closed loop Systems
        - A control system in which the control action adjusts itself according to the output generated to acheive a certain objective.

        - The difference between open loop system and closed loop system is the **feedback** closed loop system takes from the output.

        - The feedback gives an idea about the output which is then compared with the **desired action**. the deviation in output w.r.t to desired value is **error**. The controller tries to minimize this error.

        - Such systems can be seen all around us, some are present in electric irons, geysers to maintain a fixed temprature and many more!!

    <p align="center">
    <img width = "600" height = "200" src = "eqns/cl.jpeg">
    <p align = "center">
    <i>closed loop control</i>
    </p> 

### Feels complicated? 
Well, it'll be all worth it once you make your robots do this
- [![Controls-And-Dynamics](https://img.youtube.com/vi/us_sHHnyMvQ/0.jpg)](https://youtu.be/us_sHHnyMvQ)

- or maybe even this -  
- [![Controls-And-Dynamics](https://img.youtube.com/vi/fn3KWM1kuAw/0.jpg)](https://youtu.be/fn3KWM1kuAw)

### Phew!!! Now lets get into some real physics and maths

## Mathematical Modelling
This is the first step, which will walk us through the steps to derive dynamics equations of the system, analyzing the behavior of the system from the math and applying appropriate control strategy on the system to balance the system in an inherently unstable position.

### Modeling of non-linear Dynamical Systems
In mathematics and science, a non-linear system is a system in which the change of the output is not linearly proportional to the change of the input. Non-linear problems are of interest to engineers, biologists, mathematicians etc because most systems that occur in nature are inherently non-linear.
Non-linear dynamical systems that describe changes in variable over time may often appear chaotic, unpredictable or counter-intuitive in nature, contrasting with much simpler linear systems.

Typically the behavior of a non-linear system is described as a set of simultaneous equations in which the unknowns (or unknown functions in the case of differential equations) appear as variables of a polynomial of degree higher than one. Such a system is called a non-linear system of equations.

We will deal with dynamical systems that are modeled by a finite number of coupled first order ordinary differential equations

### Equations

$$
\dot{x}_1 = f_1(t, x_1, \ldots, x_n, u_1, \ldots, u_p)
$$
$$
\dot{x}_2 = f_2(t, x_1, \ldots, x_n, u_1, \ldots, u_p)
$$

$$
\vdots
$$

$$
\dot{x}_n = f_n(t, x_1, \ldots, x_n, u_1, \ldots, u_p)
$$


Here ẋ₁, ẋ₂,…ẋₙ denote the derivative of x₁, x₂…xₙ respectively with respect to time variable t and u₁, u₂,… uₚ etc are specified input variables. We call the variables x₁, x₂, …xₙ the state variables.

State Variables are used to to represent the memory the dynamical system has of its past or the desired variable of interest. We usually use vector notation to write these equations in a compact form.

#insert image

We can rewrite the n first-order differential equations as one n-dimensional first-order vector differential equation

$$
\dot{x} = f(t, x, u)
$$
#### Let's dive a bit deeper
## Linear systems

Linear systems are those whose states are governed by Linear differential equation below
<p align="center">
<img width="150" height = "90" src = "eqns/ld.png">
</p>

Where, A is a **NxN square matrix** representing the dynamics of the system. And x is  the **Nx1 state vector** representing the current state of the system.

The state consists of the variables that are used to define the current state of affairs of the system. eg: For a robots, it may be its current position and velocity, then Matrix A will be representing the dynamics relating the derivatives of position and velocity to their current values.


### How to form equations for a system?
<p align = "center">
<img width = "300" height = "300" src = "eqns/meme1.png">
</p>
Well, only few systems follow Linear characterisitcs, few others can be approximated on some conditions.

We'll get to those, first we look at one simple linear system - the spring and mass system

<p align = "center">
<img width = "400" height = "200" src = "eqns/stpring.png">
<p align="center">
<i>Brings back memories...eh?</i>
</p>

The state eqution for this system can be easily derived using Newton's Laws, but with increasing complexity of the system, use of Lagrangian is preffered as it gives the dynamics eqn with relative ease. Refer [here](https://youtu.be/KpLno70oYHE).

Either way we arrive at the eqn
<p align = "center">
<img width = "200" height= "90" src = "eqns/mass_eqn.png">
</p>

Note that here x reperesnts the displacement of mass from the normal position.

Taking $ {x}$ and $\dot{x} $ to be our states, the above eqn can be written as -
<p align = "center">
<img width = "400" height = "150" src = "eqns/linear_eqn.png">
<p align="center"> <i> Linear equation for spring mass system</i>
</p>

<p align = "center">
<img width = "250" height = "" src = "eqns/meme2.png">
</p>

## What to do with non-linear systems?

Most Real world systems are quite complex making them hard to be represented in linear forms, so we use certain methods to model them like one.

Linear or non-linear, all systems have a relation between change of stte and current state, let a non-linear system be as follows (f(x) is any non-linear function)
<p align = "center">
<img width = "200" height = "80" src = "eqns/non_lin.png">
</p>

Now, the non-linear system can be linearized about certain fixed states given as 
<p align = "center">
<img width = "200" height = "80" src = "eqns/non_lin2.png">
</p>

### Deriving the equations of motion for Non-Linear systems

The small example used for the linear system used simple mechanics and Newton's Laws of Motion. However for linearising a Non-Linear system we can go about two ways:

### i) NLM Method

Lets understant this whole process by solving the equations for a simple Pendulum

##insert bob figure
<p align = "center">
<img width = "330" height = "300" src = "eqns/bob.png">
</p>
<p align="center"> <i> Fig 1</i>
</p>

Consider a simple pendulum shown in Fig 1, where <i>l</i> denotes the length of rod and <mi></i> denotes the mass of the bob. Assume the rod is rigid and has zero mass. Let <i>θ</i> denote the angle subtended by the rod and the vertical axis through the pivot point.

The pendulum is free to swing in the vertical plane, The bob of the pendulum moves in a circle of radius <i>l</i>. To write the equations of motion, let us identify the forces acting on the bob.

- Downward gravitational force mg where g is acceleration due to gravity.

- Frictional force resisting motion which can be assumed to be proportional to the speed of the bob with a coefficient of friction k.

Using the Newton’s second law of motion, the equation of motion for the bob in the tangential direction of motion can be written as

<p align = "center">
<img width = "150" height = "30" src = "eqns/pd1.png">
</p>
To obtain the State Equation for the pendulum, the state variables can be assumed as
 $ {x_1} = \{theta}, \quad {x_2} = \dot{\theta}$ 
The state equations for the pendulum model are:
<p align = "center">
<img width = "200" height = "80" src = "eqns/pd2.png">
</p>
It is possible to find the <b>equilibrium points</b> of this system by setting the <b>state derivatives</b> to zero and then solving for x1 and x2.
<p align = "center">
<img width = "200" height = "80" src = "eqns/pd3.png">
</p>
The equilibrium points are located at (nπ,0) for n = ±1,±2,… . From the physical descriptions of the pendulum, it is clear that there are only two equilibrium positions (0,0) and (π,0). The rest of equilibrium points are just repetitions based on number of full swings of the pendulum.

Hence this is how a simple physical system is modeled.

#### Stable and Unstable Equilibrium Points
A typical problem that arises while dealing with non-linear dynamical systems is to check if a system is stable or unstable at a given equilibrium point.

<b>Equilibrium</b> Point of a system is the point at which the state of the system doesn’t change. The equilibrium points can be estimated by setting ẋ₁=0 and ẋ₂ = 0 and solving the given equations for x₁ and x₂.

<b>Stable Equilibrium</b> - If a system always returns to the equilibrium point after small perturbations.

<b>Unstable Equilibrium</b> - If a system moves away from equilibrium point after small perturbations.

Consider the following set of coupled equations as given below.
<p align = "center">
<img width = "200" height = "80" src = "eqns/pd4.png">
</p>

We will discuss the steps in order to compute the stability of system.

1. Calculate the equilibrium points of the system by setting the values of ẋ₁ = ẋ₂ = 0.
<p align = "center">
<img width = "200" height = "80" src = "eqns/pd5.png">
</p>
    ​By solving the above two equations, the values of equilibrium point are :(0,0) , (-1,1) & (1,-1)
    
2. inearize the set of equations by calculating the Jacobian.
    Behavior of Non-linear systems is very hard to analyse. Linearization is a method which involves creating a linear approximation of a non-linear system that is valid in a small region around the operating point (in this case, the equilibrium points).

    In order to linearize a set of equations, we need to first calculate the Jacobian for a set of equations. You can read more about Jacobian [here](https://mathworld.wolfram.com/Jacobian.html)

    Consider the following:

    The Jacobian J for the set of equations can be calculated as:
<p align = "center">
<img width = "200" height = "100" src = "eqns/pd6.png">
</p>

3. Substitute the value of the equilibrium points in the matrix J to find 3 matrices J₁, J₂ and J₃.
<p align = "center">
<img width = "200" height = "130" src = "eqns/pd7.png">
</p>

4. Calculate the eigenvalues of each of the matrices.

    Eigen values of state matrices represent poles of a system. The poles decides the stability of a system and if the poles are on the negative half of the complex plane i.e. they have the negative real part then the system is stable and if the real part is positive the system is unstable. A system is marginally stable if it has simple poles (non repeated) on imaginary axis and unstable if it is repeated. Hence by intuition you can see that for simple pendulum case the pendulum in downward position is stable and in upright position it is unstable. Find the Jacobian around the two equilibrium points and verify the same. [Eigen values and Eigen vectors](https://www.mathsisfun.com/algebra/eigenvalue.html)

    The eigenvalues can be calculated by constructing the characteristic equation of the matrix and equating it to zero.

    For equilibrium point (0,0) :-
<p align = "center">
<img width = "200" height = "200" src = "eqns/pd8.png">
</p>

 For equilibrium point (-1,1) and (1,-1):   
<p align = "center">
<img width = "200" height = "200" src = "eqns/pd8.png">
</p>

6. Check the real part of the eigenvalues calculated for each equilibrium points.

    For each Equilibrium point

    ● If all the eigenvalues have negative real part, the system is Stable at the given Equilibrium point.

    ● If even one of the eigenvalues has positive real part, the system is Unstable at the given Equilibrium point.

    ​ For Equilibrium Point (0,0), the eigenvalues are (-1-i) and (-1+i). Since both eigenvalues have negative real part, the system is Stable.

    ​ For Equilibrium Points (1,-1) and (-1,1), the eigenvalues are (2+2√2) and (2-2√2). Since one of the eigenvalues has a positive real part, the system is Unstable.

<p align = "center">
<img width = "200" height = "300" src = "eqns/falling-robot.gif">
<p align = "center">
<i> Just keep going!! it'll be worth it. </i>
</p>

### ii) Euler-Lagrange method 
The Euler-Lagrange method states that the equations of motion of a system can be obtained by solving the following equation:
<p align = "center">
<img width = "200" height = "100" src = "eqns/el.png">
<p align = "center">
(Assuming that there are no non-conservative forces acting on the system)
Here,

L is the Lagrangian which is the difference between the Kinetic energy and Potential energy of the system.

Hence 

$L = K.E - P.E$

x and ẋ are the state variables (In our case here, position and velocity respectively) in generalized coordinate system.

We will try to understand this using an example.

Consider the following system:
<p align = "center">
<img width = "300" height = "200" src = "eqns/fall.png">
<p align = "center">

A point mass m is raised to height y. We need to calculate the equations of motion using the Euler-Lagrange method.

Firstly we calculate the KE and PE. Then use those values to calculate the Lagrangian L.
<p align = "center">
<img width = "400" height = "200" src = "eqns/fall_eqn.png">
<p align = "center">

Equation (1) is self explanatory. The mass is raised to height y. So the potential energy stored in mass will be mgy.

Equation (2) is slightly tricky to understand. We know that kinetic energy of a point mass is (1/2) x mass x (velocity)^2. Now velocity v is nothing but rate of change of y with respect to t. Hence v can be written as dy/dt or ẏ

Equation (3) represents the Lagrangian (L) which is the difference between the KE and PE of the system.

Now we calculate the Euler Lagrange equations of motion.
<p align = "center">
<img width = "400" height = "300" src = "eqns/fall_eqn2.png">
<p align = "center">

Equation (6) gives the final answer. Here ÿ represents the acceleration.

Equation (6) makes sense as only gravitational force is acting on the system. Hence the acceleration of the system is the acceleration due to gravity.

If we had used the Newton’s laws of motion, we would have arrived at the same result, albeit in a different way.

Let us now consider a somewhat more complex example.
<p align = "center">
<img width = "530" height = "300" src = "eqns/bob2.png">
<p align = "center">

We have our pendulum equation whose equations of motion we demonstrated in previous Task using Newtons Laws of motions. Now we will demonstrate the same using Euler-Lagrangian method.

In this system, we have a pendulum. The mass of the bob is given as m. The length of rod to which the bob is attached to is l. We have assumed the rod to be rigid and have no mass. So all the mass is concentrated to the bob.

While swinging, at any arbitrary point in the pendulum’s trajectory, the pendulum can assumed to be at a height h from the bottom. h can be written as a function of θ where θ is the angle the pendulum bob makes with the vertical.

<p align = "center">
<img width = "130" height = "50" src = "eqns/bob2_eqn1.png">
<p align = "center">

First, we need to calculate the Lagrangian L for this system. For that we need to compute the kinetic energy and potential energy of this system.

Calculating the potential energy is pretty straightforward.

<p align = "center">
<img width = "500" height = "50" src = "eqns/pe.png">
<p align = "center">

The kinetic energy will be defined by (1/2) x mass x velocity^2. Here the velocity is the tangential velocity of the bob. We can take x and y components of velocity v and solve for kinetic energy using those equations.

However, we can use rotational mechanics to make our calculations simpler. Since the pendulum bob is oscillating in a circular trajectory, the kinetic energy can be given by

<p align = "center">
<img width = "110" height = "50" src = "eqns/ke3.png">
<p align = "center">

Where I is the moment of inertia and ω is the angular velocity.

But we know
<p align = "center">
<img width = "300" height = "40" src = "eqns/iw.png">
<p align = "center">

Angular velocity ω can be written as rate of change of θ with respect to time. Hence we can write ω= (dθ/dt).

Therefore we have the expression for kinetic energy
<p align = "center">
<img width = "600" height = "60" src = "eqns/ke2.png">
<p align = "center">

Now we have the expressions for PE and KE we will calculate the Lagrangian L and use it to calculate the equations of motion for this system.

<p align = "center">
<img width = "600" height = "60" src = "eqns/L.png">
<p align = "center">

Since L is a function of θ, we need to select θ and θ as state variables of the system. Hence the equations of motion can be calculated as:
<p align = "center">
<img width = "700" height = "300" src = "eqns/l2.png">

In previous Task, we had used the same pendulum example and calculated the equations of motion for pendulum using Newton’s laws. We can confirm that the same equations have been derived using the Euler-Lagrange method.

Suppose we take $ x_1={theta}$ and $x_2={theta_dot}$
We can express the equations we formed in the following way
<p align = "center">
<img width = "200" height = "120" src = "eqns/sv.png">
<p align = "center">

In this way we have a two equations that govern our system.

What happens if there is any external force acting on the system?
<p align = "center">
<img width = "400" height = "300" src = "eqns/bob3.png">
<p align = "center">

In the given simple pendulum system, we have applied an external torque to the system.

In this case, the Euler-Lagrange equation formed will be slightly different.
<p align = "center">
<img width = "200" height = "80" src = "eqns/l3.png">
<p align = "center">

Any non-conservative force acting on the system (Since states chosen are angular position and velocity that’s why force should also be taken as angular force i.e. Torque. In case we use linear motions as in the first example then we’ll use external linear force on the right hand side.) appears on the right side of the Euler-Lagrange equation. Consequently the equations of motion derived for this pendulum system will be as follows:
<p align = "center">
<img width = "250" height = "120" src = "eqns/sv2.png">
<p align = "center">

You can see that there is an additional term in the second equation. We can check if this term is dimensionally correct.

We know x₁ is the angular position θ of the pendulum bob (with respect to vertical) and x₂ is the angular velocity theta.dot of the bob. Hence ẋ₁ = x₂ will correspond to the angular velocity theta.dot and ẋ₂ will be the angular acceleration theta.double.dot. Let the angular acceleration be denoted by α.

The units and dimensions of α are rad/s^2 and [T^(-2) ] respectively.

We know T=Iα (where T= torque, I = moment of inertia, α=angular acceleration) and I = m*L^2.

(T/mL^2) equals angular acceleration α. Hence the last term is an angular acceleration term which is consistent with the equation. We can also calculate the dimensions of this term to verify. It will always come as [T^(-2) ]. This method is helpful to verify if or equations are valid.

### Introduction to State Space Modelling
We had briefly covered State Variables and State Equations in previous Task. In this section we will further elaborate on that topic and discuss the various control techniques that are associated with that.

In control engineering, a state-space representation is a mathematical model of a physical system as a set of input, output and state variables related by first-order differential equations or difference equations. State variables are variables whose values evolve through time in a way that depends on the values they have at any given time and also depends on the externally imposed values of input variables. Output variables’ values depend on the values of the state variables.

The state space equations for a linear time invariant system (LTI) system can be given as follows:
<p align = "center">
<img width = "500" height = "60" src = "eqns/ssm.png">
<p align = "center">

Here

x(t)- State Vector (n x 1 matrix)

y(t)- Output Vector (p x 1 matrix)

u(t)- Input Vector (m x 1 matrix)

A - State (or system) matrix (n x n matrix)

B - Input matrix (n x m matrix)

C - Output Matrix (p x n matrix)

D - Feed-forward matrix (p x m matrix)

where p, m, n are:

We won’t go into the theory of how these equations came into being. That’s a lot of complicated math that cannot be covered here. You can refer to good Control Systems books.

Consider a set of equations:
<p align = "center">
<img width = "500" height = "60" src = "eqns/ssm2.png">
<p align = "center">

We want to express this set of equations into the form
<p align = "center">
<img width = "500" height = "60" src = "eqns/ssm3.png">
<p align = "center">

Notice, we have neglected the Bu term in this equation. That’s because our system doesn’t have any input. It only has state variables x₁ and x₂.

Can we express the set of equations (1) in terms of (2)??

The answer is no, we cannot. (1) is a set of non linear equations while (2) is a set of linear equations. However, if we linearize (1), it might be possible to express (1) in terms of (2).

How do we linearize (1)? That was basically the whole point of previous Task.

1. <b>Find the equilibrium points</b>

    We want to find the point around which the system is stable. To find the equilibrium points we need to set ẋ₁ = 0 and ẋ₂=0. Then solve the equations for

    x₁ and x₂.
    <p align = "center">
    <img width = "400" height = "100" src = "eqns/ssm4.png">
    <p align = "center">

    If we solve (3) for x₁ and x₂ we will get the equilibrium points as (0,0), (1,√2) and (1,-√2).
2. <b> Calculate the jacobian of the system of equations</b>

    The jacobian J for the system of equations (3) will be:
    <p align = "center">
    <img width = "500" height = "180" src = "eqns/ssm5.png">
    <p align = "center">
3.  <b>Construct the state equation for each equilibrium point.</b>

    The state equation for equilibrium point (0,0) will be:
    <p align = "center">
    <img width = "500" height = "180" src = "eqns/ssm6.png">
    <p align = "center">

    Therefore the set of equations has been expressed in the form:

    <p align = "center">
    <img width = "500" height = "40" src = "eqns/ssm7.png">
    <p align = "center">

    It is very important to note that this approximation of the set of non-linear equations given in (3) will only hold true for point close to the equilibrium point (0,0).

    This means that around the vicinity of the equilibrium point (0,0), the non-linear system will behave like a linear system and the state equation given above will hold true around the vicinity of that point.

    Likewise, the state equations for equilibrium points (1,√2) and (1,-√2) are:
    <p align = "center">
    <img width = "500" height = "180" src = "eqns/ssm8.png">
    <p align = "center">

### Stability

We can find out whether the system is stable or unstable at each of the equilibrium points by finding out the eigenvalues of the A matrix. If any of the eigenvalues have a positive real part, the system will be unstable.

So, for equilibrium point (1, √2) of the system, the eigenvalues will be -2.824 and 1.414. Hence system will be unstable.

<b>Introducing Control Input</b>

Let us consider the Pendulum with external applied torque system.

We derived the equations for this system as:
<p align = "center">
    <img width = "500" height = "90" src = "eqns/st1.png">
    <p align = "center">

We can apply the same linearization technique explained above.

1. <b>Find the equilibrium points.</b>

    If we set ẋ₁ = 0 and ẋ₂=0, we will find the equilibrium points of this system as (nπ,0) where n=0,±1,±2,… .From the physical descriptions of the pendulum, it is clear that there are only two equilibrium positions (0,0) and (π,0). The rest of equilibrium points are just repetitions based on number of full swings of the pendulum.

    The equilibrium point (0,0) will be when the pendulum bob is vertically downwards.

    The equilibrium point (π,0) will be when the pendulum bob is vertically upwards.

    Intuitively, we can guess that the system will be stable at equilibrium point (0,0) and unstable at equilibrium point (π,0). Let us see if our intuition is correct.

2. <b>Calculate the jacobian of the system of equations.</b>

    The jacobian J₁ for the A matrix of the state equation will be:
    <p align = "center">
    <img width = "500" height = "200" src = "eqns/st2.png">
    <p align = "center">

    Since our system has input, we also need to calculate jacobian J₂ for the B matrix.

    J₂ will be:
    <p align = "center">
    <img width = "500" height = "200" src = "eqns/st3.png">
    <p align = "center">
3. <b> For each equilibrium point, substitute value of (x₁,x₂) in the jacobian and calculate the A and B matrix.</b>

    The values of A matrix for each equilibrium point will be given as:
    <p align = "center">
    <img width = "500" height = "100" src = "eqns/st4.png">
    <p align = "center">

    The values of B matrix for all equilibrium points will be:
    <p align = "center">
    <img width = "500" height = "80" src = "eqns/st5.png">
    <p align = "center">

4. <b>Construct the state equation for each equilibrium point.</b>

    The state equation for equilibrium point (0,0) will be:
    <p align = "center">
    <img width = "500" height = "100" src = "eqns/st6.png">
    <p align = "center">

5. <b>Check the stability of the system at each equilibrium point.</b>

    At equilibrium point (0,0) the eigenvalues will be:
    <p align = "center">
    <img width = "500" height = "60" src = "eqns/st7.png">
    <p align = "center">

    The eigenvalues for (0,0) will be purely imaginary. Hence the system will be marginally stable. Marginally stable means that system will be continue to oscillate about the equilibrium point indefinitely.

    The eigenvalues for (π,0) will be purely real. One of the eigenvalues will have positive real part. Hence the system will be unstable.

    Hence we proved that our earlier intuitions about the stability of the system are correct. The system will be stable for (0,0) and unstable for (π,0).

### Controllability and Observability

In control theory, controllability and observability are two very important properties of the system.

Controllability is the ability to drive a state from any initial value to a final value in finite amount of time by providing a suitable input. A matrix which determines if a system is fully controllable or not is called the controllability matrix.

Observability is the property of the system that for any possible sequnce of state and control inputs, the current state can be determined in finite time using only the outputs. A matrix which determines if a system is fully observable or not is called the observability matrix. A fully observable system means that it is possible to know all the state variables from the system outputs.

<p align = "center">
    <img width = "500" height = "600" src = "eqns/c1.png">
    <p align = "center">

Rank of a matrix is defines as the maximum number of linearly independent rows or columns in a matrix.

In the pendulum example (with external torque), we have the A and B matrix available to us. Hence we can calculate the controllability of the system.

[![Rank of a Matrix](https://img.youtube.com/vi/MxGJeli6qOc/0.jpg)](https://youtu.be/MxGJeli6qOc)

### Congratulations for making it to the end of subpart-1

<p align = "center">
    <img width = "300" height = "300" src = "eqns/image.png">
    <p align = "center">

## Task 1
### Rules of attempting the task:

- [This](https://drive.google.com/file/d/1FE2hlQhfYbM2snSqgf_aZrtLcdeJhqMz/view?usp=sharing) is the PDF file contains 5 questions with a total of 105 points
- It is mandatory to attempt each question
- Ques 1-4 have weightage of 10 points each
- Ques 5 is of 50 points and 6 is of 15 points
- You have to submit the your solutions in PDF file
- Answers to the questions can handwritten or typed
- You can take help of MATLAB or any other software to verify your answers.
- You can type the equations using Latex editor
- Any relevant diagram related to the question is appreciated and will earn you bonus points.

## References :

<b>We Ignore it, but wikipedia is still one of the most powerful tools [Inverted pendulum](https://en.wikipedia.org/wiki/Inverted_pendulum)

Most popular Rotary Inverted Pendulum around - you can find jackpot of papers on it [Rotary Inverted Pendulum](https://www.quanser.com/products/rotary-inverted-pendulum/)

Did you know this Nickname ? [Furuta pendulum](https://en.wikipedia.org/wiki/Furuta_pendulum)

You must be knowing Brian, don’t you?
[check this out](https://www.youtube.com/playlist?list=PLfqhYmT4ggAtpuB1g8NbgH912PwYjn_We )</b>
