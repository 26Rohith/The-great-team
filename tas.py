
def run():
    with open("tips.txt",'r') as con:
        content=con.read()
    with open("All about your interview.pdf",'w') as d:
    	d.write(content)
