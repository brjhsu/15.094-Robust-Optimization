# Code for MIT 15.094 Robust Optimization

Environment for 15.094, taught in Spring 2021. Most code is in Julia. Class project (15.094 Project.ipynb) involves robust optimization for supply and demand planning. In this project, we study robust profit maximization in a highly competitive market - the
taxi and ride share industry, where customer demand can rapidly change throughout the day.
For example, if we take the perspective of Uber in New York, clearly people trying to take a
ride to work in the morning absolutely need a ride and are more willing to pay high amounts.
Meanwhile, people taking a leisurely trip to the mall in the afternoon or weekend can afford
to consider other options (bus/train). On top of this, consumers can easily check prices of
competitor services, such as Lyft and see if they are offering reduced prices or coupons. This
represents an adversarial force on the demand for Uber’s products and creates a setting where
robust optimization can help us handle the worst-case uncertainty in demand sensitivity.

We study several settings including:
- Different uncertainty sets (box, budget, polyhedral)
- Comparison against nominal approach under uncertainty in demand
- Application of folding-horizon approach where we adjust prices as they are realized along the course of a day

Overall we show that we are able to make significant gains in profit under simulated data when using the robust approach as opposed to the nominal static-pricing policy. 
