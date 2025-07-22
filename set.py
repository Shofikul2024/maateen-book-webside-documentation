# A = {'orange', 'banana', 'pear', 'apple'}
# # print( type(A))
# print(A)








# A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# print(A)



# a=set()
# print(type(a))





# a={}
# print(type(a))





# A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
# A.add('shofikul' )
 
# print(A)









''' আমরা একবার নরমালি দুইটা এলিমেন্ট পাস করেছিলাম। 
কিন্তু তখন জিনিসগুলা ক্যারেক্টার হিসাবে ভাগ হয়ে সেটে অ্যাড হয়েছে।
আমরা যেভাবে দিয়েছি সেভাবে অ্যাড করার জন্য 
এলিমেন্টগুলোকে {} চিহ্নের ভিতরে পুরে পাঠাতে হবে। 

'''

A = {'apple', 'orange', 'apple', 'pear', 'orange', 'banana'}
 
A.update({'berry', 'grape'})
print(A)