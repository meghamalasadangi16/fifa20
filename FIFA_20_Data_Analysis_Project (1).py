#!/usr/bin/env python
# coding: utf-8

# #Title:**-PRCP-1004-Fifa20**

# # **Problem Statement**
# 
# **Task 1**:-Prepare a complete data analysis report on the given data.
# 
# **Task 2**:- Explore football skills and cluster football players based on their attributes.
# 
# **Task3**:- Explore the data and attempt all the below asked questions in a step by step manner:
# 
# * Prepare a rank ordered list of top 10 countries with most players. Which countries are producing the most footballers that play at this level?
# 
# * Plot the distribution of overall rating vs. age of players. Interpret what is the age after which a player stops improving?
# 
# * Which type of offensive players tends to get paid the most: the striker, the right-winger, or the left-winger?
# 

# # **Dataset Information**
#  FIFA 20 Football is arguably the most popular sport in the world and FIFA is the most popular football (soccer) simulation game by Electronic Arts (EA Sports).
# 
# The dataset provided includes the players data for the Career Mode from FIFA 15 to FIFA 20 ("players_20.csv"). The data allows multiple comparisons of the same players across the last 6 versions of the videogame.
# 
# Some ideas of possible analysis:
# 
# ●	Historical comparison between Messi and Ronaldo (what skill attributes changed the most during time - compared to real-life stats).
# 
# ●	Ideal budget to create a competitive team (at the level of top n teams in Europe) and at which point the budget does not allow to buy significantly better players for the 11-men lineup. An extra is the same comparison with the Potential attribute for the lineup instead of the Overall attribute.
# 
# ●	Sample analysis of top n% players (e.g. top 5% of the player) to see if some important attributes such as Agility or BallControl or Strength have been popular or not across the FIFA versions. An example would be seeing that the top 5% players of FIFA 20 are faster (higher Acceleration and Agility) compared to FIFA 15. The trend of attributes is also an important indication of how some attributes are necessary for players to win games (a version with more top 5% players with high BallControl stats would indicate that the game is more focused on the technique rather than the physical aspect).
# 

# # **Attributes Used In Project**
# 
# ●	**Name**: Name of the player.
# 
# ●	**Age**: Age of the player.
# 
# ●	**Height**: Height of the player in inches (transformed to centimeters in preprocessing).
# 
# ●	**Overall**: General performance quality and value of the player representing the key positional skills and international reputation rated between 1-99. Overall attribute is used only in preprocessing and discussion stages because using it in modelling could lead to domination by this feature. The aim of the project is not basically sort and categorize the players using their overall talent and international reputation, but to cluster them based on using their whole skillset.
# 
# ●	**Potential**: Maximum Overall rating expected to be reached by a player in the top of his career rated between 1-99.
# 
# ●	**PreferredFoot**: Right or Left. Label encoder is applied as 0 for left and 1 for right.
# 
# ●	**WeakFoot**: Represents how well a player uses his weak foot (e.g. left for righties) rated between 1 to 5.
# 
# ●	**WorkRate**: Degree of the effort the player puts in terms of attack and defense rated as low, medium and high. This feature is divided into two new features as AttackWorkRate and DefenseWorkRate. Besides, label encoder is applied as 0 for low, 0.5 for medium and 1 for high.
# 
# ●	**Position**: Position of the players on the pitch which determines their roles and responsibilities in the team. Forward positions in the football and FIFA 19 can be grouped as striker (ST: center striker, RS: right striker, LS: left striker), forward (CF: center forward, RF: right forward, LF: left forward) and winger (RW: right winger, LW: left winger). The word, forward, is used both as a general term and a special position. Strikers are positioned in front of forwards and wingers and very closed to the opposing goal. Their main responsibilities are attacking and scoring goals, that’s why their ball control, shooting and finishing skills are expected to be well. Center forwards are positioned right behind the strikers. They are expected to receive balls from the others and score assists to the others or goals. In addition to the skills expected from strikers, they have to be good at passing. Right forwards and left forwards are positioned at the right and left of the center forwards with the same expectations. Wingers are positioned near the touchlines to create chances for strikers and forwards from the right and left side of the field by breakthrough and crosses and to score goals. They are expected to be good at dribbling, acceleration, passing and crossing. Positions are used only in preprocessing and discussion stages.
# 
# ●	**ST**: Positional skill. Player’s general ability when playing in ST position rated between 1-99.
# 
# ●	**RS**: Positional skill. Player’s general ability when playing in in RS position rated between 1-99.
# 
# ●	**LS**: Positional skill. Player’s general ability when playing in in LS position rated between 1-99.
# 
# ●	**CF**: Positional skill. Player’s general ability when playing in in CF position rated between 1-99.
# 
# ●	**RF**: Positional skill. Player’s general ability when playing in in RF position rated between 1-99.
# 
# ●	**LF**: Positional skill. Player’s general ability when playing in in LF position rated between 1-99.
# 
# ●	**RW**: Positional skill. Player’s general ability when playing in in RW position rated between 1-99.
# 
# ●	**LW**: Positional skill. Player’s general ability when playing in in LW position rated between 1-99.
# 
# ●	**Crossing**: Crossing skill of the player rated between 1-99. Cross is a long-range pass from wings to center.
# 
# ●	**Finishing**: Finishing skill of the player rated between 1-99. Finishing in football refers to finish an attack by scoring a goal.
# 
# ●	**HeadingAccuracy**: Player’s accuracy to pass or shoot by using his head rated between 1-99.
# 
# ●	**ShortPassing**: Player’s accuracy for short passes rated between 1-99.
# 
# ●	**LongPassing**: Player’s accuracy for long passes rated between 1-99.
# 
# ●	**Dribbling**: Dribbling skill of the player rated between 1-99.
# Dribbling is carrying the ball without losing while moving in one particular direction.
# 
# ●	**SprintSpeed**: Speed rate of the player rated between 1-99.
# 
# ●	**Acceleration**: Shows how fast a player can reach his maximum sprint speed rated between 1-99.
# 
# ●	**FKAccuracy**: Player’s accuracy to score free kick goals rated between 1-99.
# 
# ●	**BallControl**: Player’s ability to control the ball rated between 1-99.
# ●	**Balance**: Player’s ability to remain steady while running, carrying and controlling the ball rated between 1-99.
# 
# ●	**ShotPower**: Player’s strength level of shooting the ball rated between 1-99.
# ●	**Jumping**: Player’s jumping skill rated between 1-99.
# 
# ●	**Penalties**: Player’s accuracy to score goals from penalty rated between 1-99.
# 
# ●	**Strength**: Physical strength of the player rated between 1-99.
# 
# ●	**Agility**: Gracefulness and quickness of the player while controlling the ball rated between 1-99.
# 
# ●	**Reactions**: Acting speed of the player to what happens in his environment rated between 1-99.
# 
# ●	**Aggression**: Aggression level of the player while pushing, pulling and tackling rated between 1-99.
# 
# ●	**Positioning**: Player’s ability to place himself in the right position to receive the ball or score goals rated between 1-99.
# 
# ●	**Vision**: Player’s mental awareness about the other players in the team for passing rated between 1-99.
# 
# ●	**Volleys**: Player’s ability to perform volleys rated between 1-99.
# 
# ●	**LongShots**: Player’s accuracy of shoots from long distances rated between 1-99.
# 
# ●	**Stamina**: Player’s ability to sustain his stamina level during the match rated between 1-99. Players with lower stamina get tired fast.
# 
# ●	**Composure**: Player’s ability to control his calmness and frustration during the match rated between 1-99.
# 
# ●	**Curve**: Player’s ability to curve the ball while passing or shooting rated between 1-99.
# 
# ●	**Interceptions**: Player’s ability to intercept the ball while opposite team’s players are passing rated between 1-99. It is a defensive skill.
# 
# ●	**StandingTackle**: Player’s ability to perform tackle (take the ball from the opposite player) while standing rated between 1-99. It is a defensive skill.
# 
# ●	**SlidingTackle**: Player’s ability to perform tackle by sliding rated between 1-99. It is a defensive skill.
# 
# ●	**Marking**: Player’s ability to apply strategies to prevent opposing team from taking the ball rated between 1-99. It is a defensive skill.  
# 

# # **Task 1 : Prepare a complete data analysis report on the given data.**

# ## **Import Basic Libraries**

# In[1]:


import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import warnings
warnings.filterwarnings("ignore")


# # **Loading** **data**

# In[2]:


data=pd.read_csv("players_20.csv")
data.head()


# ## **Basic Checks**

# In[3]:


data.sample(10)


# In[4]:


data.head()


# In[5]:


data.tail()


# In[6]:


data.dtypes


# In[7]:


data.info()


# In[8]:


data.describe().T


# In[9]:


cat_data=data.select_dtypes(include=["O"]).columns
cat_data


# In[10]:


## players belongs to which nanationality
data['nationality'].value_counts()


# In[11]:


num_data=data.select_dtypes(include=["int64","float64"]).columns
num_data


# # **Data** **Preprocessing**

# ## **Renamaing** **Columns**
# 

# In[12]:


data.rename(columns={'sofifa_id': 'Player_ID',
    'player_url': 'Player_URL',
    'short_name': 'Short_Name',
    'long_name': 'Full_Name',
    'age': 'Age',
    'dob': 'Date_of_Birth',
    'height_cm': 'Height_cm',
    'weight_kg': 'Weight_kg',
    'nationality': 'Nationality',
    'club': 'Club',
    'overall': 'Overall_Rating',
    'potential': 'Potential_Rating',
    'value_eur': 'Value_EUR',
    'wage_eur': 'Wage_EUR',
    'player_positions': 'Player_Positions',
    'preferred_foot': 'Preferred_Foot',
    'international_reputation': 'International_Reputation',
    'weak_foot': 'Weak_Foot',
    'skill_moves': 'Skill_Moves',
    'work_rate': 'Work_Rate',
    'body_type': 'Body_Type',
    'real_face': 'Real_Face',
    'release_clause_eur': 'Release_Clause_EUR',
    'player_tags': 'Player_Tags',
    'team_position': 'Team_Position',
    'team_jersey_number': 'Team_Jersey_Number',
    'loaned_from': 'Loaned_From',
    'joined': 'Joined',
    'contract_valid_until': 'Contract_Valid_Until',
    'nation_position': 'Nation_Position',
    'nation_jersey_number': 'Nation_Jersey_Number',
    'pace': 'Pace',
    'shooting': 'Shooting',
    'passing': 'Passing',
    'dribbling': 'Dribbling',
    'defending': 'Defending',
    'physic': 'Physic',
    'gk_diving': 'GK_Diving',
    'gk_handling': 'GK_Handling',
    'gk_kicking': 'GK_Kicking',
    'gk_reflexes': 'GK_Reflexes',
    'gk_speed': 'GK_Speed',
    'gk_positioning': 'GK_Positioning',
    'player_traits': 'Player_Traits',
    'attacking_crossing': 'Attacking_Crossing',
    'attacking_finishing': 'Attacking_Finishing',
    'attacking_heading_accuracy': 'Attacking_Heading_Accuracy',
    'attacking_short_passing': 'Attacking_Short_Passing',
    'attacking_volleys': 'Attacking_Volleys',
    'skill_dribbling': 'Skill_Dribbling',
    'skill_curve': 'Skill_Curve',
    'skill_fk_accuracy': 'Skill_FK_Accuracy',
    'skill_long_passing': 'Skill_Long_Passing',
    'skill_ball_control': 'Skill_Ball_Control',
    'movement_acceleration': 'Movement_Acceleration',
    'movement_sprint_speed': 'Movement_Sprint_Speed',
    'movement_agility': 'Movement_Agility',
    'movement_reactions': 'Movement_Reactions',
    'movement_balance': 'Movement_Balance',
    'power_shot_power': 'Power_Shot_Power',
    'power_jumping': 'Power_Jumping',
    'power_stamina': 'Power_Stamina',
    'power_strength': 'Power_Strength',
    'power_long_shots': 'Power_Long_Shots',
    'mentality_aggression': 'Mentality_Aggression',
    'mentality_interceptions': 'Mentality_Interceptions',
    'mentality_positioning': 'Mentality_Positioning',
    'mentality_vision': 'Mentality_Vision',
    'mentality_penalties': 'Mentality_Penalties',
    'mentality_composure': 'Mentality_Composure',
    'defending_marking': 'Defending_Marking',
    'defending_standing_tackle': 'Defending_Standing_Tackle',
    'defending_sliding_tackle': 'Defending_Sliding_Tackle',
    'goalkeeping_diving': 'Goalkeeping_Diving',
    'goalkeeping_handling': 'Goalkeeping_Handling',
    'goalkeeping_kicking': 'Goalkeeping_Kicking',
    'goalkeeping_positioning': 'Goalkeeping_Positioning',
    'goalkeeping_reflexes': 'Goalkeeping_Reflexes',
    'ls': 'LS',
    'st': 'ST',
    'rs': 'RS',
    'lw': 'LW',
    'lf': 'LF',
    'cf': 'CF',
    'rf': 'RF',
    'rw': 'RW',
    'lam': 'LAM',
    'cam': 'CAM',
    'ram': 'RAM',
    'lm': 'LM',
    'lcm': 'LCM',
    'cm': 'CM',
    'rcm': 'RCM',
    'rm': 'RM',
    'lwb': 'LWB',
    'ldm': 'LDM',
    'cdm': 'CDM',
    'rdm': 'RDM',
    'rwb': 'RWB',
    'lb': 'LB',
    'lcb': 'LCB',
    'cb': 'CB',
    'rcb': 'RCB',
    'rb': 'RB'
},inplace=True)


# In[13]:


data.columns


# In[14]:


# Define your 'fetch' function
def fetch(col):
    val = data[col].str.split('+').str.get(0)
    return val

# List of columns you want to apply the 'fetch' function to
columns_to_fetch = ['LS','ST','RS','LW','LF','CF','RF','RW','LAM','CAM','RAM','LM','LCM','CM','RCM','RM','LWB','LDM','CDM','RDM','RWB','LB','LCB','CB','RCB','RB']

# Apply 'fetch' function to each column and add the results as new columns
for col in columns_to_fetch:
    new_col_name = col   # Define a new column name
    data[new_col_name] = fetch(col)

# Display the updated DataFrame
data.head()


# In[15]:


data.isnull().sum()


# In[16]:


data.dtypes


# # **Replacing null values**

# ## Replacing null values for All
#  To replace the null values in a DataFrame with the median or mode value for each column, we can use the pandas library in Python.

# In[17]:


for column in data.columns:
    if data[column].dtype == ['float64','int64']:
        # Fill null values with the median for numeric columns
        median_value = data[column].median()
        data[column].fillna(median_value, inplace=True)
    else:
        # Fill null values with the mode for categorical columns
        mode_value = data[column].mode()[0]
        data[column].fillna(mode_value,inplace=True)


# In[18]:


data.isnull().sum()


# In[19]:


data.sample(10)


# # Check for Outliers

# In[20]:


num_data=data.select_dtypes(include=["int64","float64"]).columns


# In[21]:


num_data


# In[22]:


cat_data


# In[23]:


# Create a directory to store the box plots
output_directory = 'box_plots'
import os

if not os.path.exists(output_directory):
    os.makedirs(output_directory)

# Loop through all columns and create separate box plots
for column_name in data.columns:
    if data[column_name].dtypes in ['int64', 'float64']:
        plt.figure(figsize=(4, 4))  # Adjust the figure size as needed
        plt.boxplot(data[column_name], vert=False)
        plt.title(f'Box Plot for {column_name}')
        plt.xlabel('Value')
        plt.savefig(os.path.join(output_directory, f'{column_name}_box_plot.png'))
        plt.show()




# * In this datasets, we have so much Columns.so, It is not possible to Remove all outliers .
# * Then we have to Perform first Feature Engineering where we drop unwanted columns and form meanigful columns for futher process

# In[24]:


data.duplicated().sum()


# # **Data Preprocessing Report**:
# 
#  Creating a data preprocessing report involves documenting the steps taken to prepare the data for analysis, including the challenges encountered and how they were addressed. Here's a template for your data preprocessing report:
# 
#  **Step 1: Renaming Columns**
# 
# In this step, we renamed columns to make them more informative and user-friendly. This renaming was done using the rename method in pandas.
# 
# **Step 2: Handling Missing Values**
# 
# We checked for missing values in the dataset and found that there were missing values in some columns. To handle missing values, we used the following strategy:
# For numeric columns, we filled missing values with the median of the respective column.
# For categorical columns, we filled missing values with the mode (most frequent value) of the respective column.
# 
# **Step 3: Checking for Duplicates**
# 
# We checked for duplicate rows in the dataset and found that there were no duplicate rows.
# **Step 4: Feature Engineering**
# 
# In this step, we created new columns based on existing ones using the 'fetch' function for specific columns. These new columns were generated to extract relevant information and improve the dataset's usability.
# 
# **Step 5: Outlier Detection**
# 
# We identified numerical columns in the dataset and created box plots for each of them to visualize and detect potential outliers. The box plots were saved in the 'box_plots' directory for reference.
# 
# # **Challenges Faced**:
# 
# Handling missing values was a challenge, especially in columns with a mix of numeric and categorical data. Deciding whether to use median or mode required careful consideration.
# Managing a large number of columns and ensuring that each one was correctly transformed during the preprocessing phase was time-consuming.
# 
# # **Overcoming Challenges**:
# 
# We systematically applied median and mode imputation based on column data types, which helped in handling missing values effectively.
# We used a for loop to iterate through columns for outlier detection and automated the process to manage a large number of columns.
# 
# # **Conclusion**:
# 
# In this data preprocessing phase, we successfully addressed various data quality issues, such as renaming columns for clarity, handling missing values, and detecting outliers. These steps have improved the dataset's quality and made it more suitable for further analysis and modeling. The data is now ready for exploratory data analysis (EDA) and machine learning tasks.

# # **Exploratory Data analysis**

# In[25]:


# Names of all the columns.
for i in data.columns:
    print(i)


# In[26]:


data.shape


# ## **Which country has the most number of players ?**

# In[27]:


# Name of top countries and the number of players in each countries
data['Nationality'].value_counts()


# In[28]:


# Top 5 countries and number of players in each country.
data['Nationality'].value_counts()[0:5]


# In[29]:


# Top 5 countries having most number of players.
list(data['Nationality'].value_counts()[0:5].keys())


# In[30]:


# Number of the players in the top 5 countries having most number of players.
list(data['Nationality'].value_counts()[0:5])


# In[31]:


# Bar-plot of top 5 countries with most number of players.
plt.figure(figsize=(10,5))
plt.bar(list(data['Nationality'].value_counts()[0:5].keys()),list(data['Nationality'].value_counts()[0:5]),ec='black',lw=1)
plt.title("Most Players in the Country",fontsize=15)
plt.xlabel('Names of the Country',fontsize=13)
plt.ylabel('Number of Players',fontsize=13)
plt.show()


# ## **Which player has the highest salary ?**

# In[32]:


data.head()


# In[33]:


# Make a new dataset named player_salary of short_name and wage_eur columns.
player_salary=data[['Short_Name','Wage_EUR']]
player_salary.sample(15)


# In[34]:


# Head of the dataset.
player_salary.head()


# In[35]:


# Sort the dataset in the descending order of their salary.
player_salary=player_salary.sort_values(by='Wage_EUR',ascending=False)
player_salary


# In[36]:


# Top 5 records of the dataset.
player_salary.head()


# In[37]:


# Names of the top 5 players with highest salary.
list(player_salary['Short_Name'][0:5])


# In[38]:


# Top 5 highest salary.
list(player_salary['Wage_EUR'][0:5])


# In[39]:


# Bar-plot of top 5 players with highest salary.
plt.figure(figsize=(10,5))
sns.barplot(x=list(player_salary['Short_Name'][0:5]),y=list(player_salary['Wage_EUR'][0:5]))
plt.title("FIFA Salary",fontsize=15)
plt.xlabel("Name of the Players",fontsize=13)
plt.ylabel("Wage in eur",fontsize=13)
plt.show()


# # **What is the range of the salary of most of the players in the world ?**

# In[40]:


# wage_eur column of the dataset.
player_salary['Wage_EUR']


# In[41]:


# Histogram for the wage_eur column of the dataset.
plt.figure(figsize=(7,5))
plt.hist(player_salary['Wage_EUR'],bins=15,color='Blue')
plt.title("SALARY",fontsize=15)
plt.ylabel('Number of the Players',fontsize=13)
plt.xlabel('Salary of the Players',fontsize=13)
plt.show()


# In[42]:


# Dataset from player_salary where wage_eur is less than 50,000 .
player_salary[player_salary['Wage_EUR'] < 50000]


# In[43]:


# Percentage of the players who have salary less than 50,000 eur.
17688/18278*100


# ## **Who is the most tallest player in the world ?**

# In[44]:


data.head()


# In[45]:


# Make a new dataset named player_height of short_name and height_cm columns.
player_height=data[['Short_Name','Height_cm']]
player_height


# In[46]:


# Head of the dataset.
player_height.head()


# In[47]:


# Sort the dataset in the descending order of their height.
player_height=player_height.sort_values(by='Height_cm',ascending=False)
player_height


# In[48]:


# Top 5 records of the dataset.
player_height.head()


# In[49]:


# Names of the top 5 tallest players.
list(player_height['Short_Name'][0:5])


# In[50]:


# Bar-plot of top 5 tallest players.
plt.figure(figsize=(10,5))
sns.barplot(x=list(player_height['Short_Name'][0:5]),y=list(player_height['Height_cm'][0:5]))
plt.title("Tallest Player",fontsize=15)
plt.xlabel("Name of the Players",fontsize=13)
plt.ylabel("Height in cm",fontsize=13)
plt.show()


# ## **What is the range of the height of most of the players ?**

# In[51]:


# height_cm column of the dataset.
player_height['Height_cm']


# In[52]:


# Displot for the height_cm column of the dataset.
sns.displot(player_height["Height_cm"],color="Green",kde=True)
plt.title("HEIGHT",fontsize=15)
plt.ylabel('Number of the Players',fontsize=13)
plt.xlabel('Height of the Players',fontsize=13)
plt.show()


# ## **Who is the heaviest player in the world ?**

# In[53]:


# Make a new dataset named player_weight of short_name and weight_kg columns.
player_weight=data[['Short_Name','Weight_kg']]
player_weight


# In[54]:


# Head of the dataset.
player_weight.head()


# In[55]:


# Sort the dataset in the descending order of their weight.
player_weight=player_weight.sort_values(by='Weight_kg',ascending=False)
player_weight


# In[56]:


# Top 5 records of the dataset.
player_weight.head()


# In[57]:


#Names of the top 5 heaviest players.
list(player_weight['Short_Name'][0:5])


# In[58]:


# Weight of the top 5 heaviest players.
list(player_weight['Weight_kg'][0:5])


# In[59]:


# Bar-plot for top 5 heaviest players.
plt.barh(list(player_weight['Short_Name'][0:5]),list(player_weight['Weight_kg'][0:5]),ec='black',lw=1)
plt.title("Weight Of the Players",fontsize=15)
plt.xlabel('Weight in kg',fontsize=13)
plt.ylabel('Name of the Players',fontsize=13)
plt.show()


# # **Which Club has most number of the players ?**

# In[60]:


# Clubs names and the number of players in each of them.
data['Club'].value_counts()


# In[61]:


# Top 5 clubs who have the maximum number of players.
data['Club'].value_counts().index[0:5]


# In[62]:


#Count-plot of top 5 club who have the maximum number of players.
plt.figure(figsize=(11,5))
sns.countplot(y='Club',order=data['Club'].value_counts().index[0:5],data=data,palette = "Set2",ec='black',lw=1)
plt.title('Number of Players in the Club',fontsize=15)
plt.grid(True)
plt.show()


# ## **Which foot is most preferred by the players ?**

# In[63]:


data.head(3)


# In[64]:


# Name of the preferred foot and the number of players in each of them.
data['Preferred_Foot'].value_counts()


# In[65]:


# Count-plot for preferred_foot of the players.
plt.figure(figsize=(7,5))
sns.countplot(x='Preferred_Foot',order=data['Preferred_Foot'].value_counts().index[0:5],data=data,palette ="Set2",ec='black',lw=1)
plt.title('Preferred Foot',fontsize=15)
plt.show()


# # **what range of Iternational reputation does most of the players have ?**

# In[66]:


# Extract international_reputation columnn of the dataset.
data['International_Reputation']


# In[67]:


# Displot for the international_reputation column of the dataset.
sns.displot(data['International_Reputation'],kde=True)
plt.title("INTERNATIONAL REPUTATION",fontsize=15)
plt.ylabel('Number of the Players',fontsize=13)
plt.xlabel('International Reputation of the Players',fontsize=13)
plt.show()


# ## **Who is the best Dribbler in the world ?**

# In[68]:


data.head()


# In[69]:


# Create a dataFrame fifa_dribbling with short_name and dribbling columns.
fifa_dribbling=data[['Short_Name','Dribbling']]
fifa_dribbling


# In[70]:


# Sort the dataset in descending order of the dribbling.
fifa_dribbling_1=fifa_dribbling.sort_values(by='Dribbling',ascending=False)
fifa_dribbling_1


# In[71]:


# Top 5 records of the dataset.
fifa_dribbling_1[0:5]


# In[72]:


# Names of top 5 dribblers.
x=list(fifa_dribbling_1[0:5][0:5]['Short_Name'])
x


# In[73]:


# point of the top 5 dribblers.
y=list(fifa_dribbling_1[0:5][0:5]['Dribbling'])
y


# In[74]:


# Bar-plot of top 5 dribblers.
plt.figure(figsize=(10,5))
plt.bar(x,y,ec='black',lw=1)
plt.title("DRIBBLING",fontsize=15)
plt.xlabel('Name of the players',fontsize=13)
plt.ylabel('Points of Player',fontsize=13)
plt.show()


# ## **Who is the best shooter in the world ?**

# In[75]:


# Create a dataFrame fifa_shooting with short_name and shooting columns.
fifa_shooting=data[['Short_Name','Shooting']]
fifa_shooting


# In[76]:


# Sort the dataset in descending order of the shooting.
fifa_shooting_1=fifa_shooting.sort_values(by="Shooting",ascending=False)
fifa_shooting_1


# In[77]:


# Top 5 records of the dataset.
fifa_shooting_1[0:5]


# In[78]:


# Names of top 5 Shooters.
x=list(fifa_shooting_1[0:5][0:5]['Short_Name'])
x


# In[79]:


# point of the top 5 shooters.
y=list(fifa_shooting_1[0:5][0:5]['Shooting'])
y


# In[80]:


# Bar-plot of top 5 shooters.
plt.figure(figsize=(10,5))
plt.bar(x,y,ec='black',lw=1)
plt.title("SHOOTING",fontsize=15)
plt.xlabel('Name of the players',fontsize=13)
plt.ylabel('Points of Player',fontsize=13)
plt.show()


# ## **Who is the best defender in the world ?**

# In[81]:


# Create a dataFrame fifa_defender with short_name and defending columns.
fifa_defending=data[['Short_Name','Defending']]
fifa_defending


# In[82]:


# Sort the dataset in descending order of the defending.
fifa_defending_1=fifa_defending.sort_values(by="Defending",ascending=False)
fifa_defending_1


# In[83]:


# Top 5 records of the dataset.
fifa_defending_1[0:5]


# In[84]:


# Names of top 5 defenders.
x=list(fifa_defending_1[0:5][0:5]['Short_Name'])
x


# In[85]:


# point of the top 5 defender.
y=list(fifa_defending_1[0:5][0:5]['Defending'])
y


# In[86]:


# Bar-plot of top 5 shooters.
plt.figure(figsize=(10,5))
plt.bar(x,y,ec='black',lw=1)
plt.title("DEFENDING",fontsize=15)
plt.xlabel('Name of the players',fontsize=13)
plt.ylabel('Points of Player',fontsize=13)
plt.show()


# ## **Which goalkeeper has the best reflexes in the world ?**

# In[87]:


data.head(3)


# In[88]:


# Create a dataFrame fifa_gk_reflexes with short_name and gk_reflexes columns.
fifa_gk_reflexes=data[['Short_Name','GK_Reflexes']]
fifa_gk_reflexes


# In[89]:


# Sort the dataset in descending order of the gk_reflexes.
fifa_gk_reflexes_1=fifa_gk_reflexes.sort_values(by="GK_Reflexes",ascending=False)
fifa_gk_reflexes_1


# In[90]:


# Names of top 5 goalkeepers with best reflexes.
x=list(fifa_gk_reflexes_1[0:5][0:5]['Short_Name'])
x


# In[91]:


# point of the top 5 goalkeepers with best reflexes .
y=list(fifa_gk_reflexes_1[0:5][0:5]['GK_Reflexes'])
y


# In[92]:


# Bar-plot of top 5 goalkeepers with best reflexes.
plt.figure(figsize=(10,5))
plt.bar(x,y,ec='black',lw=1)
plt.title("GOALKEEPER REFLEXEX",fontsize=15)
plt.xlabel('Name of the players',fontsize=13)
plt.ylabel('Points of Player',fontsize=13)
plt.show()


# ## **SUMMARY**:
# * England has the most number of players.
# * L. Messi has the highest salary in the world.
# * 97% of the players in the world have salary below than 50,000 eur.
# * T. Holý is the tallest player in the world.
# * Most of the players in the world have height between 175-185 cm.
# * A. Akinfenwa is the heaviest player in the world.
# * Most of the players in the world have weight between 70-80 kg.
# * FC Barcelona is one of the club in the world who have the maximum number of players.
# * 76% players preferred right foot as compared to left foot.
# * Most of the players have 1 international reputation out of 5.
# * L. Messi is the best dribbler in the world.
# * Cristiano Ronaldo is the best shooter in the world.
# * G. Chiellini is the best defender in the world.
# * De Gea has the best reflexes in the world.

# # **Feature Engineering**

# ## **Drop Unwanted Columns**

# In[93]:


pd.set_option('display.max_rows',None)
pd.set_option('display.max_columns',None)


# In[94]:


data.head(2)


# In[95]:


data.drop(['Player_URL','Player_ID','Full_Name','Date_of_Birth','Player_Tags','Player_Traits'],1,inplace=True)


# In[96]:


data.head()


# ## **Adding new column 'Overall_positinal_skill'**

# In[97]:


data['Overall_positional_skill'] = data[['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW']].mean(axis=1)


# In[98]:


pd.set_option('display.float_format', '{:.2f}'.format)


# In[99]:


data.head(3)


# In[100]:


data.drop(['LS', 'ST', 'RS', 'LW', 'LF', 'CF', 'RF', 'RW'],1,inplace=True)


# In[101]:


data.head()


# ## **Preferred_Foot**
# 
# * with the help of Label encoder we have to Left-0 and right-1

# ### **Label Encoder**

# In[102]:


from sklearn.preprocessing import LabelEncoder


# In[103]:


# Initialize the LabelEncoder
label_encoder = LabelEncoder()


# In[104]:


# Fit and transform the 'Preferred_Foot' column
data['Preferred_Foot'] = label_encoder.fit_transform(data['Preferred_Foot'])


# In[105]:


data.head()


# ## **Work_Rate**

# In[106]:


# Create a mapping of WorkRate to numeric values
workrate_mapping = {'low': 0, 'medium': 0.5, 'high': 1}


# In[107]:


# Apply the mapping to the 'WorkRate' column
data['AttackWorkRate'] = data['Work_Rate'].map(workrate_mapping)
data['DefenseWorkRate'] = data['Work_Rate'].map(workrate_mapping)


# In[108]:


# Initialize the LabelEncoder
label_encoder = LabelEncoder()

# Encode the 'WorkRate' column (optional if you don't need it after splitting)
data['Work_Rate'] = label_encoder.fit_transform(data['Work_Rate'])


# In[109]:


data.sample(5)


# In[110]:


data.drop(['AttackWorkRate', 'DefenseWorkRate', 'International_Reputation','Real_Face','Joined','Contract_Valid_Until','Body_Type'],1,inplace=True)


# In[111]:


data.head()


# ## **Adding BMI column**

# In[112]:


#adding new column BMI to check the health and fitness of players
data["BMI"] = data['Weight_kg'] / (data['Height_cm'] / 100) ** 2


# In[113]:


data.head()


# In[114]:


# Now drop Height and weight column
data.drop(['Height_cm','Weight_kg'],1,inplace=True)


# In[115]:


data.head()


# In[116]:


# # Create categorical variables for different player positions with drop_first=True
# data = pd.get_dummies(data, columns=['Player_Positions'], prefix='Position', drop_first=True)


# In[117]:


data.head()


# In[118]:


# data.drop(['Team_Position'],1,inplace=True)


# In[119]:


data.head()


# In[120]:


data.drop(['Team_Jersey_Number','Nation_Jersey_Number','Nation_Position'],1,inplace=True)


# In[121]:


data.head()


# ## **Adding PhysicalProwess as new Column**

# In[122]:


# Select the physical attribute columns
physical_attributes = ['Power_Strength', 'Power_Shot_Power', 'Movement_Agility', 'Power_Stamina', 'Power_Jumping', 'Movement_Acceleration', 'Movement_Balance','Movement_Reactions', 'Movement_Sprint_Speed', 'Power_Long_Shots']

# Calculate the average physical prowess for each player
data['PhysicalProwess'] = data[physical_attributes].mean(axis=1)


# In[123]:


data.drop(['Power_Strength', 'Power_Shot_Power', 'Movement_Agility', 'Power_Stamina', 'Power_Jumping', 'Movement_Acceleration', 'Movement_Balance','Movement_Reactions', 'Movement_Sprint_Speed', 'Power_Long_Shots'],1,inplace=True)


# In[124]:


data.head()


# ## **Adding 'GK_Overall' column**

# In[125]:


# Define weights for each goalkeeper attribute
weights = {'GK_Diving': 0.2, 'GK_Handling': 0.2, 'GK_Kicking': 0.1, 'GK_Reflexes': 0.2, 'GK_Speed': 0.1, 'GK_Positioning': 0.2}

# Calculate the overall goalkeeper skill using the weighted average
data['GK_Overall'] = data[['GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes', 'GK_Speed', 'GK_Positioning']].dot(pd.Series(weights))

# Now you have a new feature 'GK_Overall' representing the overall goalkeeper skill


# In[126]:


data.head()


# In[127]:


data.drop(columns=['GK_Diving', 'GK_Handling', 'GK_Kicking', 'GK_Reflexes', 'GK_Speed', 'GK_Positioning'], inplace=True)


# ## **Adding TechnicalSkills as a new column**

# In[128]:


# Select the technical attribute columns
technical_attributes = ['Dribbling', 'Pace', 'Shooting', 'Physic', 'Passing', 'Defending']

# Calculate the average technical skills for each player
data['TechnicalSkills'] = data[technical_attributes].mean(axis=1)


# In[129]:


# drop extasting columns
data.drop(['Dribbling', 'Pace', 'Shooting', 'Physic', 'Passing', 'Defending'],1,inplace=True)


# In[130]:


data.head()


# ## **Adding 'Positional_Skills_Aggregate' as a New Column**

# In[131]:


# Calculate the mean (or sum) of position-specific attributes for each player
data['Positional_Skills_Aggregate'] = data[[
    'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM',
    'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'
]].mean(axis=1)

# You can also use 'sum' instead of 'mean' to create a different aggregate feature
# fifa_df['Positional_Skills_Aggregate'] = fifa_df[[
#     'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM',
#     'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'
# ]].sum(axis=1)

# Drop the individual position-specific attributes if you no longer need them
data.drop(columns=[
    'LAM', 'CAM', 'RAM', 'LM', 'LCM', 'CM', 'RCM', 'RM',
    'LWB', 'LDM', 'CDM', 'RDM', 'RWB', 'LB', 'LCB', 'CB', 'RCB', 'RB'
], inplace=True)


# ## **Adding Skill_Aggregate as a new column**

# In[132]:


data['Skill_Aggregate'] = data[[
    'Skill_Dribbling', 'Skill_Curve', 'Skill_FK_Accuracy', 'Skill_Long_Passing', 'Skill_Ball_Control'
]].mean(axis=1)


# Drop the individual skill-related attributes
data.drop(columns=[
    'Skill_Dribbling', 'Skill_Curve', 'Skill_FK_Accuracy', 'Skill_Long_Passing', 'Skill_Ball_Control'
], inplace=True)


# ## **Adding Mentality_Aggregate as a new Feature**

# In[133]:


# Calculate the mean of mentality-related attributes for each player
data['Mentality_Aggregate'] = data[[
    'Mentality_Aggression', 'Mentality_Interceptions', 'Mentality_Positioning',
    'Mentality_Vision', 'Mentality_Penalties', 'Mentality_Composure'
]].mean(axis=1)


# Drop the individual mentality-related attributes
data.drop(columns=[
    'Mentality_Aggression', 'Mentality_Interceptions', 'Mentality_Positioning',
    'Mentality_Vision', 'Mentality_Penalties', 'Mentality_Composure'
], inplace=True)


# ## **Adding Goalkeeping_Skills_Aggregate As a new Column**

# In[134]:


# Calculate the mean of goalkeeper-specific attributes for each player
data['Goalkeeping_Skills_Aggregate'] = data[[
    'Goalkeeping_Diving', 'Goalkeeping_Handling', 'Goalkeeping_Kicking',
    'Goalkeeping_Positioning', 'Goalkeeping_Reflexes'
]].mean(axis=1)


# Drop the individual goalkeeper-specific attributes
data.drop(columns=[
    'Goalkeeping_Diving', 'Goalkeeping_Handling', 'Goalkeeping_Kicking',
    'Goalkeeping_Positioning', 'Goalkeeping_Reflexes'
], inplace=True)


# In[135]:


data.head()


# ## **Adding 'Attacking_Skills_Aggregate' as a New Feature**

# In[136]:


# Calculate the mean of attacking-related attributes for each player
data['Attacking_Skills_Aggregate'] = data[[
    'Attacking_Crossing', 'Attacking_Finishing', 'Attacking_Heading_Accuracy',
    'Attacking_Short_Passing', 'Attacking_Volleys'
]].mean(axis=1)


# Drop the individual attacking-related attributes
data.drop(columns=[
    'Attacking_Crossing', 'Attacking_Finishing', 'Attacking_Heading_Accuracy',
    'Attacking_Short_Passing', 'Attacking_Volleys'
], inplace=True)


# In[137]:


data.head()


# ### **Adding Defending_Skills_Aggregate As a New Column**

# In[138]:


# Calculate the mean of defending-related attributes for each player
data['Defending_Skills_Aggregate'] = data[[
    'Defending_Marking', 'Defending_Standing_Tackle', 'Defending_Sliding_Tackle'
]].mean(axis=1)


# Drop the individual defending-related attributes
data.drop(columns=['Defending_Marking', 'Defending_Standing_Tackle', 'Defending_Sliding_Tackle'], inplace=True)


# In[139]:


data.head()


# In[140]:


# Define a mapping dictionary to assign numerical codes to categories
foot_skills_mapping = {
    ('Right', 4): 1,   # StrongRight
    ('Left', 4): 2,    # StrongLeft
    ('Right', 1): 3,   # BothWeak
    ('Left', 1): 3,    # BothWeak
}

# Create a function to apply the mapping and assign numerical codes
def map_foot_skills(row):
    return foot_skills_mapping.get((row['Preferred_Foot'], row['Weak_Foot']), 0)  # Default to 0 for 'Other'

# Apply the mapping function to create the 'FootSkills' feature with numerical codes
data['FootSkills'] = data.apply(map_foot_skills, axis=1)

# Optionally, drop the original 'PreferredFoot' and 'WeakFoot' features
data.drop(columns=['Preferred_Foot', 'Weak_Foot'], inplace=True)


# In[141]:


data.head()


# ## **Outliers removal**

# In[142]:


num_data1=data.select_dtypes(include=["int64","float64"]).columns
num_data


# In[143]:


# Box plot for outlier detection
plt.figure(figsize=(10,5),facecolor="white")
plotnumber=1

for column in num_data1:
  if plotnumber<17:
    ax=plt.subplot(4,4,plotnumber)
    sns.boxplot(x=data[column])
    plt.xlabel(column,fontsize=10)
    plt.ylabel("Overall_Rating",fontsize=10)
  plotnumber+=1
plt.tight_layout()


# In[144]:


#Age
sns.histplot(data=data,x='Age',kde=True)


# we use IQR methode for handling the outliers because in the above graph we dont have normal distribution.

# In[145]:


Q1=data["Age"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Age"].quantile(0.75)
print("upper_quartile",Q3)


# In[146]:


IQR=Q3-Q1
IQR


# In[147]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[148]:


len(data.loc[data["Age"]>upper_limit])/len(data)


# In[149]:


data.loc[data["Age"]>upper_limit]


# In[150]:


data.loc[data["Age"]>upper_limit,"Age"]=data["Age"].median()


# In[151]:


sns.boxplot(x=data.Age)


# In[152]:


# Overall rating
sns.histplot(data=data,x='Overall_Rating',kde=True)


# In[153]:


Q1=data["Overall_Rating"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Overall_Rating"].quantile(0.75)
print("upper_quartile",Q3)


# In[154]:


IQR=Q3-Q1
IQR


# In[155]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[156]:


len(data.loc[data["Overall_Rating"]>upper_limit])/len(data)


# In[157]:


data.loc[data["Overall_Rating"]>upper_limit,"Overall_Rating"]=data["Overall_Rating"].median()


# In[158]:


len(data.loc[data["Overall_Rating"]<lower_limit])/len(data)


# In[159]:


data.loc[data["Overall_Rating"]<lower_limit,"Overall_Rating"]=data["Overall_Rating"].median()


# In[160]:


sns.boxplot(x=data.Overall_Rating)


# In[161]:


# For Potential Rating
sns.histplot(data=data,x='Potential_Rating',kde=True)


# In[162]:


import scipy.stats as stats
# Calculate skewness and kurtosis
skewness = stats.skew(data['Potential_Rating'])
kurtosis = stats.kurtosis(data['Potential_Rating'])

# Perform Shapiro-Wilk test
shapiro_test = stats.shapiro(data['Potential_Rating'])
p_value = shapiro_test[1]

print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")
print(f"Shapiro-Wilk p-value: {p_value}")

# Check if the p-value is less than a significance level (e.g., 0.05) for normality
if p_value < 0.05:
    print(f"{'Potential_Rating'} is likely not normally distributed.")
else:
    print(f"{'Potential_Rating'} appears to be normally distributed.")


# In[163]:


Q1=data["Potential_Rating"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Potential_Rating"].quantile(0.75)
print("upper_quartile",Q3)


# In[164]:


IQR=Q3-Q1
IQR


# In[165]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[166]:


len(data.loc[data["Potential_Rating"]>upper_limit])/len(data)


# In[167]:


data.loc[data["Potential_Rating"]>upper_limit,"Potential_Rating"]=data["Potential_Rating"].median()


# In[168]:


len(data.loc[data["Potential_Rating"]<lower_limit])/len(data)


# In[169]:


data.loc[data["Potential_Rating"]<lower_limit,"Potential_Rating"]=data["Potential_Rating"].median()


# In[170]:


sns.boxplot(x=data.Potential_Rating)


# In[171]:


## value_EUR
sns.histplot(data=data,x='Value_EUR',kde=True)


# In[172]:


Q1=data["Value_EUR"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Value_EUR"].quantile(0.75)
print("upper_quartile",Q3)


# In[173]:


IQR=Q3-Q1
IQR


# In[174]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[175]:


data.loc[data["Value_EUR"]>upper_limit]


# In[176]:


len(data.loc[data["Value_EUR"]>upper_limit])/len(data)


# In[177]:


data.loc[data["Value_EUR"]>upper_limit,"Value_EUR"]=data["Value_EUR"].median()


# In[178]:


sns.boxplot(x=data.Value_EUR)


# In[179]:


# Wage_EUR
sns.histplot(data=data,x='Wage_EUR',kde=True)


# In[180]:


Q1=data["Wage_EUR"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Wage_EUR"].quantile(0.75)
print("upper_quartile",Q3)


# In[181]:


IQR=Q3-Q1
IQR


# In[182]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[183]:


data.loc[data["Wage_EUR"]>upper_limit]


# In[184]:


len(data.loc[data["Wage_EUR"]>upper_limit])/len(data)


# In[185]:


data.loc[data["Wage_EUR"]>upper_limit,"Wage_EUR"]=data["Wage_EUR"].median()


# In[186]:


sns.boxplot(x=data.Wage_EUR)


# In[187]:


# Skill moves
sns.histplot(data=data,x='Skill_Moves',kde=True)


# In[188]:


Q1=data["Skill_Moves"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Skill_Moves"].quantile(0.75)
print("upper_quartile",Q3)


# In[189]:


IQR=Q3-Q1
IQR


# In[190]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[191]:


data.loc[data["Skill_Moves"]>upper_limit]


# In[192]:


len(data.loc[data["Skill_Moves"]>upper_limit])/len(data)


# In[193]:


data.loc[data["Skill_Moves"]>upper_limit,"Skill_Moves"]=data["Skill_Moves"].median()


# In[194]:


sns.boxplot(x=data.Skill_Moves)


# In[195]:


# Release_Clause_EUR
sns.histplot(data=data,x='Release_Clause_EUR',kde=True)


# In[196]:


Q1=data["Release_Clause_EUR"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Release_Clause_EUR"].quantile(0.75)
print("upper_quartile",Q3)


# In[197]:


IQR=Q3-Q1
IQR


# In[198]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[199]:


data.loc[data["Release_Clause_EUR"]>upper_limit]


# In[200]:


len(data.loc[data["Release_Clause_EUR"]>upper_limit])/len(data)


# In[201]:


data.loc[data["Release_Clause_EUR"]>upper_limit,"Release_Clause_EUR"]=data["Release_Clause_EUR"].median()


# In[202]:


sns.boxplot(x=data.Release_Clause_EUR)


# In[203]:


data.head()


# In[204]:


# Overall_Positional_skill
sns.histplot(data=data,x='Overall_positional_skill',kde=True)


# In[205]:


import scipy.stats as stats
# Calculate skewness and kurtosis
skewness = stats.skew(data['Overall_positional_skill'])
kurtosis = stats.kurtosis(data['Overall_positional_skill'])

# Perform Shapiro-Wilk test
shapiro_test = stats.shapiro(data['Overall_positional_skill'])
p_value = shapiro_test[1]

print(f"Skewness: {skewness}")
print(f"Kurtosis: {kurtosis}")
print(f"Shapiro-Wilk p-value: {p_value}")

# Check if the p-value is less than a significance level (e.g., 0.05) for normality
if p_value < 0.05:
    print(f"{'Overall_positional_skill'} is likely not normally distributed.")
else:
    print(f"{'Overall_positional_skill'} appears to be normally distributed.")


# In[206]:


Q1=data["Overall_positional_skill"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Overall_positional_skill"].quantile(0.75)
print("upper_quartile",Q3)


# In[207]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[208]:


IQR=Q3-Q1
IQR


# In[209]:


data.loc[data["Overall_positional_skill"]>upper_limit]


# In[210]:


len(data.loc[data["Overall_positional_skill"]>upper_limit])/len(data)


# In[211]:


data.loc[data["Overall_positional_skill"]>upper_limit,"Overall_positional_skill"]=data["Overall_positional_skill"].median()


# In[212]:


len(data.loc[data["Overall_positional_skill"]<lower_limit])/len(data)


# In[213]:


data.loc[data["Overall_positional_skill"]<lower_limit,"Overall_positional_skill"]=data["Overall_positional_skill"].median()


# In[214]:


sns.boxplot(x=data.Overall_positional_skill)


# In[215]:


# BMI
sns.histplot(data=data,x='BMI',kde=True)


# In[216]:


Q1=data["BMI"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["BMI"].quantile(0.75)
print("upper_quartile",Q3)


# In[217]:


IQR=Q3-Q1
IQR


# In[218]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[219]:


data.loc[data["BMI"]>upper_limit]


# In[220]:


len(data.loc[data["BMI"]>upper_limit])/len(data)


# In[221]:


data.loc[data["BMI"]>upper_limit,"BMI"]=data["BMI"].median()


# In[222]:


len(data.loc[data["BMI"]<lower_limit])/len(data)


# In[223]:


data.loc[data["BMI"]<lower_limit,"BMI"]=data["BMI"].median()


# In[224]:


sns.boxplot(x=data.BMI)


# In[225]:


# PhysicalProwess
sns.histplot(data=data,x='PhysicalProwess',kde=True)


# In[226]:


Q1=data["PhysicalProwess"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["PhysicalProwess"].quantile(0.75)
print("upper_quartile",Q3)


# In[227]:


IQR=Q3-Q1
IQR


# In[228]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[229]:


data.loc[data["PhysicalProwess"]<lower_limit]


# In[230]:


len(data.loc[data["PhysicalProwess"]<lower_limit])/len(data)


# In[231]:


data.loc[data["PhysicalProwess"]<lower_limit,"PhysicalProwess"]=data["PhysicalProwess"].median()


# In[232]:


len(data.loc[data["PhysicalProwess"]>upper_limit])/len(data)


# In[233]:


data.loc[data["PhysicalProwess"]>upper_limit,"PhysicalProwess"]=data["PhysicalProwess"].median()


# In[234]:


sns.boxplot(x=data.PhysicalProwess)


# In[235]:


# GK_Overall
sns.histplot(data=data,x='GK_Overall',kde=True)


# In[236]:


Q1=data["GK_Overall"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["GK_Overall"].quantile(0.75)
print("upper_quartile",Q3)


# In[237]:


IQR=Q3-Q1
IQR


# In[238]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[239]:


data.loc[data["GK_Overall"]>upper_limit]


# In[240]:


len(data.loc[data["GK_Overall"]>upper_limit])/len(data)


# In[241]:


data.loc[data["GK_Overall"]>upper_limit,"GK_Overall"]=data["GK_Overall"].median()


# In[242]:


len(data.loc[data["GK_Overall"]<lower_limit])/len(data)


# In[243]:


data.loc[data["GK_Overall"]<lower_limit,"GK_Overall"]=data["GK_Overall"].median()


# In[244]:


sns.boxplot(x=data.GK_Overall)


# In[245]:


# TechnicalSkills
sns.histplot(data=data,x='TechnicalSkills',kde=True)


# In[246]:


Q1=data["TechnicalSkills"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["TechnicalSkills"].quantile(0.75)
print("upper_quartile",Q3)


# In[247]:


IQR=Q3-Q1
IQR


# In[248]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[249]:


data.loc[data["TechnicalSkills"]>upper_limit]


# In[250]:


len(data.loc[data["TechnicalSkills"]>upper_limit])/len(data)


# In[251]:


data.loc[data["TechnicalSkills"]>upper_limit,"TechnicalSkills"]=data["TechnicalSkills"].median()


# In[252]:


len(data.loc[data["TechnicalSkills"]<lower_limit])/len(data)


# In[253]:


data.loc[data["TechnicalSkills"]<lower_limit,"TechnicalSkills"]=data["TechnicalSkills"].median()


# In[254]:


sns.boxplot(x=data.TechnicalSkills)


# In[255]:


# positinal skill Agreagate
sns.histplot(data=data,x='Positional_Skills_Aggregate',kde=True)


# In[256]:


Q1=data["Positional_Skills_Aggregate"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Positional_Skills_Aggregate"].quantile(0.75)
print("upper_quartile",Q3)


# In[257]:


IQR=Q3-Q1
IQR


# In[258]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[259]:


len(data.loc[data["Positional_Skills_Aggregate"]>upper_limit])/len(data)


# In[260]:


data.loc[data["Positional_Skills_Aggregate"]>upper_limit]


# In[261]:


data.loc[data["Positional_Skills_Aggregate"]>upper_limit,"Positional_Skills_Aggregate"]=data["Positional_Skills_Aggregate"].median()


# In[262]:


data.loc[data["Positional_Skills_Aggregate"]<lower_limit]


# In[263]:


data.loc[data["Positional_Skills_Aggregate"]<lower_limit,"Positional_Skills_Aggregate"]=data["Positional_Skills_Aggregate"].median()


# In[264]:


sns.boxplot(x=data.Positional_Skills_Aggregate)


# In[265]:


# Skill_Aggregate
sns.histplot(data=data,x='Skill_Aggregate',kde=True)


# In[266]:


Q1=data["Skill_Aggregate"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Skill_Aggregate"].quantile(0.75)
print("upper_quartile",Q3)


# In[267]:


IQR=Q3-Q1
IQR


# In[268]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[269]:


len(data.loc[data["Skill_Aggregate"]>upper_limit])/len(data)


# In[270]:


data.loc[data["Skill_Aggregate"]>upper_limit]


# In[271]:


data.loc[data["Skill_Aggregate"]>upper_limit,"Skill_Aggregate"]=data["Skill_Aggregate"].median()


# In[272]:


sns.boxplot(x=data.Age)


# In[273]:


# Mentality_Aggregate
sns.histplot(data=data,x='Mentality_Aggregate',kde=True)


# In[274]:


Q1=data["Mentality_Aggregate"].quantile(0.25)
print("lower_quartile",Q1)
Q3=data["Mentality_Aggregate"].quantile(0.75)
print("upper_quartile",Q3)


# In[275]:


IQR=Q3-Q1
IQR


# In[276]:


lower_limit=Q1-1.5*IQR
print("lower_limit is",lower_limit)
upper_limit=Q3+1.5*IQR
print("upper_limit is",upper_limit)


# In[277]:


len(data.loc[data["Mentality_Aggregate"]>upper_limit])/len(data)


# In[278]:


data.loc[data["Mentality_Aggregate"]>upper_limit]


# In[279]:


data.loc[data["Mentality_Aggregate"]>upper_limit,"Mentality_Aggregate"]=data["Mentality_Aggregate"].median()


# In[280]:


len(data.loc[data["Mentality_Aggregate"]<lower_limit])/len(data)


# In[281]:


data.loc[data["Mentality_Aggregate"]<lower_limit,"Mentality_Aggregate"]=data["Mentality_Aggregate"].median()


# In[282]:


sns.boxplot(x=data.Mentality_Aggregate)


# # **Feature Selection**

# In[283]:


corr=data.corr()


# In[284]:


plt.figure(figsize=(30,30))
sns.heatmap(data.corr(),annot=True,cmap=plt.cm.RdYlGn)
plt.show()


# In[285]:


# with the following function we can select highly correlated features
# it will remove the first feature that is correlated with anything other feature

def correlation(dataset, threshold):
    col_corr = set()  # Set of all the names of correlated columns
    corr_matrix = dataset.corr()
    for i in range(len(corr_matrix.columns)):
        for j in range(i):
            if (corr_matrix.iloc[i, j]) > threshold: # we are interested in absolute coeff value
                colname = corr_matrix.columns[i]  # getting the name of column
                col_corr.add(colname)
    return col_corr


# In[286]:


corr_features = correlation(data, 0.7)
len(set(corr_features))


# In[287]:


corr_features


# In[288]:


data.drop(columns=corr_features, inplace=True)


# In[289]:


data.head()


# ## **Feature Scaling**

# In[290]:


data.drop(['Short_Name', 'Nationality', 'Club','Player_Positions', 'Team_Position', 'Loaned_From'],1,inplace=True)


# In[291]:


from sklearn.preprocessing import StandardScaler


# In[292]:


# Select the features you want to scale (exclude non-numeric and target columns)
features_to_scale = data.select_dtypes(include=['float64', 'int64']).drop(columns=['Overall_Rating'])

# Initialize the StandardScaler
scaler = StandardScaler()

# Fit and transform the selected features
scaled_features = scaler.fit_transform(features_to_scale)

# Replace the original features with the scaled features
data[features_to_scale.columns] = scaled_features


# In[293]:


data.head()


# In[294]:


data.shape


# In[295]:


features = data.select_dtypes(include=['float64', 'int64']).drop(columns=['Overall_Rating'])


# #**Feature Engineering Report:**
# 
# ## **Dataset Overview:**
# 
# The dataset under consideration is related to football players and contains various attributes related to their skills, attributes, and characteristics. Here is a brief overview of the dataset:
# 
# ##**Attributes:**
# 
# The dataset includes attributes such as "Age," "Overall_Rating," "Potential_Rating," "Value_EUR," "Wage_EUR," "Skill_Moves," "Work_Rate," and several others, including some aggregated skill-related features.
# 
# ## **Feature Encoding:**
# 
# **Categorical Features:**
# 
# Player_Positions: This feature contains information about the player's positions on the field. It was initially encoded as a comma-separated string, indicating multiple positions. To handle this, we can perform one-hot encoding, creating binary columns for each unique position. This will transform categorical data into a format suitable for machine learning algorithms.
# 
# **Nationality:**
# 
# The "Nationality" feature represents the nationality of the player. We can apply one-hot encoding to convert this categorical variable into binary columns, each representing a different nationality.
# 
# **Club:**
# 
# Similar to "Nationality," the "Club" feature can also be one-hot encoded to represent the clubs the players belong to.
# 
# **Text Features:**
# 
# **Short_Name:**
# 
# This feature contains the short names of the players. While it may not be directly useful for modeling, it could potentially be used for natural language processing tasks, such as sentiment analysis of player names.
# 
# **Data Splitting:**
# 
# Data splitting is a crucial step in preparing the dataset for machine learning. The dataset should be divided into training and testing sets to evaluate model performance. Common splitting ratios are 70/30 or 80/20 for training/testing. However, the specific split ratio depends on the dataset's size and characteristics.
# 
# ## **Feature Selection:**
# 
# Feature selection is essential to identify the most relevant and informative features for building machine learning models. In your preprocessing steps, you already performed some initial feature selection by removing highly correlated features. Further feature selection methods can be applied, such as:
# 
# Recursive Feature Elimination (RFE): This method recursively removes the least important features based on their contribution to model performance.
# 
# Feature Importance from Tree-based Models: You can use algorithms like Random Forest or Gradient Boosting to assess feature importance and select the top-ranking features.
# 
# Principal Component Analysis (PCA): PCA can be applied to reduce dimensionality while preserving as much variance as possible.
# 
# Domain Knowledge: Leveraging domain knowledge, you can manually select features that are known to be important in the context of football player analysis.
# 
# ##**Challenges Faced:**
# **Feature Encoding Challenges:**
# 
# One-hot encoding of categorical features like "Player_Positions," "Nationality," and "Club" can lead to a significant increase in the number of features, potentially causing dimensionality issues.
# 
# **Data Splitting Challenges:**
# 
# Ensuring that the split maintains the distribution of target variables, especially if there's class imbalance, is crucial.
# Feature Selection Challenges:
# Determining the optimal number of features to include in the final dataset can be challenging. Too few features may result in loss of information, while too many features can lead to overfitting.
# 
# Handling highly imbalanced features or rare categorical values during feature selection can be tricky.
# 
# Identifying and dealing with multicollinearity (correlation between features) is another challenge when selecting the most relevant features.
# 
# **Conclusion:**
# 
# In this feature engineering report, we've outlined the key steps taken to prepare the dataset for machine learning analysis. Feature encoding, data splitting, and feature selection are crucial aspects of this process. Challenges related to each step have been highlighted, and it's important to carefully address them to ensure the quality and effectiveness of the machine learning models built using this dataset.

# #**Task 2:- Explore football skills and cluster football players based on their attributes**

# # **Cluster football players based on their attributes**

# In[296]:


features.head()


# # **Principal Component Analysis (PCA)**

# In[298]:


# Step:1 Getting optimal value of pca
from sklearn.decomposition import PCA
pca = PCA() # Object creation
principlecomponents = pca.fit_transform(features) # Fitting the data
plt.figure(figsize=(10,7))
sns.set_style('darkgrid')
plt.plot(np.cumsum(pca.explained_variance_ratio_),marker='*',color='k') #plot the variance ratio
plt.xlabel('Number of components',fontsize=20)
plt.ylabel('Variance(%)',fontsize=20) # for each componant
plt.title('Explained Variance',fontsize=20)
plt.show()


# In[299]:


# Step:2 Select the components
pca = PCA(n_components=3)
fifa = pca.fit_transform(data)

# Step:3 Make new dataframe
principle_df = pd.DataFrame(data=fifa,columns=['pca1','pca2','pca3'])
principle_df.head()


# #** PCA used for Clustering Football Players:**
# 
# Using Principal Component Analysis (PCA) to cluster football players based on their attributes is a common technique in data analysis and dimensionality reduction. Here's a report on why and how PCA is used for this task and a conclusion summarizing its benefits:
# 
# ## **1. Dataset Overview:**
# 
# The dataset contains various attributes of football players, including age, potential rating, value in euros, wage in euros, skill moves, work rate, overall positional skill, BMI, physical prowess, GK overall, goalkeeping skills aggregate, defending skills aggregate, and foot skills.
# 
# ## **2. Purpose of Using PCA:**
# 
# The primary goal of applying PCA to this dataset is to reduce its dimensionality while retaining as much valuable information as possible.
# Dimensionality reduction is essential for clustering, visualization, and simplifying subsequent analyses.
# PCA transforms the original features into linearly uncorrelated variables called principal components, which can reveal hidden structures and patterns in the data.
# 3. Steps for PCA:
# 
# #**Step 1: Getting the Optimal Number of Components:**
# 
# In the first step, PCA is performed on the original features.
# A scree plot is created to visualize the explained variance ratio as the number of components increases.
# The plot helps identify an optimal number of components that retain a significant portion of the variance while reducing dimensionality.
# 
# ##**Step 2: Selecting the Components:**
# 
# Based on the scree plot, you decided to retain three principal components.
# PCA is then applied with the chosen number of components.
# 
# ##**Step 3: Creating a New DataFrame:**
# 
# 
# A new DataFrame named principle_df is created, containing the transformed data with the selected principal components.
# The columns pca1, pca2, and pca3 represent the values of the first three principal components.
# 
# ##**4. Benefits of Using PCA:**
# 
# Dimensionality Reduction: PCA reduces the number of features, making it easier to work with and visualize the data.
# Visualization: Reduced-dimensional data can be easily visualized in 2D or 3D plots, aiding in the interpretation of player clusters.
# Improved Clustering: Clustering algorithms often perform better in lower-dimensional spaces with reduced noise.
# Interpretability: Principal components can reveal the most significant attributes driving player variations.
# Reduced Multicollinearity: PCA minimizes multicollinearity among features, which can be beneficial for clustering.
# 
# ##**Conclusion**
# 
# PCA is a valuable technique for dimensionality reduction and simplification of high-dimensional datasets like the one containing football player attributes.
# By selecting an optimal number of components (e.g., three in this case), you can effectively reduce dimensionality while preserving a significant portion of the variance.
# The resulting principle_df with three principal components can now be used for clustering football players based on their attributes, providing a more interpretable and manageable dataset for analysis.
# Overall, PCA is a powerful tool for feature engineering and simplifying complex datasets, making it easier to extract meaningful insights and patterns from the data.

# ### **K-MEANS CLUSTERING**

# In[300]:


#Step:1 Define independant veriable
X = features_to_scale
X.head()


# In[301]:


# Initalize the k value
from sklearn.cluster import KMeans
kmeans = KMeans() # Object creation
wcss = [] # Create empty list

for i in range(2,11):
    kmeans = KMeans(n_clusters=i,random_state=42)
    kmeans = kmeans.fit(X)
    wcss.append(kmeans.inertia_)
plt.figure(figsize=(10,7))
plt.plot(range(2,11),wcss,marker='*')
plt.title('The Elbow Method',fontsize=20)
plt.xlabel('Number of clusters',fontsize=20)
plt.ylabel('WCSS',fontsize=20)
plt.show()


# In[302]:


# Step:3 initalize the cluster
kmeans = KMeans(n_clusters=4,random_state=45)

# Step:4 Fitting the data
kmeans.fit(X)

# Step:5  Get labels
kmeans.labels_

# Step:6 Print dataset with labels
features_to_scale['cluster'] = pd.DataFrame(kmeans.labels_)
features_to_scale.head()


# In[303]:


# Step:7 initalize the centroids
kmeans.cluster_centers_


# In[304]:


# Step:8 Create a new veriable assign to labels
labels = kmeans.labels_
labels

# Step:9 import library to evaluate the model
from sklearn.metrics import silhouette_score
silhou_score = silhouette_score(X,labels)
print("Silhouette Score:",silhou_score)


# In[305]:


# Create a scatter plot using seaborn
sns.scatterplot(x=data.Overall_Rating, y=features_to_scale.Overall_positional_skill, hue=kmeans.labels_, palette='viridis')

# Add labels and legend
plt.xlabel('Overall_Rating')
plt.ylabel('Overall_positional_skill')
plt.title('Clustered Data with Colors')
plt.legend(loc='best')  # Add a legend for cluster colors

# Show the plot
plt.show()


# In[307]:


from sklearn.cluster import KMeans
from sklearn.metrics import silhouette_score

# Assuming you have standardized attributes in 'scaled_attributes'

# Try different values of 'k'
for k in range(2, 12):  # You can adjust the range as needed
    kmeans = KMeans(n_clusters=k, random_state=42)
    labels = kmeans.fit_predict(features_to_scale)
    silhouette_avg = silhouette_score(features_to_scale, labels)
    print(f"Silhouette Score for k={k}: {silhouette_avg}")


# #**Overview of K-Means Clustering:**
# 
# K-Means clustering is a popular unsupervised machine learning algorithm used to partition a dataset into distinct groups or clusters based on similarity. In this context, K-Means is applied to cluster football players based on their standardized attributes, including age, potential rating, value in euros, wage in euros, skill moves, work rate, overall positional skill, BMI, physical prowess, GK overall, goalkeeping skills aggregate, defending skills aggregate, and foot skills.
# 
# #**Steps in K-Means Clustering:**
# 
# **Data Preparation:**
# 
# The dataset is prepared with standardized features to ensure that each feature contributes equally to the clustering process.
# 
# **Choosing the Number of Clusters (K):**
# 
# The Elbow Method is employed to determine the optimal number of clusters (K) by evaluating the within-cluster sum of squares (WCSS) for a range of K values.
# The Elbow Method helps to identify an inflection point where increasing K provides diminishing returns in terms of reducing WCSS.
# 
# **Initializing K-Means:**
# 
# The K-Means algorithm is initialized with the chosen number of clusters (K), which in this case is 4 based on the Elbow Method.
# 
# **Fitting the Model:**
# 
# The K-Means algorithm is applied to the standardized dataset.
# 
# **Cluster Label Assignment:**
# 
# Each data point (football player) is assigned to one of the K clusters based on its similarity to the cluster centroids.
# Result Interpretation:
# 
# The dataset is augmented with cluster labels, indicating which cluster each player belongs to.
# 
# **Evaluating the Model:**
# 
# The silhouette score is calculated to evaluate the quality of the clustering. The silhouette score measures the similarity of each data point to its assigned cluster compared to other clusters. A higher silhouette score indicates better-defined clusters.
# 
#  # **Result:**
# 
# * The K-Means clustering algorithm has successfully clustered football players based on their standardized attributes into four distinct clusters.
# 
# * The silhouette score, a measure of clustering quality, is approximately **0.78**, indicating reasonable separation between clusters.
# 
# * To visualize the results, scatter plots were created, showing the clustering of players based on specific attributes like "Overall_Rating" and "Overall_positional_skill." These plots provide insights into how players are grouped based on these attributes.
# 
# ## **Conclusion**
# 
# K-Means clustering is a valuable technique for segmenting football players into meaningful clusters based on their attributes.
# The choice of four clusters was determined using the Elbow Method, and the resulting clusters are reasonably well-separated.
# Cluster analysis can help in various football-related tasks, such as team formation, player scouting, and performance analysis, by identifying players with similar attributes and playing styles.
# Further analysis and domain-specific knowledge can be applied to interpret the characteristics of each cluster and make informed decisions for team management and strategy.
# 
# 

# # **Task3:- Explore the data and attempt all the below asked questions.**

# In[312]:


df = pd.read_csv('players_20.csv')


# In[318]:


df.head(3)


# ### Prepare a rank ordered list of top 10 countries with most players. Which countries are producing the most footballers that play at this level?

# In[319]:


# Assuming your dataset is named 'data' and the nationality column is named 'Nationality'
top_countries = df['nationality'].value_counts().head(10)

# Print the top 10 countries with the most players
print("Top 10 Countries with the Most Players:")
print(top_countries)


# **Based on the available data, here is a rank-ordered list of the top 10 countries with the most players:**
# 
# 1.England
# 
# 2.Germany
# 
# 3.Spain
# 
# 4.France
# 
# 5.Argentina
# 
# 6.Italy
# 
# 7.Brazil
# 
# 8.Netherlands
# 
# 9.Portugal
# 
# 10.Chile
# 
# 
# **These countries are producing the most footballers at the level represented in the dataset. England leads the list with the highest number of players, followed closely by Germany and Spain. This indicates that these countries have a strong footballing culture and a significant presence in the dataset.**

# ### **Plot the distribution of overall rating vs. age of players. Interpret what is the age after which a player stops improving?**

# In[324]:


import matplotlib.pyplot as plt

# Plotting the distribution of Overall Rating vs. Age
plt.figure(figsize=(10, 6))
plt.scatter(df['age'], df['overall'], alpha=0.5)
plt.title('Distribution of Overall Rating vs. Age')
plt.xlabel('age')
plt.ylabel('overall')
plt.grid(True)

# Adding a trend line or regression line
import numpy as np
from scipy.stats import linregress

slope, intercept, r_value, p_value, std_err = linregress(df['age'], df['overall'])
age_range = np.arange(df['age'].min(), df['age'].max() + 1)
rating_pred = intercept + slope * age_range
plt.plot(age_range, rating_pred, color='red', linestyle='--', label='Trend Line')

# Show the plot
plt.legend()
plt.show()


# 1.The scatter plot shows how the overall rating of players is distributed across different ages.
# 
# 2.The trend line helps us see the general trend of how overall rating changes with age.
# 
# 3.In general, players tend to improve in their early twenties and reach their peak overall rating. After a certain age (usually in the late twenties or early thirties), the overall rating may start to decline.
# 
#  **players tend to stop improving significantly and reach their peak performance in their mid to late 20s, as indicated by the distribution of overall rating vs. age. After this age range, the rate of improvement slows down or levels off for most players.**

# ### **Which type of offensive players tends to get paid the most: the striker, the right-winger, or the left-winger?**

# In[325]:


# Assuming you have a DataFrame named 'data' containing player data
# Filter the data for ST, RS, and LS positions
offensive_players = df[df['player_positions'].str.contains('st|rs|ls', case=False, regex=True)]

# Calculate the average wage for each position
average_wage_by_position = offensive_players.groupby('player_positions')['wage_eur'].mean().reset_index()

# Sort the positions by average wage in descending order
average_wage_by_position = average_wage_by_position.sort_values(by='wage_eur', ascending=False)

# Display the result
print(average_wage_by_position)


# **Based on the provided data, the type of offensive player position that tends to get paid the most in terms of average wage (Wage_EUR) is "RW, CF, ST" (Right Wing, Center Forward, Striker), followed by "CF, LW, ST" (Center Forward, Left Wing, Striker), and "CF, ST, LW" (Center Forward, Striker, Left Wing).**
# 
# **Here is the ranked list of offensive player positions by average wage:**
# 
# **RW, CF, ST: €565,000.00**
# 
# **CF, LW, ST: €140,000.00**
# 
# **CF, ST, LW: €126,000.00**
# 
# **It appears that players with the "RW, CF, ST" position tend to have the highest average wage among the three positions listed.**

# ## **Team Details**
# * Team ID - PTID-CDS-AUG-23-1609
# * Team Members mail_id -
# ssmmtj2511@gmail.com,
# rahini15ece@gmail.com,
# payalkharkar8@gmail.com,
# dishantkharkar9@gmail.com,
# meghamalasadangi616@gmail.com.
# 
# **Thank you**
# 

# In[ ]:




