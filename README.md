# Project_2_EDA

Vanguard A/B Test (Second project for Ironhack)

As part of its ongoing commitment to improving the digital client experience, Vanguard has introduced a new user interface (UI) enhancement featuring real-time, context-sensitive prompts. These updates aim to make the online process more seamless, user-friendly, and efficient for clients navigating investment tasks.

To evaluate the effectiveness of these enhancements, the Customer Experience team launched an A/B testing initiative. The purpose of this analysis is to determine whether these UI improvements positively influence client behavior. Specifically, we aim to assess whether the new design:

- Increases the overall process completion rate
- Reduces the time clients spend on each step
- Minimizes user errors during the process

This project explores the outcomes of the experiment, guided by a data-driven approach to test these key hypotheses and help Vanguard make informed, client-centered design decisions.


Project Structure :
- Data : Raw and Clean.
- Notebooks : Jupyter Notebooks with detailed analysis.
- Graphics and Dashboard : Tableau
- README.md: Project documentation.

Project Overview :

- Introduction  
- Exploratory Data Analysis (EDA) 
- Performance Metrics 
- Experiment Evaluation
- Tableau Visualizations
- Teamwork & Project Management 
- Challenges & Learnings 
- Conclusion 


Data Overview : 

We use three datasets provided by the company as follows :

- Client Profiles (df_final_demo): Demographics like age, gender, and account details of our clients.
- Digital Footprints (df_final_web_data): A detailed trace of client interactions online.
- Experiment Roster (df_final_experiment_clients): A list revealing which clients were part of the grand experiment.


Exploratory Data Analysis (DA) :
- Data Cleaning
- Numerical Measures


Methodology and Languages:
- Python
- Tableau


Performance Matrics: 

- Completion Rate
- Time Spent on Each Step
- Error Rates
- Duration of a Successful Process


Hypotheses:  

- Whether the average age of clients engaging with the test group is the same as those engaging with the control group
- Whether the average age of clients in control group is greater than those engaging with test group
- Whether the proportion of males and females differs between the Test and Control groups
- Whether the difference of the Error rate significant:
- Test whether the difference of average duration of a successful process is significant


Findings: 

- The difference in Completion rates is statistically significant.
- The difference in time spent per step is statistically significant.
- The difference error rate is statistically significant.
- The difference in duration of a successful process is statistically significant.

Conclusion and Recommendation :

The difference in completion rate and the new modern user interface make us recommend to implement the new digital experience. Nevertheless, the error rate needs to be improved in order to guarantee a positive customer experience. 


Presentation link:

https://docs.google.com/presentation/d/1VngpZ_blF-hf0yX3lHXD5oC7PmUJ7e2ij7u5i6U2DvY/edit?slide=id.gc6f980f91_0_42#slide=id.gc6f980f91_0_42

Trello Link: 

https://trello.com/b/hpf3Ey9Z/vanguarabtestproject
