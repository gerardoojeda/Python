import pandas as pd
#pandas works with dataframes lets call it data frames
df=pd.read_csv('pokemon_data.csv')
#filtering data
#this will get us the row of pkemons that have grass AND are poison and HP>70
AND=df.loc[(df['Type 1']=='Grass') & (df['Type 2']=='Poison') & (df['HP']>70)]
print(AND)
#this will get us the row of pkemons that have grass OR are poison
OR=df.loc[(df['Type 1']=='Grass') | (df['Type 2']=='Poison')]
print(OR.head(10))
#CHECK ALL DE MEGA POKEMONS
print(df.loc[df['Name'].str.contains('Mega')])
#A LIST WITH NO MEGA PKEMONS USE THE NOT AS ~
print(df.loc[~df['Name'].str.contains('Mega')])
#---------------------------------------------------------------------
#LETS CHANGE THE FIRE TYPE TO FIRY
df.loc[df['Type 1']=='Fire','Type 1']='Fuego'
print(df)
#LETS CHANGE THE FUEGO TYPE TO LEGENDARY
df.loc[df['Type 1']=='Fuego','Legenary']=True
print(df.head(10))
#----------------------------------------------------------------------
#statistics with statistics
df=pd.read_csv('pokemon_data.csv')#restanting the data for future excersises
print(df.groupby(['Type 1']).mean())#this would give us the mean of their stats grouped by Type 1
print(df.groupby(['Type 1']).mean().sort_values('Attack',ascending=False))#this would give us the mean of their stats grouped by Type 1  with special focus on the type of pokemosn with highest attack
print(df.groupby(['Type 1']).sum())#this would sum up all the values for each trype 1
print(df.groupby(['Type 1']).count())#this would count how many of each Type 1 pkemons are there
#lets look to see how to arrange better
df['Count']=1
print(df.groupby(['Type 1','Type 2']).count()['Count'])
#-----------------------------------------------------------------------------------------------------
#LARGE AMOUNTS OF DATA
#lets create a new data frame
new_df=pd.DataFrame(columns=df.columns)#here we are creating an empy Data frame

for df in pd.read_csv('pokemon_data.csv',chunksize=5):#chunkcsize are the rows
    print("Chunksize in DF: ")
    print(df)
    results=df.groupby(['Type 1']).count()

    new_df=pd.concat([new_df,results])# in each chunk we are filling up new_Df with the count given by type 1
print(new_df.head(5))