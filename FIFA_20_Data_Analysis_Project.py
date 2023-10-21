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

# In[1]:


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


# ## **Adding TechnicalSkills as a new column**

# In[125]:


# Select the technical attribute columns
technical_attributes = ['Dribbling', 'Pace', 'Shooting', 'Physic', 'Passing', 'Defending']

# Calculate the average technical skills for each player
data['TechnicalSkills'] = data[technical_attributes].mean(axis=1)


# In[126]:


# drop extasting columns
data.drop(['Dribbling', 'Pace', 'Shooting', 'Physic', 'Passing', 'Defending'],1,inplace=True)


# In[127]:


data.head()


# # **Feature Selection**

# In[128]:


corr=data.corr()


# In[129]:


plt.figure(figsize=(30,30))
sns.heatmap(data.corr(),annot=True,cmap=plt.cm.RdYlGn)
plt.show()


# In[130]:


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


# In[131]:


corr_features = correlation(data, 0.7)
len(set(corr_features))


# In[132]:


corr_features


# In[133]:


data.drop(columns=corr_features, inplace=True)


# In[134]:


data.head()


# In[ ]:




