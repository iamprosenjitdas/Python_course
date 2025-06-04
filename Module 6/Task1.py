stu_dict={"Ram":100,"Lakshman":99.99,"Bharat":99.5}
find_name=input("Enter the name of the student for search")
stu_names=stu_dict.keys()
if find_name.lower() in stu_names:
	print("{}'s mark is:{}".format(find_name.lower(), stu_dict[find_name.lower()]))
if find_name.upper() in stu_names:
	print("{}'s mark is:{}".format(find_name.upper(), stu_dict[find_name.upper()]))
if find_name.capitalize() in stu_names:
	print("{}'s mark is:{}".format(find_name.capitalize(),stu_dict[find_name.capitalize()]))
else:
	print("Student not found")