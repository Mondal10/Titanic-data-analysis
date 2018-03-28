# Titanic-data-analysis (not prediction)
install python 
install libraries : matplotlib, numpy, pandas, no need to install seaborn since predictionn is not done 
install jupyter notebook : for installing jupyter notebook 
1. Open command prompt 
2. Go to c: drive by using "cd.." command
3. Now navigate to the folder where python is installed, in my case its installed here "C:\Users\Whatever_is_your_user_name\AppData\Local\Programs\Python\Python36-32\Scripts" 
4. Once you are in the scripts directory use "pip install jupyter"
5. Once its done open jupyter notebook on your browser

Open the titanic.ipynb on jupyter

# Data Description:
survival: Survival (0 = No; 1 = Yes)</br>
pclass: Passenger Class (1 = 1st; 2 = 2nd; 3 = 3rd)</br>
name: Name </br>
sex: Sex </br>
age: Age </br>
sibsp: Number of Siblings/Spouses Aboard  </br>
parch: Number of Parents/Children Aboard  </br>
ticket: Ticket Number  </br>
fare: Passenger Fare  </br>
cabin: Cabin  </br>
embarked: Port of Embarkation (C = Cherbourg; Q = Queenstown; S = Southampton)

# Special Notes:

Pclass is social/economic status 1st ~ Upper; 2nd ~ Middle; 3rd ~ Lower </br>
Age is in Years; Fractional if Age less than One (1) If the Age is Estimated, it is in the form xx.5 </br>
With respect to the family relation variables (i.e. sibsp and parch) some relations were ignored. The following are the definitions used for sibsp and parch. </br>

Sibling: Brother, Sister, Stepbrother, or Stepsister of Passenger Aboard Titanic </br>
Spouse: Husband or Wife of Passenger Aboard Titanic (Mistresses and Fiances Ignored) </br>
Parent: Mother or Father of Passenger Aboard Titanic </br>
Child: Son, Daughter, Stepson, or Stepdaughter of Passenger Aboard Titanic </br>
Other family relatives excluded from this study include cousins, nephews/nieces, aunts/uncles, and in-laws. Some children travelled only with a nanny, therefore parch=0 for them. As well, some travelled with very close friends or neighbors in a village, however, the definitions do not support such relations.
