import aboutInterview as ai
import Resume as res
import coverletter as cl
import ipq as ipq
import tas as tas

print("Welcome to interview buddy")
print("How can we assist you?")
while True:
  print("1.About Interviews\n2.Make a resume\n3.Write a cover letetr\n4.Important questions\n5.Tips and Suggetsions\n6.Body Language\n7.End the application")
  ip1=int(input("Enter your option: "))
  match ip1:
    case 1:
      ai.about()
    case 2:
      res.resume()
    case 3:
      cl.writeup()
    case 4:
		ipq.questions()
	case 5:
		tas.tas()		
	case 6:
		bl.language()
	case 7:
		break
		
