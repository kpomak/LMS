import json


def create_mark(obj, table):
    with open("LMS/mainapp/fixtures/temp", "w") as file:
        for item in obj:
            file.write(f"{table}.objects.create(")
            for field in item["fields"]:
                name = item["fields"][field]
                file.write('\n\t{0}="{1}",'.format(field, name))
            file.write("\n)\n")

    # return f"Courses.objects.create(\n\tname={obj['fields']['name']}\n\tdescription=\
    #     {obj['fields']['description']}\n\tdescription_as_markdown={obj['fields']['description_as_markdown']}\n\t"


data_list = []

with open("LMS/mainapp/fixtures/002_courses.json") as f:
    data_list = json.load(f)

create_mark(data_list, "Courses")
# create_mark(data_list,'CoursesTeachers')

# print(r'{0}'.format(data_list[0]['fields']['description']))
