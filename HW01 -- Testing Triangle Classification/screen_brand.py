from datetime import datetime
now = datetime.now()
dt_string = now.strftime("%Y-%m-%d %H:%M:%S")

def my_brand(assignment):
    print("""\n=*=*=*= Jason McCauley =*=*=*=

=*=*=*= Course 2024F-SSW567-WS =*=*=*= 

=*=*=*= """ + assignment + """ =*=*=*= 

=*=*=*= """ + dt_string + """ =*=*=*= \n""")