fname = input("Enter your first name: ").capitalize()
lname = input("Enter your last name: ").capitalize()
prev_job = input("What was the last company you worked at? ")
yrs_at_prev_job = input("How long did you work there? ")
about = input("Write a little about yourself: ")

header = f"<h1>{fname} {lname}</h1>"
h2 = f"<h2>Previous job: {prev_job}. Worked there for {yrs_at_prev_job} years.</h2>"
p1 = f"<p>About Me: {about}</p>"

print(header)
print(h2)
print(p1)

