import pandas as pd
#pandas works with dataframes lets call it data frames
df=pd.read_csv('pokemon_data.csv')
print(df.head(3))#shows te first 3 rows
print(df.tail(3))#shows te last 3 rows
#Read teh heathers
print(df.columns)
#Read an specific column
print(df['Name'])
#multiple colums
print(df[['Name','Type 1','Legendary']])
#-----------------------------------------------------
#now rows
print(df.iloc[1])#this will give me all the atributes from that row
print(df.iloc[0:15])#this will give me all the atributes from row 0 to 14
#-------------------------------------------------------
print('aqui\n')
#specific location(Row,Colum)
print(df.iloc[2,1])#this will get us the value at row 2 and column 1
#------------------------------------------------------
#go through the rows
for index,row in df.iterrows():
    print(index,row['Name'])
#---------------------------------------------------
#get attributes from specific things
df.loc[df['Type 1']=="Fire"]
#---------------------------------------------------------------
#sorting values
print(df.sort_values('Name',ascending=False))
#this would get the names but backwards
#---------------------------------------------------------------
# MAKING CHANGES TO THE DATA
print(df.head(0))
#rank pokemons based on their stats
#adda colum suming all the stats
df['Total']=df['HP']+df['Attack']+df['Defense']+df['Speed']
print(df.head(3))
df=df.drop(columns=['Total'])#this would errase the column total
print(df.head(3))
#another way would be
df['Total']=df.iloc[:,4:10].sum(axis=1)

#save csv
df.to_csv('modified.csv')
#save as excel
#df.to_excel('excel.xlsx',index=False)
#save as txt
df.to_csv('pokemon_modified.txt',index=False,sep='\t')