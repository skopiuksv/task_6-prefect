query_create_tables1 = 'create or replace table raw_table (\
        "_ID" varchar(16777216),\
        "IOS_App_Id" NUMBER(38,0),\
        "Title" varchar(16777216),\
        "Developer_Name" VARCHAR(16777216),\
        "Developer_IOS_Id" FLOAT,\
        "IOS_Store_Url" VARCHAR(16777216),\
        "Seller_Official_Website" VARCHAR(16777216),\
        "Age_Rating" VARCHAR(16777216),\
        "Total_Average_Rating" FLOAT,\
        "Total_Number_of_Ratings" FLOAT,\
        "Average_Rating_For_Version" FLOAT,\
        "Number_of_Ratings_For_Version" NUMBER(38,0),\
        "Original_Release_Date" VARCHAR(16777216),\
        "Current_Version_Release_Date" VARCHAR(16777216),\
        "Price_USD" FLOAT,\
        "Primary_Genre" VARCHAR(16777216),\
        "All_Genres" VARCHAR(16777216),\
        "Languages" VARCHAR(16777216),\
        "Description" VARCHAR(16777216)\
        );'

query_create_tables2 = 'create or replace table stage_table like raw_table;'
query_create_tables3 = 'create or replace table master_table like raw_table;'

query_create_streams1 = 'create or replace stream raw_stream on table raw_table;'
query_create_streams2 = 'create or replace stream stage_stream on table stage_table;'

query_insert_data_1 = 'insert into stage_table select "_ID", "IOS_App_Id","Title","Developer_Name","Developer_IOS_Id",\
 "IOS_Store_Url","Seller_Official_Website","Age_Rating","Total_Average_Rating",\
 "Total_Number_of_Ratings","Average_Rating_For_Version","Number_of_Ratings_For_Version",\
 "Original_Release_Date","Current_Version_Release_Date","Price_USD","Primary_Genre","All_Genres","Languages","Description" from raw_stream;'

query_insert_data_2 = 'insert into master_table select "_ID", "IOS_App_Id","Title","Developer_Name","Developer_IOS_Id",\
 "IOS_Store_Url","Seller_Official_Website","Age_Rating","Total_Average_Rating",\
 "Total_Number_of_Ratings","Average_Rating_For_Version","Number_of_Ratings_For_Version",\
 "Original_Release_Date","Current_Version_Release_Date","Price_USD","Primary_Genre","All_Genres","Languages","Description" from stage_stream;'
