import streamlit as st
import pandas as pd
from streamlit_option_menu import option_menu

totalMoneyGranted = 0
totalInterestCharged = 0

def tableBanking():
    applicant , amount  = st.columns(2)
    members = ("Patrick" , "Victor" ,"Laban", "Kirathi","Ndichu" , "Eng Muriithi","Joram" ,"Jomo" ,"General" ,"Jonte")
    #members.remove("Patrick")
 
    

    with applicant:
        st.header("Applicant")
        option1 = st.selectbox(
            'Select Loan Applicant' , 
            (members) , key = "applicant1" , label_visibility="collapsed" 
        )
    
        if option1:
        # st.write(option1)
            idx = members.index(option1)
            members =  members[:idx] + members[idx+1:]
            
        option2 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant2" 
        )

        if option2:
        # st.write(option1)
            idx = members.index(option2)
            members =  members[:idx] + members[idx+1:]
        
        option3 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant3"
        )
        if option3:
        # st.write(option1)
            idx = members.index(option3)
            members =  members[:idx] + members[idx+1:]

        option4 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant4"
        )
        if option4:
            # st.write(option1)
            idx = members.index(option4)
            members =  members[:idx] + members[idx+1:]
        
        option5 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant5"
        )
        if option5:
            # st.write(option1)
            idx = members.index(option5)
            members =  members[:idx] + members[idx+1:]
        
        option6 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant6"
        )
        if option6:
            # st.write(option1)
            idx = members.index(option6)
            members =  members[:idx] + members[idx+1:]

        option7 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant7"
        )
        if option7:
            # st.write(option1)
            idx = members.index(option7)
            members =  members[:idx] + members[idx+1:]

        option8 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant8"
        )
        if option8:
            # st.write(option1)
            idx = members.index(option8)
            members =  members[:idx] + members[idx+1:]

        option9 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant9"
        )
        if option9:
            # st.write(option1)
            idx = members.index(option9)
            members =  members[:idx] + members[idx+1:]

        option10 = st.selectbox(
            '' ,
            (members) , label_visibility="collapsed" ,  key =  "applicant10"
        )
        if option10:
            # st.write(option1)
            idx = members.index(option10)
            members =  members[:idx] + members[idx+1:]
        

    with amount:
        st.header("Amount")
        amount1 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount1")
        amount2 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount2")
        amount3 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount3")
        amount4 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount4")
        amount5 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount5")
        amount6 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount6")
        amount7 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount7")
        amount8 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount8")
        amount9 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount9")
        amount10 = st.number_input('Loan Amount' ,  label_visibility="collapsed" , key =  "amount10")

    if st.button('Submit'):
        loanAmounts = [amount1,amount2,amount3,amount4,amount5,amount6,amount7,amount8,amount9,amount10]

        applicantsToOmit = loanAmounts.count(0)
        st.write('Applicants To Omit ' , applicantsToOmit)

        if applicantsToOmit < 10:
            validApplicants = 10 - applicantsToOmit
            roundOneAllocation = 3000 * validApplicants

            totalAmountBorrowed = amount1 + amount2 + amount3 + amount4 + amount5 + amount6 + amount7 + amount8+ amount9 + amount10
            #Get shared balance
            Principal = 30000
            sharedBalance = Principal - roundOneAllocation
            cumulativeExcess = totalAmountBorrowed - roundOneAllocation
            st.write('Total Loan applied : ' , totalAmountBorrowed)
            st.write('Shared Balance after First Allocation ' , sharedBalance)
            st.write('Cummulative Excess ' , cumulativeExcess)
            st.write('*************************************************************')

            

            def returnGrantedAmount(requestedAmount , sharedBalance , cumulativeExcess):
                global totalMoneyGranted
                global totalInterestCharged
                if requestedAmount != 0:
                   

                    if Principal > totalAmountBorrowed:
                        grantedAmount = requestedAmount
                    else:
                        grantedAmount = round(int((((requestedAmount - 3000) / cumulativeExcess) * sharedBalance) + 3000) / 500) * 500

                    requestedLoan = requestedAmount           
                    Interest = grantedAmount / 10
                    paybackAmount = grantedAmount + Interest

                    totalMoneyGranted += grantedAmount
                    totalInterestCharged += Interest


                    return [requestedLoan , grantedAmount , Interest , paybackAmount , totalMoneyGranted , totalInterestCharged]
                        
                else:
                    return [0 , 0 , 0 , 0 , 0 , 0]
            
            
            
            person1= returnGrantedAmount(amount1, sharedBalance , cumulativeExcess )
            person2= returnGrantedAmount(amount2, sharedBalance , cumulativeExcess )
            person3= returnGrantedAmount(amount3, sharedBalance , cumulativeExcess )
            person4= returnGrantedAmount(amount4, sharedBalance , cumulativeExcess )
            person5= returnGrantedAmount(amount5, sharedBalance , cumulativeExcess )
            person6= returnGrantedAmount(amount6, sharedBalance , cumulativeExcess )
            person7= returnGrantedAmount(amount7, sharedBalance , cumulativeExcess )
            person8= returnGrantedAmount(amount8, sharedBalance , cumulativeExcess )
            person9= returnGrantedAmount(amount9, sharedBalance , cumulativeExcess )
            person10= returnGrantedAmount(amount10, sharedBalance , cumulativeExcess )



            #st.write(option1 , ' Requested ' ,  person1[0] , ' Granted ' , person1[1] )

            def load_data():
                return pd.DataFrame(
                    {
                        "No": [1,2,3,4,5,6,7,8,9,10,"Totals: "],
                        "Applicant" : [option1,option2,option3,option4,option5,option6,option7,option8,option9,option10 , "Totals: "],
                        "Loan Requested ": [person1[0],person2[0],person3[0],person4[0],person5[0],person6[0],person7[0],person8[0],person9[0],person10[0] ,totalAmountBorrowed ],
                        "Loan Granted ": [person1[1],person2[1],person3[1],person4[1],person5[1],person6[1],person7[1],person8[1],person9[1],person10[1] , totalMoneyGranted],
                        "Interest Charged": [person1[2],person2[2],person3[2],person4[2],person5[2],person6[2],person7[2],person8[2],person9[2],person10[2] , totalInterestCharged],
                        "Payment amount": [person1[3],person2[3],person3[3],person4[3],person5[3],person6[3],person7[3],person8[3],person9[3],person10[3] , ""]

                    } 
                    )
            df = load_data()
            st.dataframe(df)
        else:
            st.write('Please Input Values')
    else:
        st.write('Please select loans')


selected = option_menu(
    menu_title=None,
    options = ["Main App" , "Table Banking" , "Financials"],
    icons= ["house" , "bank" ,"money"],
    menu_icon="cast",
    default_index = 0,
    orientation="horizontal",
)

if selected == "Table Banking":
    tableBanking()




