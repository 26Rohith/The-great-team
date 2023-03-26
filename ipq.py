def run():
    with open("questions.txt",'r') as con:
        content=con.read()
    with open("Important questions.pdf",'w') as d:
    	d.write(content)
