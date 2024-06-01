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
    <img width = "600" height = "150" src = "control_loop_images/open_loop.png">
    <p align = "center">
    <i>open loop control</i>
    </p>  

    - Closed loop Systems
        - A control system in which the control action adjusts itself according to the output generated to acheive a certain objective.

        - The difference between open loop system and closed loop system is the **feedback** closed loop system takes from the output.

        - The feedback gives an idea about the output which is then compared with the **desired action**. the deviation in output w.r.t to desired value is **error**. The controller tries to minimize this error.

        - Such systems can be seen all around us, some are present in electric irons, geysers to maintain a fixed temprature and many more!!

    <p align="center">
    <img width = "600" height = "200" src = "control_loop_images/closed_loop.png">
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


