#!/bash/bin

#This script requires files with dates as a name
#You need to run partitioner first or
#you can uncomment the next line:

#sh partitioner.sh;

echo '“id”,“created_at”,“name”,“has_test”,“alternate_url”' > union.csv;
for i in 1 2
do	
	cat "`sed "${i}q;d" dates.txt`".csv | tail -n +2 >> union.csv;
done

#cat union.csv | sort -k1 > union.csv;
echo '“id”,“created_at”,“name”,“has_test”,“alternate_url”' > "`sed "${i}q;d" dates.txt`".csv;

head -n1 union.csv > final_union.csv;
tail -n +2 union.csv | sort -k2 -k1 >> final_union.csv;

rm union.csv;
rm dates.txt;
