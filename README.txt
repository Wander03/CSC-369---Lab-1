Name: Andrew Kerr

Part 1:
After looking at the json file and Part 2 queries, I decided to partition by event ID since this would speed up 2 of the
required queries. This comes with the added benefit of the event IDs already being in ascending order, so I would not
need to sort them as well. My approach consists of two parts: counts the total number of lines and evenly splitting the
json file into 10 partitions. Lines 14 to 18 of my partition_prgm count the number of lines in the json and determine
the partition_size for partitions 0-8 (9 would vary depending on how well the total number divides by 10). The remainder
of my program goes through the lines of the json file one at a time (so only 1 line is read into memory at any given
moment - thank you yield), writing to a new partition.json file. Once the count of lines reaches its partition size, my
program starts on the next partition.json file from where it left off. In the "background", my program determines the
starting and ending event IDs in each partition.json and saves them to an index.json to be used in Part 2.

Part 2:
Queries 1 and 2 were simple due to my partitioning strategy and index.json file. Using the index file, I was easily able
to only read the partition.json files that hold the corresponding event IDs. Furthermore, since I knew that the IDs were
sorted in ascending order, I could stop the program from inspecting any unnecessarily lines. Query 3, 4, and 5 required
full scan of all partition jsons. This could have been avoided by selecting a different partitioning method, however
then Queries 1 and 2 would be difficult. Another possible improvement would be to include secondary indexes (partition
by document). This would greatly speed up Query 3 since then all the program would have to do is get the length of a few
lists.
