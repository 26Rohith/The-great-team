def run():
    title=input("enter title:")
    f="From"
    name=input("enter your name:")
    roll=input("Enter your roll number:")
    coll=input("Enter college name")
    loc=input("Enter location")
    f1="To"
    to=input("Enter to whom you are writing")
    clg=input("Enter you clg name")
    loc1=input("location of your clg")
    sub=input("Enter the sub:")
    salutation=input("salutation:")
    body=input("Enter the content:")
    by=input("at last:")


    #var=title,f,name,roll,coll,loc,f1,to,clg,loc1,sub,salutation,body
    a=open("data.txt","w")
    #a.write(str(var))
    #a.close()


    f=open("data.txt",'w')
    content=""
    while(True):
        ip=input()
        content=content+ip
        if '@' in ip:
            break
    str1=f'''"content":"{content}",'''
    str2=f'''"f":"{f}",'''
    str3=f'''"name":"{name}",'''
    str4=f'''"roll":"{roll}",'''
    str5=f'''"coll":"{coll}",'''
    str6=f'''"loc":"{loc}",'''
    str7=f'''"f1":"{f1}",'''
    str8=f'''"to":"{to}",'''
    str9=f'''"clg":"{clg}",'''
    str10=f'''"loc1":"{loc1}",'''
    str11=f'''"sub":"{sub}",'''
    str12=f'''"salutation":"{salutation}",'''

    str13=f'''"body":"{body}",'''
    str14=f'''"by":"{by}",'''
    data=str1+str2+str3+str4+str5+str6+str7+str8+str9+str10+str11+str12+str13+str14
    strf="data="+"{"+data+"}"
    a.write(strf)
    a.close()
    for i in strf:
        print(i)
