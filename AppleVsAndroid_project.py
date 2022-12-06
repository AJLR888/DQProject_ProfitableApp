#!/usr/bin/env python
# coding: utf-8

# # Importing Data

# In[1]:


from csv import reader

### The Google Play data set ###
opened_file = open('/Users/nonox/MyDataSets/GooglePlayStore.csv', encoding = 'utf8')
read_file = reader(opened_file)
android = list(read_file)
android_header = android[0]

### The Apple data set ###
opened_file = open('/Users/nonox/MyDataSets/AppleStore.csv', encoding = 'utf8')
read_fileI = reader(opened_file)
apple = list(read_fileI)
apple_header = apple[0]



        


# In[2]:


print(apple)


# 
# # Definition of the function.
# 

# In[3]:


def explore_data(dataset, start, end, rows_and_columns=False):
    dataset_slice = dataset[start:end]    
    for row in dataset_slice:
        print(row)
        print('\n')                                     # Add a new (empty) line after each printed row
    if rows_and_columns:
        print('Number of rows:', len(dataset))          #len() tells us about "how many of something"   
        print('Number of columns:', len(dataset[0]))    


# In[4]:


explore_data(apple,0,5,True)


# 
# # Testing the function
# 

# In[5]:


# Let's run the function "explore_data"

explore_data(android,0,3,True)


# 
# # Checking the *length* of each row
# 

# ## Apple

# In[6]:


# We will check each row lenth against
# the header row to spot any data discrepancy
# related to the row's lenth
for row in android:
    if len(row) != len(android_header):
        print(android_header)
        print('\n')                                             # Space between lines.
        print(row)
        print('\n')
        print("Index position is: ", android.index(row))        # If there is any data discrepancy, the affected row/s will be printed.
        print('Android column lenth: ', len(android_header))        
        print('Discrepant Android column lenth: ',len(row))


# In[7]:


# After identifying the discrepancy, we will delete the row affected
# this is, row 10472.

# But before we delete the "faulty" row we make sure by double checking
# that row 10473 is the row we need to delete.

print(android[10473])

#Also we check the lenth before deleting the row:
print('Current lenth: ', len(android))


# In[8]:


# Now we proceed to delete the row:

del(android[10473])           # Careful!!!! Run this only once, otherwise you will delete extra rows.


# In[9]:



# We check that the targeted row has been deleted, 
# by checking that all prior and post rows have the same lenth:

print(len(android[10471]))
print('\n')
print(len(android[10472]))
print('\n')
print(len(android[10473]))
print('\n')
print(len(android[10474]))
print('\n')
#As well as we check that the lenth has decreased by 1.
print('Current lenth: ', len(android))


# ## Android

# In[10]:


# We will check each row lenth against
# the header row to spot any data discrepancy
# related to the row's lenth
for row in apple:
    if len(row) != len(apple_header):
        print(apple_header)
        print('\n')                                           # Space between lines.
        print(row)
        print('\n')
        print("Index position is: ", apple.index(row))        # If there is any data discrepancy, the affected row/s will be printed.
        print('Android column lenth: ', len(apple_header))        
        print('Discrepant column lenth: ',len(row))


# # Checking Duplicates

# ## Android

# In[11]:


# Deleting duplicates on adroid dataset.

Android_DuplicatedApps = []
Android_NonDuplicatedApps = []

for row in android:
    AppName = row[0]
    if AppName in Android_NonDuplicatedApps:
        Android_DuplicatedApps.append(AppName)
    else:
        Android_NonDuplicatedApps.append(AppName)

        
print('Number of duplicated apps: ', len(Android_DuplicatedApps))
print('\n')
print('Sample of duplicated apps: ', Android_DuplicatedApps[3:10])
print('\n')


# ## Apple 

# In[12]:


# Deleting duplicates in Apple dataset.

Apple_DuplicatedApps = []
Apple_NonDuplicatedApps = []

for row in apple:
    AppName = row[0]
    if AppName in Apple_NonDuplicatedApps:
        Apple_DuplicatedApps.append(AppName)
    else:
        Apple_NonDuplicatedApps.append(AppName)

        
print('Number of duplicated apps: ', len(Apple_DuplicatedApps))
print('\n')
print('Sample of duplicated apps: ', Apple_DuplicatedApps[3:10])
print('\n')


# ## Apple: any problem found

# # Cleaning Duplicates

# ## Android

# In[13]:


# Among all duplicated apps, we will select those duplicated apps 
# with the highest number of reviews. We consider that it means 
# that is more recent in time, in other words the latest update.

# Step1: I will create an empty dictionary to host the app and its number of
# reviews.

Android_ReviewsMax = {}

# Step2: I will create a loop for the dataset, -android-, and I will store
# the duplicated apps in it.

for app in android[1:]:
    name = app[0]                  
    n_reviews = float(app[3])      
# Inside the loop I created two variables -name- and -n_reviews-. For every iteration, in each row, 
# I select each app |name| and its number of reviews |n_reviews|.

    if name in Android_ReviewsMax and Android_ReviewsMax[name] < n_reviews:   
        Android_ReviewsMax[name] = n_reviews                                      
# for each iteration in each row, if the app -name- already exist in my dictionary -android_ReviewMax- and its number of reviews is bigger than the number of reviews in my dictionary         
# I substitute the new "bigger" number of reviews in my dictionary.

    elif name not in Android_ReviewsMax:           
        Android_ReviewsMax[name] = n_reviews       
# If the app -name- is not in android_ReviewsMax
# I store the app -name- with its number of reviews in the dictionary I created -android_ReviewMax-
##############################
# Remember: 
#    1) The loop is run as many times as rows exists in the dataset, -android-.
#    2) Remember that the app name is in the header this is, the first row. That is why app[0].



# In[14]:


print('Expected length: ', len(android[1:]) - 1181) # I don't count the header
print('Actual length: ', len(Android_ReviewsMax))


# 
# # Putting together all data:
# 

# ## 1) I separate cleaned data vs no cleaned

# In[15]:


AndroidCleaned = []
AndroidAdded = []

for app in android[1:]:
    name = app[0]
    n_reviews = float(app[3])
    
    if (Android_ReviewsMax[name] == n_reviews) and (name not in AndroidAdded):
        AndroidCleaned.append(app)
        AndroidAdded.append(name)


# #### Apple: we don't do anything on apple as no duplicated were found

# 
# 
# ### Testing if we get the same length than before. 9659 rows.
# 

# In[16]:



explore_data(AndroidCleaned,0,3,True)
print('Header length(columns): ',len(android_header))
print('\n')


# 
# # Finding and removing foreign languages Apps.
# 

# ### Before starting, some clarifications:

# #### 1) Characters that are specific to English texts are encoded using the ASCII standard. Each ASCII character has a corresponding number between 0 and 127.
# 
# #### 2) We use ord(). Is a built-in function to find out the corresponding encoding number of -each- character, this is letter, number, etc..

# In[17]:


# Examples:

character = 'y'

# find unicode of P
unicode_char = ord(character)
print(unicode_char)
# Output: 121

##########################

character = '5'

# find unicode of P
unicode_char = ord(character)
print(unicode_char)
# Output: 53


# ### Create a function to remove any app if its name has more than 3 non-ASCII characters

# In[18]:


def IsEnglish(string):
    non_ascii = 0
    
    for character in string:
        if ord(character) > 127:
            non_ascii += 1
    
    if non_ascii > 3:
        return False
    else:
        return True


# ### Testing is_english() function.

# In[19]:


print(IsEnglish('This is a test1 💁👌🎍😍'))
print(IsEnglish('This is a test2 🎍😍'))


# ### Now, using the prior function I will select and store all apps that have a name in English language.
# 

# In[20]:


AndroidEnglish = []
AppleEnglish = []

for row in AndroidCleaned:
    name = row[0]
    if IsEnglish(name):
        AndroidEnglish.append(row)

for row in apple:
    name = row[0]
    if IsEnglish(name):
        AppleEnglish.append(row)
        
explore_data(AndroidEnglish, 0, 5, True)
print('\n')
explore_data(AppleEnglish, 0, 3, True)


# # The next step will be to isolate free apps, since that will be my market (free apps)

# In[21]:


# Let's find how many apps are free:

AndroidFreeApps = []
AppleFreeApps = []

for row in AndroidEnglish[1:]:
    Free = row[7]
    if Free == '0':
        AndroidFreeApps.append(row)
        

for row in AppleEnglish[1:]:
    Free = row[5]
    if Free == '0':
        AppleFreeApps.append(row)
        
print(len(AndroidFreeApps))
print(len(AppleFreeApps))


# # Development & Strategy

# ### My end goal is to find out what kind of apps attracts more people, the more people use our app the better for our revenues:
# 
# ## Strategy: 
# ### 1) Build a simple version of the app in Android.
# ### 2) If enough people are interested in the app, I will develop it further.
# ### 3) If the app is profitable, I will develop it in IOS system.
# 
# ### Therefore, I need to find an app that is succesfull in both markets
# ### 

# ## I will build a frequency table that shows: prime_genre, Genres, Category of the Google Play data set.

# ### I need two functions to analyze the frequency tables:
# #### a) A function to generate frequency tables that shows %
# #### b) A function to display the % in a descending order

# In[22]:


# I will build a frequency table for the prime_genre column of the App Store dataset.
# FristlyI will count the amount of apps for a certain genre. To do that will create
# a dictrionary named table.
def freq_table(dataset, index):
    Table = {}
    Total = 0
    
    for row in dataset:
        Total += 1
        Value = row[index]        #Sum up the number of rows.
        if Value in Table:        #I want to count the number of time that a genre(or a value) appears
            Table[Value] += 1     #If the genre is in the table, I sum up 1 unit. 
        else:
            Table[Value] = 1      #If not, I create the dictionary index and add 1 as a dictionary value.
    
    table_percentages = {}                              #I will calculate the percentages and return them.
    for key in Table:                                   #key means dictionary key which is the same than index.
        Percentage = (Table[key] / Total) * 100         #By typing -table[key]- we are calling to the dictionary value.
        table_percentages[key] = Percentage             #I asign -percentage- the dictionary value of -table_precentages- 
    
    return table_percentages


def display_table(dataset, index):
    Table = freq_table(dataset, index)                # I need to use the data extracted with the function freq_table, to do that I need to asign the results
    TableDisplay = []                                 # of -freq_table- to a variable, I will call the variable -Table-.
    for key in Table:                                 # I create a loop to iterate every index in the dictionary -table-. 
        KeyValueAsTuple = (Table[key], key)            # I want to create a tuple because it is easier to order the values.
        TableDisplay.append(KeyValueAsTuple)          # For every iteration, I change the order of the dictionary and store them as a tuple. 
                                                      # I place first the dictionary value, then the dictionary index.
        
    TableSorted = sorted(TableDisplay, reverse = True)    #I want to print the data. To do that I need to asign the organized data to a variable, called -TableSorted- 
    for entry in TableSorted:                             #
        print(entry[1], ':', entry[0])                    # Remember that I transformed the dictionary in a tuple, so that is why I 
                                                          # Example of frequency table as a tuple [(50,'Genre1'),(89,'Genre2'),(439,'Genre3')]
            
            


# ## I will print Prime_genre from Apple Store data set.

# In[29]:



display_table(AppleFreeApps,-5)


# ## Analyzing results for pime_genre in apple data set
# 
# ### Conclusions:
# #### 1) Games is by far the most common genre
# #### 2) There are 23 genres, 18 genres represent, individuallly, less than 3% over the total. In other words 78% of genres represent less than 3% of the total
# #### 3) The genre with less representation is "Medical"
# #### 4) Does existing apps in the genres with least representations satisfy the current demand? Does they have a high user rating?

# ## I will print Genres and category from Google Play data set.

# In[27]:


display_table(AndroidFreeApps, 1) #Category


# In[28]:


display_table(AndroidFreeApps, -4) #Genres


# ### Note: The previous data is related to the number of apps in each 'genre' / 'category'

# ## It would be interesting to know how many users have each genre.
# ## We can find this in Android data set as 'installs' column. But this information is not available on Apple data set, however we can count the number of 'user rating'

# ## Let's start with Apple data set. I will calculate the average number of user rating per app genre.

# In[6]:


GenresApple = freq_table(AppleFreeApps, -5)

for genre in GenresApple:
    Total = 0                    # I will store the number of ratings for each genre.
    LenGenre = 0                 # I will store the number of apps for each genre.
    for app in AppleFreeApps:    #
        GenreApp = app[-5]
        if GenreApp == genre:
            
        


# In[7]:


print(5   +3) 
print(3 -   4)


# In[3]:


if True:
    print(1)
else:
    print("a;sldifsafd")


# 
