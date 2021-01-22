# Dependencies and Setup
import pandas as pd

# File to Load (Remember to Change These)
file_to_load = "Resources/purchase_data.csv"

# Read Purchasing File and store into Pandas data frame
purchase_data = pd.read_csv(file_to_load)


#Player Count
player_df = purchase_data.drop_duplicates(subset=['SN'])
player_count = len(player_df)
print(player_count)


#Purchasing Analysis
item_df = purchase_data.drop_duplicates(subset=['Item ID'])
unique_items = len(item_df)
print(unique_items)


average_price = round(purchase_data['Price'].mean(), 2)
print(average_price)


total_purchases = len(purchase_data)
print(total_purchases)

total_revenue = round(sum(purchase_data['Price']), 2)
print(total_revenue)


#Gender Demographics
male_players_df = player_df[player_df['Gender'] == 'Male']
male_player_count = len(male_players_df)
male_player_percentage = round(((male_player_count / player_count) * 100), 2)
print(male_player_count)
print(str(male_player_percentage)+"%")


female_players_df = player_df[player_df['Gender'] == 'Female']
female_player_count = len(female_players_df)
female_player_percentage = round(((female_player_count / player_count) * 100), 2)
print(female_player_count)
print(str(female_player_percentage)+"%")

other_players_df = player_df[player_df['Gender'] == 'Other / Non-Disclosed']
other_player_count = len(other_players_df)
other_player_percentage = round(((other_player_count / player_count) * 100), 2)
print(other_player_count)
print(str(other_player_percentage)+"%")


#Purchasing Analysis (Gender)
male_purchase_df = purchase_data[purchase_data['Gender'] == 'Male']
male_dup_players_dropped = male_purchase_df.drop_duplicates(subset=['SN'])
male_purchase_count = len(male_dup_players_dropped)
print(male_purchase_count)
male_average_purchase = round(male_purchase_df['Price'].mean(), 2)
print(male_average_purchase)
male_total_purchase = round(sum(male_purchase_df['Price']), 2)
print(male_total_purchase)
male_total_per = round((male_total_purchase / male_player_count), 2)
print(male_total_per)


female_purchase_df = purchase_data[purchase_data['Gender'] == 'Female']
female_dup_players_dropped = female_purchase_df.drop_duplicates(subset=['SN'])
female_purchase_count = len(female_dup_players_dropped)
print(female_purchase_count)
female_average_purchase = round(female_purchase_df['Price'].mean(), 2)
print(female_average_purchase)
female_total_purchase = round(sum(female_purchase_df['Price']), 2)
print(female_total_purchase)
female_total_per = round((female_total_purchase / female_player_count), 2)
print(female_total_per)


other_purchase_df = purchase_data[purchase_data['Gender'] == 'Other / Non-Disclosed']
other_dup_players_dropped = other_purchase_df.drop_duplicates(subset=['SN'])
other_purchase_count = len(other_dup_players_dropped)
print(other_purchase_count)
other_average_purchase = round(other_purchase_df['Price'].mean(), 2)
print(other_average_purchase)
other_total_purchase = round(sum(other_purchase_df['Price']), 2)
print(other_total_purchase)
other_total_per = round((other_total_purchase / other_player_count), 2)
print(other_total_per)


#Age Demographics
#Years_9
years_9 = purchase_data[purchase_data["Age"] < int(10)]
years_9_purchase_count = len(years_9)
print(years_9_purchase_count)
years_9_average_purchase = round(years_9['Price'].mean(), 2)
print(years_9_average_purchase)
years_9_total_purchase = years_9['Price'].sum()
print(years_9_total_purchase)
years_9_dup_players_dropped = years_9.drop_duplicates(subset=['SN'])
years_9_purchase_count = len(years_9_dup_players_dropped)
print(years_9_purchase_count)


#years_10_14
years_10_14 = purchase_data[(purchase_data["Age"] >= int(10)) & (purchase_data["Age"] <= int(14))]
years_10_14_purchase_count = len(years_10_14)
print(years_10_14_purchase_count)
years_10_14_average_purchase = round(years_10_14['Price'].mean(), 2)
print(years_10_14_average_purchase)
years_10_14_total_purchase = years_10_14['Price'].sum()
print(years_10_14_total_purchase)
years_10_14_dup_players_dropped = years_10_14.drop_duplicates(subset=['SN'])
years_10_14_purchase_count = len(years_10_14_dup_players_dropped)
print(years_10_14_purchase_count)


#years_15_19
years_15_19 = purchase_data[(purchase_data["Age"] >= int(15)) & (purchase_data["Age"] <= int(19))]
years_15_19_purchase_count = len(years_15_19)
print(years_15_19_purchase_count)
years_15_19_average_purchase = round(years_15_19['Price'].mean(), 2)
print(years_15_19_average_purchase)
years_15_19_total_purchase = years_15_19['Price'].sum()
print(years_15_19_total_purchase)
years_15_19_dup_players_dropped = years_15_19.drop_duplicates(subset=['SN'])
years_15_19_purchase_count = len(years_15_19_dup_players_dropped)
print(years_15_19_purchase_count)


#years_20_24
years_20_24 = purchase_data[(purchase_data["Age"] >= int(20)) & (purchase_data["Age"] <= int(24))]
years_20_24_purchase_count = len(years_20_24)
print(years_20_24_purchase_count)
years_20_24_average_purchase = round(years_20_24['Price'].mean(), 2)
print(years_20_24_average_purchase)
years_20_24_total_purchase = years_20_24['Price'].sum()
print(years_20_24_total_purchase)
years_20_24_dup_players_dropped = years_20_24.drop_duplicates(subset=['SN'])
years_20_24_purchase_count = len(years_20_24_dup_players_dropped)
print(years_20_24_purchase_count)


#years_25_29
years_25_29 = purchase_data[(purchase_data["Age"] >= int(25)) & (purchase_data["Age"] <= int(29))]
years_25_29_purchase_count = len(years_25_29)
print(years_25_29_purchase_count)
years_25_29_average_purchase = round(years_25_29['Price'].mean(), 2)
print(years_25_29_average_purchase)
years_25_29_total_purchase = round(years_25_29['Price'].sum(),2)
print(years_25_29_total_purchase)
years_25_29_dup_players_dropped = years_25_29.drop_duplicates(subset=['SN'])
years_25_29_purchase_count = len(years_25_29_dup_players_dropped)
print(years_25_29_purchase_count)

#years_30_34
years_30_34 = purchase_data[(purchase_data["Age"] >= int(30)) & (purchase_data["Age"] <= int(34))]
years_30_34_purchase_count = len(years_30_34)
print(years_30_34_purchase_count)
years_30_34_average_purchase = round(years_30_34['Price'].mean(), 2)
print(years_30_34_average_purchase)
years_30_34_total_purchase = round(years_30_34['Price'].sum(), 2)
print(years_30_34_total_purchase)
years_30_34_dup_players_dropped = years_30_34.drop_duplicates(subset=['SN'])
years_30_34_purchase_count = len(years_30_34_dup_players_dropped)
print(years_30_34_purchase_count)


#years_35_39
years_35_39 = purchase_data[(purchase_data["Age"] >= int(35)) & (purchase_data["Age"] <= int(39))]
years_35_39_purchase_count = len(years_35_39)
print(years_35_39_purchase_count)
years_35_39_average_purchase = round(years_35_39['Price'].mean(), 2)
print(years_35_39_average_purchase)
years_35_39_total_purchase = years_35_39['Price'].sum()
print(years_35_39_total_purchase)
years_35_39_dup_players_dropped = years_35_39.drop_duplicates(subset=['SN'])
years_35_39_purchase_count = len(years_35_39_dup_players_dropped)
print(years_35_39_purchase_count)



#years_40_44
years_40_44 = purchase_data[(purchase_data["Age"] >= int(40)) & (purchase_data["Age"] <= int(44))]
years_40_44_purchase_count = len(years_40_44)
print(years_40_44_purchase_count)
years_40_44_average_purchase = round(years_40_44['Price'].mean(), 2)
print(years_40_44_average_purchase)
years_40_44_total_purchase = years_40_44['Price'].sum()
print(years_40_44_total_purchase)
years_40_44_dup_players_dropped = years_40_44.drop_duplicates(subset=['SN'])
years_40_44_purchase_count = len(years_40_44_dup_players_dropped)
print(years_40_44_purchase_count)


#years_45_49
years_45_49 = purchase_data[(purchase_data["Age"] >= int(45)) & (purchase_data["Age"] <= int(49))]
years_45_49_purchase_count = len(years_45_49)
print(years_45_49_purchase_count)
years_45_49_average_purchase = round(years_45_49['Price'].mean(), 2)
print(years_45_49_average_purchase)
years_45_49_total_purchase = years_45_49['Price'].sum()
print(years_45_49_total_purchase)
years_45_49_dup_players_dropped = years_45_49.drop_duplicates(subset=['SN'])
years_45_49_purchase_count = len(years_45_49_dup_players_dropped)
print(years_45_49_purchase_count)


player_list = []
purchase_list = []
for x in range(len(player_df)):
    player = player_df["SN"].iat[x]
    player_purchase_df = purchase_data[purchase_data["SN"] == str(player)]
    player_purchase_total = round(sum(player_purchase_df["Price"]),2)
    player_list.append(player)
    purchase_list.append(player_purchase_total)




columns = ["Player", "Purchase_Total"]
player_purchase_total_df = pd.DataFrame(list(zip(player_list, purchase_list)), columns = columns)
player_purchase_total_df = player_purchase_total_df.sort_values(['Purchase_Total'], ascending=False)
player_purchase_total_df_filtered = player_purchase_total_df[:5]
print(player_purchase_total_df_filtered)











